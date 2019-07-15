import sys
sys.path.append(".")

from cws_client import WebsocketClient
from client.client_pb2 import ClientMessage


def subscribe(c, message):
    # if authenticated
    if message.status == 1:
        c.logger.info('Authenticated')

        # we'll subscribe to spread updates in this example
        # use * instead of market ID to subscribe to all markets
        msg = ClientMessage()

        # subscribe to bitfinex:ltc-usd spread updates
        s1 = msg.subscribe.subscriptions.add()
        s1.stream_subscription.resource = 'markets:2:book:spread'

        # subscribe to kraken:btc-usd spread updates
        s2 = msg.subscribe.subscriptions.add()
        s2.stream_subscription.resource = 'markets:87:book:spread'

        # send subscription message subscribing to spread updates
        c.send(msg.SerializeToString())


def market_update(c, m):
    c.logger.info(
        f'MarketID: {m.market.marketId}; '
        f'Spread: {m.orderBookSpreadUpdate.bid.priceStr} - {m.orderBookSpreadUpdate.ask.priceStr}'
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

    example_client.run()
