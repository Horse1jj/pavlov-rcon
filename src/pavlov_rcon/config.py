from pydantic import BaseModel
import json

class Config(BaseModel):
    ip: str
    port: int
    password: str

    @classmethod
    def load(cls, filepath: str):
        with open(filepath, "r") as f:
            data = json.load(f)
        return cls(**data)
