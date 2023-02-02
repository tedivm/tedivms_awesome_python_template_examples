from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = "bare"
    debug: bool = False
