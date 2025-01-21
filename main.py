from fastapi import FastAPI, HTTPException, status
import uvicorn

from models import OrganizationORM
from orm import Orm


# app = FastAPI()
#
# @app.get('/org')
# async def get_organization():
#     organization = await Orm.get_organization_rel_building()
#     return organization

async def main():
    # await Orm.create_tables()
    # await Orm.insert_buildings()
    # await Orm.insert_organization()
    # await Orm.insert_numbers()
    # await Orm.insert_class_activity()
    # await Orm.insert_active()
    pass




    # await Orm.get_organizations_rel_building() #получить все организации
    # await Orm.get_organizations_by_address() #список всех организаций находящихся в конкретном здании
    # await Orm.get_organization_by_id() #вывод информации об организации по её идентификатору
    # await Orm.get_organization_by_activity() # список всех организаций, которые относятся к указанному виду деятельности

app = FastAPI(title="Организации")

@app.get('/organizations', status_code=status.HTTP_200_OK)
async def get_all_organizations():
    res = await Orm.get_organizations_rel_building()
    return {'data': res}




@app.get("/buildings/organizations")
async def get_organization_by_building(building_address: str):
    result = await Orm.get_organizations_by_address(building_address)
    if not result:
        raise HTTPException(status_code=404, detail="Building not found")
    return {'data': result}


@app.get("/organizations/{organization_id}")
async def get_organization(organization_id: int):
    organization = await Orm.get_organization_by_id(organization_id)
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return {'data': organization}



@app.get("/organizations/by_activity/{activity_name}")
async def get_organizations_by_activity(activity_name: str):
    result = await Orm.get_organization_by_activity(activity_name)
    if not result:
       raise HTTPException(status_code=404, detail="Activity not found")
    return {'data': result}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
    # asyncio.run(main())