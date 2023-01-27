import os

from pydantic import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
    POSTGRES_SERVER = os.environ['POSTGRES_SERVER']
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_DB = os.environ['POSTGRES_DB']

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    JWT_SECRET = os.environ['JWT_SECRET']
    JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
    JWT_EXPIRES_S = os.environ['JWT_EXPIRES_S']


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
