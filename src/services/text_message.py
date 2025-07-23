from pywa_async import WhatsApp
from pywa_async.types.sent_message import SentMessage


class TextMessageService:
    """
    Service for handling text messages in WhatsApp.

    Methods:
        send_text_message
        send_text_message_with_url
        send_reaction_message
    """

    def __init__(self, wa: WhatsApp):
        self.wa = wa

    async def send_text_message(self, to: str, message: str) -> SentMessage:
        self.__validate_message(message)
        return await self.wa.send_text(to=to, text=message)

    async def send_text_message_with_url(
        self,
        to: str,
        message: str,
    ) -> SentMessage:
        self.__validate_message(message)
        return await self.wa.send_text(to=to, text=message, preview_url=True)

    async def send_reaction_message(
        self, to: str, message_id: str, reaction: str
    ) -> SentMessage:
        return await self.wa.send_reaction(
            to=to, emoji=reaction, message_id=message_id
        )

    def __validate_message(self, message: str) -> None:
        if not message:
            raise ValueError("Message cannot be empty")
        if len(message) > 4096:
            raise ValueError(
                "Message exceeds maximum length of 4096 characters"
            )
