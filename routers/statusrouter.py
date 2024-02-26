from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from database.models import Status
from database.schemas import StatusCreate
from services.statusservice import StatusService

router = APIRouter(prefix="/statuses", tags=["Statuses"])


@router.get("/")
def getAllStatuses(db: Session = Depends(get_db)):
    return StatusService.get_all_statuses(db=db)


@router.post("/")
def createStatus(status: StatusCreate, db: Session = Depends(get_db)):
    return StatusService.create_status(status, db)


@router.put("/{statusid}")
def updateStatus(statusid: int, status: StatusCreate, db: Session = Depends(get_db)):
    return StatusService.update_status(statusid=statusid, status=status, db=db)


@router.delete("/{statusid}")
def deleteStatus(statusid: int, db: Session = Depends(get_db)):
    return StatusService.deleteStatus(statusid=statusid, db=db)

