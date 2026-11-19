from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.types import ASGIApp
from utils.JwtServices import verify_token

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    async def dispatch(self,request:Request,call_next):
        if True or request.url.path.endswith(("/reg","/login","/dish","/tables"))or request.url.path.startswith(("/reg","/login","/dish","/tables","/docs")):
                    return await call_next(request)
        #True or zaglushka
        token=request.cookies.get("access_token")
        if not token:
            return JSONResponse(status_code=401, content={"detail": "Missing or invalid credentials"}) 
        
        try:
            payload=await verify_token(token)
            if payload["success"]==True:
                request.state.user = payload["payload"]  
                response=await call_next(request)
                return response
            else :
                return JSONResponse(status_code=401, content={"detail": "Missing or invalid credentials"}) 
        except :
            return JSONResponse(status_code=401, content={"detail": "something goes wrong"}) 
