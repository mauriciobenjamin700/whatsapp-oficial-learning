from pydantic_settings import BaseSettings, SettingsConfigDict
from pywa_async import WhatsApp


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8',
        extra="ignore",
        case_sensitive=True
    )

    ACCESS_TOKEN: str = ""
    PHONE_NUMBER_ID: str = ""
    BUSINESS_ACCOUNT_ID: str = ""
    WABA_ID: str = ""
    VERSION: str = "v22.0"
    TO: str = ""

settings = Settings()

async_wa: WhatsApp = WhatsApp(
    phone_id=settings.PHONE_NUMBER_ID,
    token=settings.ACCESS_TOKEN,
)