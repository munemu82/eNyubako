from fastapi import Depends, HTTPException
from database.models import Customer, Project, TokenTable
from db import get_db, Base, engine, SessionLocal
from sqlalchemy.orm import Session
from database.schemas import CustomerCreate, ProjectCreate


class ProjectService:
    def get_all_projects(db: Session, skip: int = 0, limit: int = 100):
       # return db.query(Customer).all()
        return db.query(Project).offset(skip).limit(limit).all()

    def get_project_by_customer(cust_id: str, db: Session = Depends(get_db)):
        return db.query(Project).filter(Project.owner_id == cust_id).all()

   
    def update_project(customerid: int, projectid: int, project: ProjectCreate, db: Session):
        # Find the customer record in the database
        db_project = db.query(Project).filter(
             Customer.id == customerid, Project.id ==projectid).first()

        db_project.name = project.name
        db_project.startDate = project.startDate
        db_project.endDate = project.endDate
        db_project.budget = project.budget
        db_project.status_id = project.status_id

        db.commit()

        return db_project

