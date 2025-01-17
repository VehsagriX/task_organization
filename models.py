from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class OrganizationORM(Base):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    building_id: Mapped[int] = mapped_column(ForeignKey("building.id"))
    building: Mapped["BuildingORM"]= relationship(back_populates="organization")

    numbers: Mapped[list["NumberOrm"]] = relationship(
        back_populates="organization"
    )

    class_activity: Mapped[list["ActivityORM"]] = relationship(
        back_populates="organization_connection"
    )



class BuildingORM(Base):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    organization: Mapped["OrganizationORM"] = relationship(back_populates="building")



class NumberOrm(Base):
    __tablename__ = "number"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))

    organization: Mapped["OrganizationORM"] = relationship(
        back_populates="numbers"
    )



class ActivityClassificationORM(Base):
    __tablename__ = "activity_classification"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    activity_id: Mapped[list["ActivityORM"]] = relationship(
        back_populates="class_activity"
    )


class ActivityORM(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


    class_activity: Mapped["ActivityClassificationORM"] = relationship(
        back_populates="activity_id"
    )
    organization_connection: Mapped[list["OrganizationORM"]] = relationship(
        back_populates="class_activity"
    )



class OrganizationActivityORM(Base):
    __tablename__ = "organization_activity"

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activity.id"))

