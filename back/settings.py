import pathlib
from distutils.util import strtobool

import environ
from pydantic_settings import BaseSettings

BASE_DIR = pathlib.Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env('DEBUG', cast=strtobool, default=False)


settings = Settings()



