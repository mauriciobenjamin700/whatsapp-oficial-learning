from fastapi import FastAPI
from pywa_async import WhatsApp

from src.core.settings import settings

wa: WhatsApp = None


def create_wa_client(app: FastAPI) -> WhatsApp:
    """Cria e configura o cliente WhatsApp"""
    global wa

    wa = WhatsApp(
        phone_id=settings.PHONE_NUMBER_ID,
        token=settings.ACCESS_TOKEN,
        server=app,  # Passa a instância do FastAPI
        callback_url=settings.CALLBACK_URL,
        verify_token=settings.VERIFY_TOKEN,
        app_id=settings.APP_ID,
        app_secret=settings.APP_SECRET,
    )

    return wa


def get_wa_client() -> WhatsApp:
    """Retorna a instância do cliente WhatsApp"""
    return wa
