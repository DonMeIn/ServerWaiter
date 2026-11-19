from pwdlib import PasswordHash
from datetime import datetime
import uuid 
import repositories.user_reps as reps
import utils.JwtServices as JWT
import utils.EmailServices as email

passwordHash=PasswordHash.recommended()
date=lambda:datetime.now().strftime("%d.%m.%Y %H:%M:%S")
new_uuid=uuid.uuid4()
def verify_pass_srv(password:str,hash:str):
    is_valid=passwordHash.verify(password,hash)
    return is_valid

async def registration_srv(user):
    value=user.get("email")
    code=str(new_uuid)
    newUser={
            "name":user["name"],
            "password":passwordHash.hash(user["password"]),
            "email":user["email"],
            "accessLevel":3,
            "emailIsConfirmed":False,
            "confirmationCode":code,
            "date":date()
        }
    if await email.send_mail(user["email"],code):
        return await reps.add_user_reps(newUser)
    else:
            return {"success":False,"msg":"error with sending email"}
 
async def add_user_srv(user,):
     
     newUser={
                "name":user["name"],
                "password":passwordHash.hash(user["password"]),
                "accessLevel":(user["accessLevel"] if user["accessLevel"] else 1),
                "date":date()
            }
     return await reps.add_user_reps(newUser)
     
async def log_in_srv(user):
    userInfo=await reps.find_by_name_reps(user.name)
    match userInfo:
        case None:
            return {"success":False,"msg":"wrong name or pass"}
        case False:
            return {"success":False,"msg":"internal error with DB"}
        case _:
             if verify_pass_srv(user.password,userInfo.password):
                 match userInfo.emailIsConfirmed:
                     case False:
                         return {"success":False,"username":userInfo.name,"msg":"Please confirm email"}
                     case _:
                         tokenInfo= await JWT.create_token(userInfo.name)
                         if tokenInfo["success"]:
                            return {"success":True,"username":userInfo.name,"token":tokenInfo["token"]}
                         else:
                             return tokenInfo
             else: return {"success":False,"msg":"wrong name or pass"}

async def check_user_access_srv(user:str):
     userInfo=await reps.find_by_name_reps(user)
     if userInfo:
         if userInfo.accessLevel==3:
             return True
         return False
     return False

async def confirm_email_srv(confirmation):
    return await reps.ConfirmEmail(confirmation)

