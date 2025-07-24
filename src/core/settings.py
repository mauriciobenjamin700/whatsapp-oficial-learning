from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

    ACCESS_TOKEN: str = ""
    PHONE_NUMBER_ID: str = ""
    BUSINESS_ACCOUNT_ID: str = ""
    WABA_ID: str = ""
    VERSION: str = "v22.0"
    TO: str = ""
    CALLBACK_URL: str = "https://example.com/callback"
    PORT: int = 8001
    VERIFY_TOKEN: str = "your_verify_token"
    APP_ID: str = "your_app_id"
    APP_SECRET: str = "your_app_secret"


settings = Settings()
