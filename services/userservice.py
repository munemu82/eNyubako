from fastapi import Depends, HTTPException, status
from database.models import User,TokenTable,Project
from db import get_db, Base, engine, SessionLocal
from sqlalchemy.orm import Session
from database.schemas import UserCreate, ProjectCreate, RequestDetails, ChangePassword
from utils import create_access_token,create_refresh_token,verify_password,get_hashed_password
from auth_bearer import JWTBearer
from datetime import datetime 
import jwt
from dotenv import load_dotenv
import os
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

load_dotenv(".env")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class UserService:
    def getUsers( dependencies=Depends(JWTBearer()),session: Session = Depends(get_db), skip: int = 0, limit: int = 100):
        return session.query(User).offset(skip).limit(limit).all()
    
    def register_user(user: UserCreate, session: Session = Depends(get_db)):
        existing_user = session.query(User).filter_by(email=user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        encrypted_password =get_hashed_password(user.password)

        new_user = User(username=user.username, email=user.email, password=encrypted_password )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        json_compatible_item_data = jsonable_encoder(new_user)
        #return {"message":"user created successfully"}
        return JSONResponse(content=json_compatible_item_data)

    def login(request: RequestDetails, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == request.email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
        hashed_pass = user.password
        if not verify_password(request.password, hashed_pass):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect password"
            )
        
        access=create_access_token(user.id)
        refresh = create_refresh_token(user.id)

        token_db = TokenTable(user_id=user.id,  access_toke=access,  refresh_toke=refresh, status=True)
        db.add(token_db)
        db.commit()
        db.refresh(token_db)
        return {
            "access_token": access,
            "refresh_token": refresh,
        }
    

    def change_password(request: ChangePassword, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == request.email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
        
        if not verify_password(request.old_password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid old password")
        
        encrypted_password = get_hashed_password(request.new_password)
        user.password = encrypted_password
        db.commit()
        
        return {"message": "Password changed successfully"}
    
    
    def logout(dependencies=Depends(JWTBearer()), db: Session = Depends(get_db)):
        token=dependencies
        payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
        user_id = payload['sub']
        token_record = db.query(TokenTable).all()
        info=[]
        for record in token_record :
            print("record",record)
            if (datetime.utcnow() - record.created_date).days >1:
                info.append(record.user_id)
        if info:
            existing_token = db.query(TokenTable).where(TokenTable.user_id.in_(info)).delete()
            db.commit()
            
        existing_token = db.query(TokenTable).filter(TokenTable.user_id == user_id, TokenTable.access_toke==token).first()
        if existing_token:
            existing_token.status=False
            db.add(existing_token)
            db.commit()
            db.refresh(existing_token)
        return {"message":"Logout Successfully"} 
