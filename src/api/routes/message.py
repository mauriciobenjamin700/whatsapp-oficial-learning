from fastapi import APIRouter, Depends, UploadFile
from pywa_async import WhatsApp

from src.api.dependencies import get_async_wa_client
from src.schemas import MessageResponse
from src.services import (
    MediaMessageService,
    ReactionMessageService,
    TextMessageService,
)

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/send/text")
async def send_text_message(
    to: str,
    body: str,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send a text message.
    
    Args:
        to (str): The recipient's phone number.
        body (str): The content of the text message.
    """
    service = TextMessageService(wa)
    result = await service.send_text_message(to, body)
    return MessageResponse.model_validate(result, from_attributes=True)

@router.post("/send/image")
async def send_image_message(
    to: str,
    media_path: UploadFile,
    caption: str = None,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send an image message.
    
    Args:
        to (str): The recipient's phone number.
        media_path (str): The path to the image file.
        caption (str, optional): The caption for the image.
    """
    service = MediaMessageService(wa)

    image = await media_path.read()
    content_type = media_path.content_type

    result = await service.send_image_message(to, image, content_type, caption)
    return MessageResponse.model_validate(result, from_attributes=True)

@router.post("/send/video")
async def send_video_message(
    to: str,
    media_path: UploadFile,
    caption: str = None,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send a video message.
    
    Args:
        to (str): The recipient's phone number.
        media_path (str): The path to the video file.
        caption (str, optional): The caption for the video.
    """
    service = MediaMessageService(wa)

    video = await media_path.read()
    content_type = media_path.content_type
    print(f"Content Type: {content_type}")

    result = await service.send_video_message(to, video, content_type, caption)
    return MessageResponse.model_validate(result, from_attributes=True)

@router.post("/send/audio")
async def send_audio_message(
    to: str,
    media_path: UploadFile,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send an audio message.
    
    Args:
        to (str): The recipient's phone number.
        media_path (str): The path to the audio file.
    """
    service = MediaMessageService(wa)

    audio = await media_path.read()
    content_type = media_path.content_type
    print(f"Content Type: {content_type}")

    result = await service.send_audio_message(to, audio, content_type)
    return MessageResponse.model_validate(result, from_attributes=True)


@router.post("/send/document")
async def send_document_message(
    to: str,
    media_path: UploadFile,
    caption: str = None,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send a document message.
    
    Args:
        to (str): The recipient's phone number.
        media_path (str): The path to the document file.
        caption (str, optional): The caption for the document.
    """
    service = MediaMessageService(wa)

    document = await media_path.read()
    content_type = media_path.content_type
    filename = media_path.filename

    result = await service.send_document_message(
        to, 
        document, 
        filename, 
        content_type, 
        caption
    )
    return MessageResponse.model_validate(result, from_attributes=True)


@router.post("/send/reaction")
async def send_reaction_message(
    to: str,
    message_id: str,
    emoji: str = "👍",
    wa: WhatsApp = Depends(get_async_wa_client)
) -> MessageResponse:
    """
    Endpoint to send a reaction message.
    
    Args:
        to (str): The recipient's phone number.
        message_id (str): The ID of the message to react to.
        emoji (str): The emoji to use for the reaction.
    """
    service = ReactionMessageService(wa)
    result = await service.send_reaction_message(to, message_id, emoji)
    return MessageResponse.model_validate(result, from_attributes=True)


@router.post("/mark-as-read")
async def mark_message_as_read(
    message_id: str,
    wa: WhatsApp = Depends(get_async_wa_client)
) -> bool:
    """
    Endpoint to mark a message as read.
    
    Args:
        message_id (str): The ID of the message to mark as read.
    """
    service = ReactionMessageService(wa)
    return await service.mark_message_as_read(message_id)