from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
# from pydantic import EmailStr

from src.auth_services import auth_service

# from src.conf.config import settings

# import os


# conf = ConnectionConfig(
#     MAIL_USERNAME=settings.mail_username,
#     MAIL_PASSWORD=settings.mail_password,
#     MAIL_FROM=EmailStr(settings.mail_from),
#     MAIL_PORT=settings.mail_port,
#     MAIL_SERVER=settings.mail_server,
#     MAIL_FROM_NAME="Desired Name",
#     MAIL_STARTTLS=False,
#     MAIL_SSL_TLS=True,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True,
#     TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
# )

conf = ConnectionConfig(
    MAIL_USERNAME="hannasagan@meta.ua",
    MAIL_PASSWORD="Hanna-0714!",
    MAIL_FROM="hannasagan@meta.ua",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.meta.ua",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)

async def send_email(email: str, host: str):
    try:
        token_verification = auth_service.create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email ",
            recipients=[email],
            template_body={"host": host, "email": email,"token": token_verification},
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message, template_name="email_template.html")
    except ConnectionErrors as err:
        print(err)

