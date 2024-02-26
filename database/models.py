from sqlalchemy import (
    LargeBinary, 
    Column, 
    String, 
    Integer,
    DateTime,
    Boolean, 
    UniqueConstraint,
    ForeignKey, 
    PrimaryKeyConstraint,
    Float
)
from sqlalchemy.orm import relationship

import datetime

from db import Base
    
class User(Base):
    """Models a user table"""
    __tablename__ = "users"
    email = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    password = Column(String, nullable=False)
    username = Column(String(225), nullable=False)
    is_active = Column(Boolean, default=True)


class TokenTable(Base):
    __tablename__ = "token"
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    firstName = Column(String(50), index=True)
    lastName = Column(String(50), index=True)
    email = Column(String(50), index=True)
    phone = Column(String(15), index=True)
    address = Column(String(100), nullable=True)
    projects = relationship("Project", back_populates="owner")

class Project(Base):
     __tablename__ = "projects"
     id = Column(Integer, nullable=False, primary_key=True)
     name = Column(String(100), nullable=False)
     startDate = Column(DateTime, nullable=True)
     endDate = Column(DateTime, nullable=True)
     budget = Column(Float, default=0.00)
     status_id = Column(Integer, ForeignKey("statuses.id"))
     owner_id = Column(Integer, ForeignKey("customers.id"))

     owner = relationship("Customer", back_populates="projects")
    # tasks = relationship("Task", back_populates="project_task")
    # equipments = relationship("ProjectEquipment", back_populates="Project")
     # materials = relationship("ProjectMaterial", back_populates="project")
     status = relationship("Status", back_populates="projects")
     tasks = relationship("Task", back_populates="project_task")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    taskName = Column(String(100),  nullable=False)
    description = Column(String(250), nullable=True)
    startDate = Column(DateTime, nullable=True)
    endDate = Column(DateTime, nullable=True)
    status_id = Column(Integer, ForeignKey("statuses.id"))
    price = Column(Float, default=0.00)
    project_task_id = Column(Integer, ForeignKey("projects.id"))

    #project_task_id= Column(Integer, ForeignKey("Projects.id"))

    #project_task = relationship("Project", back_populates="tasks")
    #equipments = relationship("TaskEquipment", back_populates="task")
    #materials = relationship("TaskMaterial", back_populates="task")
    status = relationship("Status", back_populates="tasks")
    project_task = relationship("Project", back_populates="tasks")
    equipments = relationship("Equipment", back_populates="task_equipment")
    materials = relationship("Material", back_populates="task_material")

class Equipment(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True)
    equipmentName = Column(String(100),  nullable=False)
    item_type_id = Column(Integer, ForeignKey("item_types.id"))
    image_url =  Column(String(100),  nullable=True)
    price = Column(Float, default=0.00)
    task_equipment_id = Column(Integer, ForeignKey("tasks.id"))

    #projects = relationship("ProjectEquipment", back_populates="equipment")
    #tasks = relationship("TaskEquipment", back_populates="equipment")
    item_type = relationship("ItemType", back_populates="equipments")
    task_equipment = relationship("Task", back_populates="equipments")

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    materialName = Column(String(100),  nullable=False)
    item_type_id = Column(Integer, ForeignKey("item_types.id"))
    image_url =  Column(String(100),  nullable=True)
    price = Column(Float, default=0.00)
    task_material_id = Column(Integer, ForeignKey("tasks.id"))

    #projects = relationship("ProjectMaterial", back_populates="material")
    #tasks = relationship("TaskMaterial", back_populates="material")
    item_type = relationship("ItemType", back_populates="materials")
    task_material = relationship("Task", back_populates="materials")


""" class ProjectEquipment(Base):     # Intermediate table to form many-to-many relationship between project and equipment
    __tablename__ = "Project_equipments"

    project_id = Column(ForeignKey('Projects.id'), primary_key=True)
    equipment_id = Column(ForeignKey('Equipments.id'), primary_key=True)
    quantity = Column(Integer, default=0.00)
    unit_price = Column(Float, default=0.00)

    project = relationship("Project", back_populates="project_equipments")
    equipment = relationship("Equipment", back_populates="project_equipments") """

""" class TaskEquipment(Base):     # Intermediate table to form many-to-many relationship between task and equipment
    __tablename__ = "Task_equipments"

    task_id = Column(ForeignKey('Tasks.id'), primary_key=True)
    equipment_id = Column(ForeignKey('Equipments.id'), primary_key=True)
    quantity = Column(Integer, default=0.00)
    unit_price = Column(Float, default=0.00)

    task = relationship("Task", back_populates="Task_equipments")
    equipment = relationship("Equipment", back_populates="Task_equipments") """


""" class ProjectMaterial(Base):     # Intermediate table to form many-to-many relationship between project and equipment
    __tablename__ = "Project_materials"

    project_id = Column(ForeignKey('Projects.id'), primary_key=True)
    material_id = Column(ForeignKey('Materials.id'), primary_key=True)
    quantity = Column(Integer, default=0.00)
    unit_price = Column(Float, default=0.00)

    project = relationship("Project", back_populates="materials")
    material = relationship("Material", back_populates="materials") """


""" class TaskMaterial(Base):     # Intermediate table to form many-to-many relationship between project and equipment
    __tablename__ = "Task_materials"

    task_id = Column(ForeignKey('Tasks.id'), primary_key=True)
    material_id = Column(ForeignKey('Materials.id'), primary_key=True)
    quantity = Column(Integer, default=0.00)
    unit_price = Column(Float, default=0.00)

    task = relationship("Task", back_populates="materials")
    material = relationship("Material", back_populates="materials")
 """

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    projects = relationship("Project", back_populates="status")
    tasks = relationship("Task", back_populates="status")

class ItemType(Base):
    __tablename__ = "item_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    equipments = relationship("Equipment", back_populates="item_type")
    materials = relationship("Material", back_populates="item_type")
