from fastapi import FastAPI, HTTPException, status
import uvicorn
import os, sys
import asyncio
from models import OrganizationORM
from orm import Orm
from schemas import OrganizationRelNumbsAndActivity, OrganizationDTO


sys.path.insert(1, os.path.join(sys.path[0], '..'))







app = FastAPI(title="Организации")

@app.get('/organizations', status_code=status.HTTP_200_OK)
async def get_all_organizations() -> list[OrganizationRelNumbsAndActivity]:
    res = await Orm.get_organizations_rel_building()
    return  res




@app.get("/buildings/organizations")
async def get_organization_by_building(building_address: str)-> OrganizationDTO:
    building_address= building_address.title()
    result = await Orm.get_organizations_by_address(building_address)
    if not result:
        raise HTTPException(status_code=404, detail="Building not found")
    return result


@app.get("/organizations/{organization_id}")
async def get_organization(organization_id: int)-> OrganizationRelNumbsAndActivity:
    organization = await Orm.get_organization_by_id(organization_id)
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return organization



@app.get("/organizations/by_activity/{activity_name}")
async def get_organizations_by_activity(activity_name: str)-> dict:
    activity_name = activity_name.capitalize()
    result = await Orm.get_organization_by_activity(activity_name)
    print(result)
    if not result:
       raise HTTPException(status_code=404, detail="Activity not found")
    return {'data': result}

if __name__ == "__main__":


    uvicorn.run(app="main:app", reload=True)