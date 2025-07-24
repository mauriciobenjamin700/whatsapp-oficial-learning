from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pywa_async import WhatsApp, types

from src.api.routes import message_router
from src.core import create_wa_client

app = FastAPI(
    title="WhatsApp Oficial Learning API",
    description="API for WhatsApp Oficial Learning",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wa = create_wa_client(app)


@wa.on_message
async def hello(_: WhatsApp, msg: types.Message):
    try:
        await msg.react("👋")
        await msg.reply("Recebido")
    except Exception as e:
        print(f"Erro ao responder mensagem: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


app.include_router(message_router)
