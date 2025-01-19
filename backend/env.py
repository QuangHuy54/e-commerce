from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv(".env")


class Env(BaseModel):
    APP_ENV: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int
    OPENAI_API_KEY: str


env = Env.model_validate(os.environ)
print("#####", env)
