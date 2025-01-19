from fastapi import FastAPI
import asyncio
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




    await Orm.get_organization_rel_building()
    # await Orm.get_organization_by_address()


if __name__ == "__main__":
    asyncio.run(main())