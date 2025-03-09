import pytest 
from pavlov_rcon.main import PavlovRCON

def test_sync_rcon():
    rcon = PavlovRCON("127.0.0.1", 7777, "password")
    assert rcon.ip == "127.0.0.1"
    assert rcon.port == 7777