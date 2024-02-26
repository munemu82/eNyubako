from database import schemas
import database.models as models
import uvicorn
import jwt
from datetime import datetime 
from database.models import User,TokenTable
from db import get_db, Base, engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from auth_bearer import JWTBearer
from functools import wraps
from utils import create_access_token,create_refresh_token,verify_password,get_hashed_password
from dotenv import load_dotenv
import os

# LOAD ENVIRONMENT VARIABLES
load_dotenv(".env")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# ROUTERS IMPORTS
from routers import customerrouter, userrouter, projectrouter, statusrouter


app = FastAPI(title="E-Nyumbako APIs",
    description="A FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

models.Base.metadata.create_all(bind=engine)

# APP ROUTES
app.include_router(userrouter.router, prefix="")
app.include_router(customerrouter.router, prefix="")
app.include_router(projectrouter.router, prefix="")
app.include_router(statusrouter.router, prefix="")

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    
        payload = jwt.decode(kwargs['dependencies'], JWT_SECRET_KEY, ALGORITHM)
        user_id = payload['sub']
        data= kwargs['session'].query(models.TokenTable).filter_by(user_id=user_id,access_toke=kwargs['dependencies'],status=True).first()
        if data:
            return func(kwargs['dependencies'],kwargs['session'])
        
        else:
            return {'msg': "Token blocked"}
        
    return wrapper

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)

