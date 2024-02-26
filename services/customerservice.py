from fastapi import Depends, HTTPException
from database.models import Customer,TokenTable,Project
from db import get_db, Base, engine, SessionLocal
from sqlalchemy.orm import Session
from database.schemas import CustomerCreate, ProjectCreate


class CustomerService:
    def get_all_customers(db: Session, skip: int = 0, limit: int = 100):
       # return db.query(Customer).all()
        return db.query(Customer).offset(skip).limit(limit).all()

    def get_customer_by_email(email: str, db: Session = Depends(get_db)):
        return db.query(Customer).filter(Customer.email == email).first()

    def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
        # Check if Customer already exists
        existing_customer = db.query(Customer).filter_by(email=customer.email).first()

        if existing_customer:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        new_customer = Customer(firstName=customer.firstName, lastName = customer.lastName, email=customer.email, 
                                phone=customer.phone )
       
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

        return new_customer

    def update_customer(customerid: int, customer: CustomerCreate, db: Session):
        # Find the customer record in the database
        db_customerid = db.query(Customer).filter(Customer.id == customerid).first()

        db_customerid.firstName = customer.firstName
        db_customerid.lastName = customer.lastName
        db_customerid.email = customer.email
        db_customerid.phone = customer.phone
        db_customerid.address = customer.address

        db.commit()

        return db_customerid
    

    def deleteCustomer(customerid: int, db: Session):
         # Find the customer record in the database
        db_customerid = db.query(Customer).filter(Customer.id == customerid).first()

        db.delete(db)

        db.commit()

        return db_customerid

    def create_customer_project(db: Session, project: ProjectCreate):
        db_project= Project(**project.dict())
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
