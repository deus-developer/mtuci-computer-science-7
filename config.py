from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_bot_token: str = Field(alias="TELEGRAM_BOT_TOKEN")
    database_url: PostgresDsn = Field(alias="DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
