import schemas.userTypes as types

async def add_user_reps(user):
    match await find_by_name_reps(user["name"]):
        case None:
            if user.get("email"):
                match await find_by_email_reps(user["email"]):
                    case None:
                        return await insertInDB_reps(user)
                    case False:
                        return {"success":False,"error":"Internal error with DB"}
                    case _:
                        return {"success":False,"email":"this email is already exist"}
            else :
                return await insertInDB_reps(user)
        case False:
            return {"success":False,"error":"Internal error with DB"}
        case _:
            return {"success":False,"email":"this name is already exist"}
                
                        
    # if await find_by_name(user["name"]):
    #     return {"success":False,"name":"this name is already exist"}
    # elif user.get("email") and await find_by_email(user["email"]):
    #     return {"success":False,"email":"this mail is already exist"}
    # else:
    #     newUser=types.UserSchema.model_validate(user)
    #     try:
    #         await newUser.insert()
    #         return {"success":True,"username":newUser.name}
    #     except :
    #         # Сюда код попадет, если запись в MongoDB сорвалась
    #         return {"success":False,"error":"Internal error"}
    #         # Здесь можно сделать raise HTTPException(...)

async def ConfirmEmail(Confirmation): 
    user= await find_by_name_reps(Confirmation.name)
    match user:
        case False:
            return {"success":False,"msg":"Internal error with DB "}
        case None:
            return {"success":False,"msg":"wrong username or code"}
        case _:
            if user.confirmationCode==Confirmation.code and user.emailIsConfirmed==False:
                user.emailIsConfirmed=True
                try:
                    await user.save()
                    return {"success":True}
                except:
                    return {"success":False,"msg":"Internal error with DB "}
            elif user.emailIsConfirmed==True:
                return {"success":False,"msg":"Email is already confirmed "}
            else:
                return {"success":False,"msg":"wrong username or code"}


async def insertInDB_reps(user):
    newUser=types.UserSchema.model_validate(user)
    try:
        await newUser.insert()
        return {"success":True,"username":newUser.name}
    except :
        # Сюда код попадет, если запись в MongoDB сорвалась
        return {"success":False,"error":"Internal error with DB"}
        # Здесь можно сделать raise HTTPException(...)

async def find_by_name_reps(name:str):
    try:
        user=await types.UserSchema.find_one(types.UserSchema.name==name)
        return user
    except:
         return False

async def find_by_email_reps(email:str):
     try:
         user=await types.UserSchema.find_one(types.UserSchema.email==email)
         return user
     except:
        return False