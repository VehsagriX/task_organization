from fastapi import FastAPI
import asyncio
from orm import Orm

async def main():
    await Orm.create_tables()
    await Orm.insert_buildings()
    await Orm.insert_organization()
    await Orm.insert_numbers()
    await Orm.insert_class_activity()
    await Orm.insert_active()



if __name__ == "__main__":
    asyncio.run(main())