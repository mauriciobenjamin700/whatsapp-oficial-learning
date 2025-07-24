from typing import Optional

from pywa_async import WhatsApp
from pywa_async.types.message import Contact
from pywa_async.types.sent_message import SentMessage


class MediaMessageService:
    """
    Service for sending various types of media messages using WhatsApp API.

    Methods:
        send_image_message: Sends an image message.
        send_video_message: Sends a video message.
        send_audio_message: Sends an audio message.
        send_document_message: Sends a document message.
        send_location_message: Sends a location message.
        send_contact_message: Sends a contact message.
        send_sticker_message: Sends a sticker message.
        send_catalog_message: Sends a catalog message.
    """

    def __init__(self, wa: WhatsApp):
        self.wa = wa

    async def send_image_message(
        self,
        to: str,
        media_path: str | bytes,
        content_type: Optional[str] = None,
        caption: Optional[str] = None,
    ) -> SentMessage:
        """
        Sends an image message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            media_path (str): The path to the image file.
            caption (str, optional): The caption for the image.
        """
        return await self.wa.send_image(
            to=to, image=media_path, mime_type=content_type, caption=caption
        )

    async def send_video_message(
        self,
        to: str,
        media_path: str | bytes,
        content_type: str = "video/mp4",
        caption: str = None,
    ) -> SentMessage:
        """
        Sends a video message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            media_path (str): The path to the video file.
            caption (str, optional): The caption for the video.

        Returns:
            SentMessage: The sent message object containing
            details of the sent video.
        """
        return await self.wa.send_video(
            to=to, video=media_path, mime_type=content_type, caption=caption
        )

    async def send_audio_message(
        self,
        to: str,
        media_path: str | bytes,
        content_type: Optional[str] = None,
    ) -> SentMessage:
        """
        Sends an audio message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            media_path (str): The path to the audio file.

        Returns:
            SentMessage: The sent message object containing
            details of the sent audio.
        """
        return await self.wa.send_audio(
            to=to, audio=media_path, mime_type=content_type
        )

    async def send_document_message(
        self,
        to: str,
        media_path: str | bytes,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        caption: str = None,
    ) -> SentMessage:
        """
        Sends a document message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            media_path (str): The path to the document file.
            caption (str, optional): The caption for the document.

        Returns:
            SentMessage: The sent message object containing
        """
        return await self.wa.send_document(
            to=to,
            document=media_path,
            filename=filename,
            caption=caption,
            mime_type=content_type,
        )

    async def send_location_message(
        self,
        to: str,
        latitude: float,
        longitude: float,
        name: str = None,
        address: str = None,
    ) -> SentMessage:
        """
        Sends a location message to a specified recipient.
        Args:
            to (str): The recipient's phone number.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            name (str, optional): The name of the location.
            address (str, optional): The address of the location.
        Returns:
            SentMessage: The sent message object containing
        """
        return await self.wa.send_location(
            to=to,
            latitude=latitude,
            longitude=longitude,
            name=name,
            address=address,
        )

    async def send_contact_message(
        self, to: str, contact: Contact
    ) -> SentMessage:
        """
        Sends a contact message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            contact (Contact): The contact object containing
                details of the contact to be sent.
        Returns:
            SentMessage: The sent message object containing
            details of the sent contact.
        """
        return await self.wa.send_contact(to=to, contact=contact)

    async def send_sticker_message(
        self, to: str, sticker_path: str
    ) -> SentMessage:
        """
        Sends a sticker message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            sticker_path (str): The path to the sticker file.
        Returns:
            SentMessage: The sent message object containing
            details of the sent sticker.
        """
        return await self.wa.send_sticker(to=to, sticker=sticker_path)

    async def send_catalog_message(
        self, to: str, body: str, footer: str, thumbnail_product_sku: str
    ) -> SentMessage:
        """
        Sends a catalog message to a specified recipient.

        Args:
            to (str): The recipient's phone number.
            body (str): The body text of the catalog message.
            footer (str): The footer text of the catalog message.
            thumbnail_product_sku (str): The SKU of the product thumbnail.

        Returns:
            SentMessage: The sent message object containing
            details of the sent catalog message.
        """
        return await self.wa.send_catalog(
            to=to,
            body=body,
            footer=footer,
            thumbnail_product_sku=thumbnail_product_sku,
        )
