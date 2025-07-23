from pywa_async import WhatsApp
from pywa_async.types.message import SentMessage


class ReactionMessageService:
    """
    Service for handling reaction messages in WhatsApp.

    Methods:
        send_reaction_message
        mark_message_as_read
        indicate_typing_message
    """

    def __init__(self, wa: WhatsApp):
        self.wa = wa

    async def send_reaction_message(
        self, to: str, message_id: str, reaction: str
    ) -> SentMessage:
        return await self.wa.send_reaction(
            to=to, emoji=reaction, message_id=message_id
        )

    async def mark_message_as_read(self, message_id: str) -> bool:
        return await self.wa.mark_message_as_read(message_id=message_id)

    async def indicate_typing_message(self, message_id: str) -> bool:
        return await self.wa.indicate_typing(message_id=message_id)
