from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from database.models import User
from database.schemas import UserCreate, ChangePassword
from services.userservice import UserService
from auth_bearer import JWTBearer

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def getAllUser(db: Session = Depends(get_db)):
    return UserService.getUsers(db=db)

@router.post("/register")
def register_user(user: UserCreate, db: Session  = Depends(get_db)):
    return UserService.register_user(user, db)

@router.post("/login")
def login(user: UserCreate, db: Session  = Depends(get_db)):
    return UserService.login(user, db)

@router.post("/change-password")
def change_password(request: ChangePassword, db: Session  = Depends(get_db)):
    return UserService.change_password(request, db)

@router.post("/logout")
def logout(dependencies=Depends(JWTBearer()), db: Session  = Depends(get_db)):
    return UserService.logout(dependencies, db)

