from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    checkpoint_path: str
    folder_path: str
    valid_extensions: tuple = '.txt',

    class Config:
        env_file = ".env"

settings = Settings()
