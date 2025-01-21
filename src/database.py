from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


engine_postg = create_async_engine(url=settings.DATABASE_URL, echo=True)
engine_sqlite = create_async_engine(url=settings.data_sqlite, echo=True)
my_session = async_sessionmaker(engine_sqlite, expire_on_commit=False)




class Base(DeclarativeBase):
    repr_cols_num = 5
    repr_cols = tuple()


    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"