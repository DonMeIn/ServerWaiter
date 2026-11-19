from fastapi import APIRouter,Response,Request
import schemas.userTypes as types
import services.user_services as services
from starlette.responses import JSONResponse
router=APIRouter(prefix="/users",tags=["user"])

@router.post("/reg")
async def Registration(user:types.newAdminType):
        newuser={**user.model_dump(exclude_none=True),"accessLevel":3}
        return await services.registration_srv(newuser)
        #else:
         #   return JSONResponse(status_code=401, content={"detail": "no available access"}) 
      
@router.post("/adduser")
async def addUser(user:types.newUserType,request:Request):
        if await services.check_user_access_srv(request.state.user["name"]):
        
            newuser={**user.model_dump(exclude_none=True)}
            return await services.add_user_srv(newuser)
        else:
            return JSONResponse(status_code=401, content={"detail": "no available access"}) 
                
    
@router.post("/login")
async def Log_In(user:types.LoginType,response:Response):
   logInProgress=await services.log_in_srv(user)
   match logInProgress["success"]:
       case True :
            response.set_cookie(
            key="access_token",
            value=logInProgress["token"],
            httponly=True,     # Защита от кражи через JavaScript (XSS)
            secure=False,       # Работает только по HTTPS (для localhost можно False, но в продакшене True)
            samesite="lax",    # Защита от CSRF-атак. Если фронт и бэк на разных доменах, может потребоваться "none"
            max_age=3600,      # Время жизни куки в секундах (1 час)
            )
            return {"success":True,"username":user.name}
       case False:
           return logInProgress


@router.post("/emailConfirm")
async def Confirm_Email(confirmation:types.ConfirmationType):
    return await services.confirm_email_srv(confirmation)
 
