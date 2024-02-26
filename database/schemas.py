from pydantic import BaseModel, Field, condecimal
import datetime
from typing import List
from decimal import Decimal
# ---------------------------------------USER SCHEMA ---------------------------------------
class UserBase(BaseModel):
    username:str
    email:str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class RequestDetails(BaseModel):
    email:str
    password:str
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class ChangePassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime


# ---------------------------------------EQUIPMENT SCHEMA---------------------------------------
class EquipmentBase(BaseModel):
    equipmentName: str
    item_type_id: int = Field(
        title="The id of the item_type record",
        description="The item_type record needs to be already created"
    )
    task_equipment_id: int
    item_type_id:int

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int

    class Config:
        orm_mode = True

# ---------------------------------------MATERIAL SCHEMA---------------------------------------
class MaterialBase(BaseModel):
    materialName: str
    item_type_id: int = Field(
        title="The id of the item_type record",
        description="The item_type record needs to be already created"
    )
    task_material_id: int
    item_type_id: int

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int

    class Config:
        orm_mode = True

# ---------------------------------------TASK SCHEMA---------------------------------------
class TaskBase(BaseModel):
    taskame:str
    status_id: int = Field(
        title="The id of the status record",
        description="The status record needs to be already created"
    )
    project_task_id: int
    status_id:int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    materials:List[Material] = []
    equipments:List[Equipment] = []
    
    class Config:
        orm_mode = True


""" class TaskEquipmentBase(BaseModel):    
    task_id: int
    equipment_id: int
    quantity: int = Field(
        title="The quantity ordered for this item"
    )
    unit_price: Decimal = Field(default=0.0, max_digits=5, decimal_places=3)
    
class TaskEquipmentCreate(TaskEquipmentBase):
    pass

class TaskMaterialBase(BaseModel):    
    task_id: int
    material_id: int
    quantity: int = Field(
        title="The quantity ordered for this item"
    )
    unit_price: Decimal = Field(default=0.0, max_digits=5, decimal_places=3)
    
class TaskMaterialBaseCreate(TaskMaterialBase):
    pass
 """
# ---------------------------------------PROJECT SCHEMA ---------------------------------------
class ProjectBase(BaseModel):
     name: str
     owner_id:int= Field(
        title="The id of the owner/customer record",
        description="The owner/customer record needs to be already created"
    )
     status_id: int = Field(
        title="The id of the status record",
        description="The status record needs to be already created"
    )
    

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    budget: float
    tasks:List[Task] = []

    class Config:
        orm_mode = True

""" class ProjectEquipmentBase(BaseModel):     
    project_id: int
    equipment_id: int
    quantity: int = Field(
        title="The quantity ordered for this item"
    )
    unit_price: Decimal = Field(default=0.0, max_digits=5, decimal_places=3)


class ProjectEquipmentCreate(ProjectEquipmentBase):  
    pass

class ProjectMaterialBase(BaseModel): 
    project_id: int
    material_id: int 
    quantity: int = Field(
        title="The quantity ordered for this item"
    )
    unit_price: Decimal = Field(default=0.0, max_digits=5, decimal_places=3)

class ProjectMaterialCreate(ProjectMaterialBase):
    pass """


# ---------------------------------------CUSTOMER SCHEMA---------------------------------------
class customerBase(BaseModel):
    firstName: str
    lastName: str
    email:str
    phone:str

class CustomerCreate(customerBase):
    pass

class Customer(customerBase):
    id: int
    projects:List[Project] = []

    class Config:
        orm_mode = True

# ---------------------------------------Status SCHEMA---------------------------------------
class StatusBase(BaseModel):
    name: str = Field(
        title="The name of the Status",
        description="The name has a maximum length of 30 characters",
        max_length=30,
        example = "Mobile phone"
    )

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True

# ---------------------------------------ItemType SCHEMA---------------------------------------
class ItemTypeBase(BaseModel):
    name: str = Field(
        title="The name of the ItemType",
        description="The name has a maximum length of 30 characters",
        max_length=30,
        example = "Mobile phone"
    )

class ItemTypeCreate(ItemTypeBase):
    pass

class ItemType(ItemTypeBase):
    id: int

    class Config:
        orm_mode = True