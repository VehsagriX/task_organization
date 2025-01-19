from pydantic import BaseModel, ConfigDict






class OrganizationDTO(BaseModel):
    title: str





class NumbersDTO(BaseModel):
    phone: str

class ActivityDto(BaseModel):
    name: str


class BuildingDTO(BaseModel):
    address: str

class OrganizationRelNumbsAndActivity(OrganizationDTO):
    building: "BuildingDTO"
    numbers: list['NumbersDTO']
    organization_actives: list['ActivityDto']
