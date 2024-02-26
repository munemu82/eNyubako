from fastapi import Depends, HTTPException
from database.models import Customer, Project, TokenTable, Status
from db import get_db, Base, engine, SessionLocal
from sqlalchemy.orm import Session
from database.schemas import  StatusCreate


class StatusService:
    def get_all_statuses(db: Session, skip: int = 0, limit: int = 100):
       # return db.query(Customer).all()
        return db.query(Status).offset(skip).limit(limit).all()

    def get_status_by_id(status_id: int, db: Session = Depends(get_db)):
        return db.query(Status).filter(Status.id == status_id).first()

    def create_status(status: StatusCreate, db: Session = Depends(get_db)):
        # Check if Customer already exists
        existing_status= db.query(Status).filter_by(name=status.name).first()

        if existing_status:
            raise HTTPException(status_code=400, detail="Status already registered")
        
        new_status = Status(name=status.name )
       
        db.add(new_status)
        db.commit()
        db.refresh(new_status)

        return new_status
   
    def update_status(status_id: int, status: StatusCreate, db: Session):
        # Find the customer record in the database
        db_status = db.query(Status).filter(Status.id == status_id).first()

        db_status.name = status.name
      

        db.commit()

        return db_status
    
    def deleteStatus(status_id: int, db: Session):
         # Find the customer record in the database
        db_statusId = db.query(Status).filter(Status.id == status_id).first()

        db.delete(db_statusId)

        db.commit()

        return db_statusId


