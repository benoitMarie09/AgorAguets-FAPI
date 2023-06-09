from pydantic import BaseSettings


class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str

    class Config:
        env_file = ".env"

