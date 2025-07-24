from pywa_async import WhatsApp

from src.core import get_wa_client


def get_async_wa_client() -> WhatsApp:
    """
    Returns the WhatsApp client instance.

    This function retrieves the WhatsApp client from the async_wa settings.

    Returns:
        The WhatsApp client instance.
    """
    return get_wa_client()
