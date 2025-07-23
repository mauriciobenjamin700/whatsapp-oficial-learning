from pywa import WhatsApp

from core.settings import settings


wa = WhatsApp(
    phone_id=settings.PHONE_NUMBER_ID,
    token=settings.ACCESS_TOKEN,
)

TO = settings.TO

result = wa.send_message(
    to=TO,
    text='Hi! This message sent from pywa!'
)

print(result)