from fastapi_mail import FastMail, MessageSchema, MessageType
from app.settings import mail_connection_config
from app.models.email import EmailSchema

async def send(
        email: EmailSchema,
        html: str
    ) -> None:

    message = MessageSchema(
        subject="MyProj password reset",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(mail_connection_config)
    await fm.send_message(message)





