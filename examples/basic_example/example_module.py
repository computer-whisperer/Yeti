import yeti
import asyncio


class Example(yeti.Module):

    def module_init(self):
        self.add_task(self.say_hi("Hello world!"))
        self.add_task(self.tactfull_hello())

    @asyncio.coroutine
    def tactfull_hello(self):
        yield from yeti.get_event("tick").wait()
        print("... hi?")

    @asyncio.coroutine
    def say_hi(self, message):
        while True:
            print(message)
            yield from asyncio.sleep(1)
