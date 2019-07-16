import base64
import hashlib
import hmac
import logging
from datetime import datetime
from logging import Logger
from websocket import WebSocketApp
from cws.client.client_pb2 import ClientMessage
from cws.stream.stream_pb2 import StreamMessage


class WebsocketClient:
    logger: Logger

    _CW_WEBSOCKET_ENDPOINT = 'wss://stream.cryptowat.ch'
    _handlers: dict
    _api_key: str
    _api_secret: str
    _wsa: WebSocketApp

    """
    Simple websocket client for cryptowat.ch.
    Default INFO stdout stream logger will be created if not provided. 
        api_key      API Key, can be obtained at https://cryptowat.ch/account/api-access
        api_secret   API Secret, can be obtained at https://cryptowat.ch/account/api-access
        logger       Replace default stream logger with logging.Logger instance
        debug        Verbose logging level, will log every message. 
    """
    def __init__(self, api_key: str, api_secret: str, logger=None, debug=False):
        self._api_key = api_key
        self._api_secret = api_secret

        self._handlers = {}

        if logger is None:
            self.logger = logging.getLogger('WebsocketClient')
            stream_handler = logging.StreamHandler()
            formatter = logging.Formatter(fmt='%(asctime)s: %(levelname)s: %(message)s')
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
            self.logger.setLevel(logging.INFO if not debug else logging.DEBUG)
        else:
            if isinstance(logger, Logger):
                self.logger = logger
            else:
                raise ValueError(f'logger must be instance of logging.Logger, got {type(logger)}')

        self._wsa = WebSocketApp(
            self._CW_WEBSOCKET_ENDPOINT,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )

    """
    Register a handler for a specific message type. 
    Multiple handlers for same message type will be stored. 
    Multiple handlers will be called in stored order. 
        message_type    Type of a message (first non-empty field in the message)
        handler         Callable handler for given message type
    """
    def add_handler(self, message_type, handler):
        if message_type in self._handlers:
            if type(self._handlers[message_type]) != list:
                self._handlers[message_type] = [self._handlers[message_type]]
            self._handlers[message_type].append(handler)
        else:
            self._handlers[message_type] = handler

    """
    Unregister one or all handler(s) for a specific message type
        message_type    Type of a message
        handler         Optional callable to remove 
    """
    def remove_handler(self, message_type, handler=None):
        if message_type in self._handlers:
            if handler is None:
                del self._handlers[message_type]
            else:
                if type(self._handlers[message_type]) == list:
                    self._handlers[message_type].remove(handler)
                elif self._handlers[message_type] == handler:
                    del self._handlers[message_type]

    """
    Proxy to websocket send method
    """
    def send(self, data):
        self.logger.debug(f'Sent {data}')
        return self._wsa.send(data)

    """
    Block the thread and run websocket loop.
    Run it from a thread if you prefer non-blocked main thread.
    """
    def run(self):
        self._wsa.run_forever()

    def close(self):
        self._wsa.close()

    def _on_open(self):
        self.logger.info('Open')
        self._do_auth()

    def _do_auth(self):
        m = ClientMessage()
        nonce = str(int(datetime.utcnow().timestamp() * 1_000_000_000))

        key_hash = hmac.new(
            base64.b64decode(self._api_secret),
            f'stream_access;access_key_id={self._api_key};nonce={nonce};'.encode(),
            digestmod=hashlib.sha512
        )

        m.apiAuthentication.token = base64.b64encode(key_hash.digest())
        m.apiAuthentication.nonce = nonce
        m.apiAuthentication.api_key = self._api_key

        self.send(m.SerializeToString())

    def _on_message(self, data):
        self.logger.debug(f'Received {data}')

        if len(data) == 1 and data == b'\x01':
            return

        m = StreamMessage()

        m.ParseFromString(data)
        m_type = m.ListFields()[0][0].name
        message = getattr(m, m.ListFields()[0][0].name)

        if m_type in self._handlers:
            if type(self._handlers[m_type]) == list:
                for handler in self._handlers[m_type]:
                    if callable(handler):
                        try:
                            handler(self, message)
                        except Exception as e:
                            self.logger.error(f'{type(e)} while calling handler for {m_type}: {e}')
                    else:
                        self.logger.warning(f'Handler for {m_type} is not callable')
            elif callable(self._handlers[m_type]):
                try:
                    self._handlers[m_type](self, message)
                except Exception as e:
                    self.logger.error(f'{type(e)} while calling handler for {m_type}: {e}')
            else:
                self.logger.warning(f'Handler for {m_type} must be callable or list of callable objects, got {type(self._handlers[m_type])}')
        else:
            self.logger.warning(f'No handler for {m_type}')

    def _on_close(self):
        self.logger.info('Connection closed')

    def _on_error(self, error):
        if type(error) == KeyboardInterrupt:
            return

        self.logger.error(f'Error: {type(error)} {error}')
