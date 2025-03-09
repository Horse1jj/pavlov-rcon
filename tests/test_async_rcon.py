import pytest
import asyncio
from pavlov_rcon.async_rcon import PavlovRCON

@pytest.mark.asyncio
async def test_async_rcon():
    rcon = PavlovRCON("127.0.0.1", 7777, "password")
    assert rcon.ip == "127.0.0.1"