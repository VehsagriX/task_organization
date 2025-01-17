import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings


engine = create_async_engine(url=settings.DATABASE_URL, echo=True)

my_session = async_sessionmaker(engine, expire_on_commit=False)



# async def connect_db():
#     async with engin.connect() as connect:
#         res = await connect.execute(text('SELECT 1, 2, 3'))
#         print(f'{res.first()=}')
#
# asyncio.run(connect_db())


class Base(DeclarativeBase):
    pass