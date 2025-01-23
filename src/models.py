

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class OrganizationORM(Base):
    __tablename__ = "organization_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    building_id: Mapped[int] = mapped_column(ForeignKey("building_table.id", ondelete="CASCADE"))

    building: Mapped["BuildingORM"] = relationship(
        back_populates="organization_list"
    )

    numbers: Mapped[list["NumberOrm"]] = relationship(
        back_populates="organization_nums"
    )

    organization_actives: Mapped[list["ActivityORM"]] = relationship(
        back_populates="organization_connection",
        secondary="organization_activity_table"
    )


class BuildingORM(Base):
    __tablename__ = "building_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]


    organization_list: Mapped[list["OrganizationORM"]] = relationship(back_populates="building")


class NumberOrm(Base):
    __tablename__ = "number_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey("organization_table.id",  ondelete="CASCADE"))

    organization_nums: Mapped["OrganizationORM"] = relationship(
        back_populates="numbers"
    )


class ActivityClassificationORM(Base):
    __tablename__ = "activity_classification_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]


    activity_list: Mapped[list["ActivityORM"]] = relationship(
        back_populates="class_activity"
    )


class ActivityORM(Base):
    __tablename__ = "activity_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    class_activity_id: Mapped[int] = mapped_column(ForeignKey("activity_classification_table.id", ondelete="CASCADE"))

    class_activity: Mapped["ActivityClassificationORM"] = relationship(
        back_populates="activity_list"
    )
    organization_connection: Mapped[list["OrganizationORM"]] = relationship(
        back_populates="organization_actives",
        secondary="organization_activity_table"
    )


class OrganizationActivityORM(Base):
    __tablename__ = "organization_activity_table"

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization_table.id", ondelete="CASCADE"), primary_key=True)
    activity_id: Mapped[int] = mapped_column(ForeignKey("activity_table.id", ondelete="CASCADE"), primary_key=True)
