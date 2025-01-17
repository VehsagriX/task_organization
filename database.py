import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings


engin = create_async_engine(settings.DATABASE_URL, echo=True)

my_session = async_sessionmaker(engin, expire_on_commit=False)



# async def connect_db():
#     async with engin.connect() as connect:
#         res = await connect.execute(text('SELECT 1, 2, 3'))
#         print(f'{res.first()=}')



class Base(DeclarativeBase):
    pass