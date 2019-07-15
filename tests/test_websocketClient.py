from unittest import TestCase
from client import WebsocketClient


class TestWebsocketClient(TestCase):
    def setUp(self):
        self.client = WebsocketClient('abc', 'cba')

    def test_add_handler(self):
        def message1_1(x):
            ...

        def message1_2(x):
            ...

        def message2_1(x):
            ...

        def message2_2(x):
            ...

        self.assertEquals(self.client._handlers, {})
        self.client.add_handler('message_1', message1_1)
        self.assertEquals(self.client._handlers, {'message_1': message1_1})
        self.client.add_handler('message_1', message1_2)
        self.assertEquals(self.client._handlers, {'message_1': [message1_1, message1_2]})
        self.client.add_handler('message_2', message2_1)
        self.assertEquals(self.client._handlers, {'message_1': [message1_1, message1_2], 'message_2': message2_1})
        self.client.add_handler('message_2', message2_2)
        self.assertEquals(self.client._handlers, {'message_1': [message1_1, message1_2], 'message_2': [message2_1, message2_2]})

    def test_remove_handler(self):
        def message1_1(x):
            ...

        def message1_2(x):
            ...

        self.assertEquals(self.client._handlers, {})
        self.client.add_handler('message_1', message1_1)
        self.assertEquals(self.client._handlers, {'message_1': message1_1})
        self.client.remove_handler('message_1', message1_2)
        self.assertEquals(self.client._handlers, {'message_1': message1_1})
        self.client.remove_handler('message_1', message1_1)
        self.assertEquals(self.client._handlers, {})

        self.client.add_handler('message_1', message1_1)
        self.client.add_handler('message_1', message1_2)
        self.client.remove_handler('message_1', message1_1)
        self.assertEquals(self.client._handlers, {'message_1': [message1_2]})

        self.client.remove_handler('message_2')
        self.assertEquals(self.client._handlers, {'message_1': [message1_2]})

        self.client.remove_handler('message_1')
        self.assertEquals(self.client._handlers, {})

    def test_send(self):
        self.fail()

    def test_run(self):
        self.fail()
