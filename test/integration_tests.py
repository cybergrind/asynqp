import asyncio
import asynqp


class WhenConnectingToRabbit:
    def given_the_loop(self):
        self.loop = asyncio.get_event_loop()

    def when_I_connect(self):
        self.connection = self.loop.run_until_complete(asyncio.wait_for(asynqp.connect(), 0.2))

    def it_should_connect(self):
        assert self.connection is not None

    def cleanup_the_connection(self):
        self.connection.close()


class WhenOpeningAChannel:
    def given_a_connection(self):
        self.loop = asyncio.get_event_loop()
        self.connection = self.loop.run_until_complete(asyncio.wait_for(asynqp.connect(), 0.2))

    def when_I_open_a_channel(self):
        self.channel = self.loop.run_until_complete(asyncio.wait_for(self.connection.open_channel(), 0.2))

    def it_should_give_me_the_channel(self):
        assert self.channel is not None

    def cleanup_the_channel_and_connection(self):
        self.loop.run_until_complete(self.close())

    @asyncio.coroutine
    def close(self):
        yield from self.channel.close()
        yield from self.connection.close()
