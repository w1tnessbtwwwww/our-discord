from pydantic import Field
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    token: str = Field(alias="BOT_TOKEN")
    client_id: str = Field(alias="CLIENT_ID")

config: Config = Config()