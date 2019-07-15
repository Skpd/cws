# Cryptowatch Websocket client

Simple python client for cryptowat.ch websocket streams.

### Setup

Install required packages in virtual environment

Pull protobuf protocols submodule

Compile protocols

setup.sh script can do it all for you. 

If you prefer to use your own virtual environment - replace path to virtual environment in VENV variable.

If you prefer different python binary - replace it PYTHON_EX variable.


### Example

```python
example_client = WebsocketClient(api_key=api_key, api_secret=api_secret)
example_client.add_handler('authenticationResult', lambda client, message: client.loger.info(message))
example_client.run()
``` 

See example/simple_subscribe.py for details.
