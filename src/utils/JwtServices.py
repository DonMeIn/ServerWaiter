import jwt
from datetime import datetime, timedelta, timezone
SECRET_KEY = "secret-key-ne-one-is"
ALGORITHM = "HS256"

async def create_token(username:str)->dict:
    try:
        payload={
        "name": username,                                    # Имя (из репозитория)
        "exp": datetime.now(timezone.utc) + timedelta(hours=1), # Время жизни токена
        "iat": datetime.now(timezone.utc)  
        }
        jwt_token=jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"success":True,"token":jwt_token}
    except:
        return {"success":False,"msg":"authorization error"}
async def verify_token(token: str) -> dict:
    try:
        # Декодируем токен. На выходе получаем DICT!
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"success":True,"payload":decoded_payload}
        
    except jwt.ExpiredSignatureError:
        return {"success":False,"payload":None,"msg":"authorization error"}
    except jwt.InvalidTokenError:
        return {"success":False,"payload":None,"msg":"authorization error"}
