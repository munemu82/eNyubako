from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from database.models import Customer
from database.schemas import CustomerCreate, ProjectCreate
from services.customerservice import CustomerService

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/")
def getAllCustomers(db: Session = Depends(get_db)):
    return CustomerService.get_all_customers(db=db)


@router.post("/")
def createCustomer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer(customer, db)


@router.put("/{customerid}")
def updateCustomer(customerid: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.update_customer(customerid=customerid, customer=customer, db=db)


@router.delete("/{customerid}")
def deleteCustomer(customerid: int, db: Session = Depends(get_db)):
    return CustomerService.deleteCustomer(customerid=customerid, db=db)

@router.post("/projects")
def createCustomerProject(project: ProjectCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer_project(project=project, db=db)

