from threading import Thread
from time import sleep
from google.protobuf.json_format import ParseDict, MessageToDict
from cws.cws_client import WebsocketClient
from cws.client.client_pb2 import ClientMessage


def subscribe(c, message):
    # if authenticated
    if message.status == 1:
        c.logger.info('Authenticated')

        # we'll subscribe to spread updates in this example
        # use * instead of market ID to subscribe to all markets

        # subscribe to bitfinex:ltc-usd and kraken:btc-usd spread updates
        msg_data = {
            'subscribe': {
                'subscriptions': [
                    {'streamSubscription': {'resource': 'markets:2:book:spread'}},
                    {'streamSubscription': {'resource': 'markets:87:book:spread'}},
                ]
            }
        }

        # build msg from dict if it looks easier
        # see simple_subscribe for example on how to build message manually
        msg = ParseDict(msg_data, ClientMessage())

        # send subscription message subscribing to spread updates
        c.send(msg.SerializeToString())
    else:
        c.logger.warning(message)


def market_update(c, m):
    # convert to dict if it is easier to use
    msg_data = MessageToDict(m)

    order_book = msg_data['orderBookSpreadUpdate']
    c.logger.info(
        f"MarketID: {msg_data['market']['marketId']}; "
        f"Spread: {order_book['bid']['priceStr']} - {order_book['ask']['priceStr']}"
    )


if __name__ == '__main__':
    # REPLACE IT WITH YOUR API KEYS WHEN/IF ENFORCED
    api_key = 'xxxxxxxxxxxxxxxxxxxx'
    api_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # -----------------------------

    example_client = WebsocketClient(api_key=api_key, api_secret=api_secret)

    # adding message handler to subscribe to market updates once authenticated
    example_client.add_handler('authenticationResult', subscribe)

    # adding handler to show market updates
    example_client.add_handler('marketUpdate', market_update)

    # misc handlers to improve visibility
    example_client.add_handler('subscriptionResult', lambda a, b: a.logger.info(f'Subscribed to {b.status.keys}'))
    example_client.add_handler('bandwidthUpdate', lambda a, b: a.logger.info(f'Bandwidth Update: {b}'))

    c_thread = Thread(target=example_client.run, daemon=True)
    c_thread.start()

    while c_thread.is_alive():
        try:
            # do something else
            sleep(.001)
        except KeyboardInterrupt:
            example_client.close()
            c_thread.join()

    print('done')
