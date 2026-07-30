from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "OBE PLO Attainment"
    database_url: str = "sqlite:///./obe_plo.db"
    secret_key: str = "change-this-secret-key"
    upload_dir: str = "uploads"
    export_dir: str = "exports"


settings = Settings()
