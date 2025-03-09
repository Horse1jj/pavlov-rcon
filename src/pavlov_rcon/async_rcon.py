import asyncio

class AsyncPavlovRCON:
    def __init__(self, ip: str, port: int, password: str):
        self.ip = ip
        self.port = port
        self.password = password
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.ip, self.port)
        await self.send_command(self.password)  # Authenticate

    async def send_command(self, command: str) -> str:
        if not self.writer:
            raise ConnectionError("Not connected to the server.")
        self.writer.write(command.encode("utf-8") + b"\n")
        await self.writer.drain()
        response = await self.reader.read(4096)
        return response.decode("utf-8")

    async def disconnect(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
