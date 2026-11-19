from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType, NameEmail
from pydantic import BaseModel, EmailStr,SecretStr
from typing import List

# 2. Исправленная конфигурация для Gmail на порту 587 (используем STARTTLS)
conf = ConnectionConfig(
    MAIL_USERNAME="waiter.testing.email@gmail.com",
    MAIL_PASSWORD=SecretStr("rhwu bycu xlpl xnhl"),
    MAIL_FROM="waiter.testing.email@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,  # ДЛЯ ПОРТА 587 ДОЛЖНО БЫТЬ TRUE
    MAIL_SSL_TLS=False,  # ДЛЯ ПОРТА 587 ДОЛЖНО БЫТЬ FALSE
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def send_mail(mail: EmailStr,code:str):  # Исправлен тип аргумента
  # Параметр recipients обязательно должен быть СПИСКОМ строк:
  message = MessageSchema(
      subject="Fastapi-Mail module",
      recipients=[NameEmail(name="",email=mail)],  # Добавлены квадратные скобки [ ]
      body=f"<p>Your code={code}</p>",  # Добавлена пропущенная запятая
      subtype=MessageType.html,
  )

  fm = FastMail(conf)
  try:
        await fm.send_message(message)
        return True
  except:return False