import asyncio


class HelloWorld(AppBase):
    __version__ = "1.0.0"
    app_name = "hello_world"  # this needs to match "name" in api.yaml
    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def add(self,num1,num2):
        return str(num1 + num2)
    async def sub(self, num1, num2):
        return str(num1 - num2)
    async def mul(self,num1,num2):
        return str(num1 * num2)
    async def dev(self,num1,num2):
        return str(num1 / num2)




if __name__ == "__main__":
    asyncio.run(HelloWorld.run(), debug=True)
