from pywa_async import WhatsApp

from src.core import async_wa


def get_async_wa_client() -> WhatsApp:
    """
    Returns the WhatsApp client instance.
    
    This function retrieves the WhatsApp client from the async_wa settings.
    
    Returns:
        The WhatsApp client instance.
    """
    return async_wa