from pywa_async import WhatsApp
from pywa_async.types.sent_message import SentMessage
from pywa_async.types.template import Template


class TemplateMessageService:
    """
    Service for handling template messages in WhatsApp.

    Methods:
        send_template_message
    """

    def __init__(self, wa: WhatsApp):
        self.wa = wa

    async def send_template_message(
        self, to: str, template: Template
    ) -> SentMessage:
        return await self.wa.send_template(to=to, template=template)
