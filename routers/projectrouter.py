from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from database.models import Project
from database.schemas import ProjectCreate
from services.projectservice import ProjectService

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/")
def getAllProjects(db: Session = Depends(get_db)):
    return ProjectService.get_all_projects(db=db)

@router.get("/{customerid}")
def getCustomerProjects(customerid: int, db: Session = Depends(get_db)):
    return ProjectService.get_project_by_customer(customerid=customerid, db=db)



""" @router.put("/{projectid}/{customerid}")
def updateProject(projectid: int, customerid: int, project: ProjectCreate, db: Session = Depends(get_db)):
    return ProjectService.update_project(customerid=customerid,projectid=projectid, project=project, db=db) """

