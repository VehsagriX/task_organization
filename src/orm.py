from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from models import OrganizationORM, BuildingORM, NumberOrm, ActivityClassificationORM, ActivityORM, \
    OrganizationActivityORM
from database import Base, engine_sqlite, my_session
from schemas import OrganizationRelNumbsAndActivity, OrganizationDTO


class Orm:

    @staticmethod
    async def insert_organization():
        async with my_session() as session:
            organization_1 = OrganizationORM(
                title='ООО “Рога и Копыта”',
                building_id=2
            )

            organization_2 = OrganizationORM(
                title='ООО “Водка-Пиво”',
                building_id=2
            )
            organization_3 = OrganizationORM(
                title='ООО “Аграр”',
                building_id=2
            )
            organization_4 = OrganizationORM(
                title='ООО “Дорблю”',
                building_id=1
            )
            organization_5 = OrganizationORM(
                title='ООО “Малина”',
                building_id=1
            )

            session.add_all([organization_1, organization_2, organization_3, organization_4, organization_5])
            await session.commit()

    @staticmethod
    async def insert_buildings():
        async with my_session() as session:
            building_1 = BuildingORM(
                address='г. Москва, ул. Ленина 1, офис 17',
                latitude=1.33,
                longitude=30.44
            )
            building_2 = BuildingORM(
                address='г. Москва, ул. Cталина 4, офис 3',
                latitude=25.33,
                longitude=75.44
            )

            session.add_all([building_1, building_2])
            await session.commit()

    @staticmethod
    async def insert_numbers():
        async with my_session() as session:
            numbs_1 = NumberOrm(
                phone='+7999222222',
                organization_id=1
            )
            numbs_2 = NumberOrm(
                phone='+7999233222',
                organization_id=1
            )

            numbs_4 = NumberOrm(
                phone='+7977922222',
                organization_id=2
            )

            numbs_7 = NumberOrm(
                phone='+7977922422',
                organization_id=3
            )
            numbs_8 = NumberOrm(
                phone='+7933664545',
                organization_id=3
            )
            numbs_9 = NumberOrm(
                phone='+7755544477',
                organization_id=3
            )
            numbs_10 = NumberOrm(
                phone='+7978877956',
                organization_id=4
            )
            numbs_11 = NumberOrm(
                phone='+7977556687',
                organization_id=4
            )

            numbs_13 = NumberOrm(
                phone='+7978877960',
                organization_id=5
            )
            numbs_14 = NumberOrm(
                phone='+7977554872',
                organization_id=5
            )
            numbs_15 = NumberOrm(
                phone='+7797794587',
                organization_id=5
            )

            session.add_all([numbs_1, numbs_2, numbs_4, numbs_7, numbs_8, numbs_9, numbs_10,
                             numbs_11, numbs_13, numbs_14, numbs_15])

            await session.commit()

    @staticmethod
    async def insert_class_activity():
        async with my_session() as session:
            class_active_1 = ActivityClassificationORM(title='Еда')
            class_active_2 = ActivityClassificationORM(title='Автомобили')
            class_active_3 = ActivityClassificationORM(title='Ремонт')

            session.add_all([class_active_1, class_active_2, class_active_3])
            await session.commit()

    @staticmethod
    async def insert_active():
        async with my_session() as session:
            active_1 = ActivityORM(name='Мясная продукция', class_activity_id=1)
            active_2 = ActivityORM(name='Молочная продукция', class_activity_id=1)
            active_3 = ActivityORM(name='Легковые', class_activity_id=2)
            active_4 = ActivityORM(name='Грузовые', class_activity_id=2)
            active_5 = ActivityORM(name='Обувь', class_activity_id=3)
            active_6 = ActivityORM(name='Мебель', class_activity_id=3)
            active_7 = ActivityORM(name='Квартира', class_activity_id=1)

            get_organization_1 = select(OrganizationORM).options(
                selectinload(OrganizationORM.organization_actives)).filter_by(id=1)
            get_organization_2 = select(OrganizationORM).options(
                selectinload(OrganizationORM.organization_actives)).filter_by(id=2)
            get_organization_3 = select(OrganizationORM).options(
                selectinload(OrganizationORM.organization_actives)).filter_by(id=3)
            get_organization_4 = select(OrganizationORM).options(
                selectinload(OrganizationORM.organization_actives)).filter_by(id=4)
            get_organization_5 = select(OrganizationORM).options(
                selectinload(OrganizationORM.organization_actives)).filter_by(id=5)

            organization_1 = (await session.execute(get_organization_1)).scalar_one()
            organization_2 = (await session.execute(get_organization_2)).scalar_one()
            organization_3 = (await session.execute(get_organization_3)).scalar_one()
            organization_4 = (await session.execute(get_organization_4)).scalar_one()
            organization_5 = (await session.execute(get_organization_5)).scalar_one()

            organization_1.organization_actives.append(active_1)
            organization_1.organization_actives.append(active_2)
            organization_1.organization_actives.append(active_4)
            organization_2.organization_actives.append(active_3)
            organization_2.organization_actives.append(active_4)

            organization_3.organization_actives.append(active_5)
            organization_3.organization_actives.append(active_6)
            organization_3.organization_actives.append(active_7)

            organization_4.organization_actives.append(active_5)
            organization_4.organization_actives.append(active_7)

            organization_5.organization_actives.append(active_1)
            organization_5.organization_actives.append(active_2)

            session.add_all([active_1, active_2, active_3, active_4, active_5, active_6, active_7])

            await session.commit()

    @staticmethod
    async def get_organizations_rel_building():
        """
        select o.id, o.title, b.address
        from organization_table o
        Join building_table b ON o.building_id = b.id
        :return:
        """
        async with my_session() as session:
            query = (
                select(
                    OrganizationORM,
                )
                .options(joinedload(OrganizationORM.building))
                .options(selectinload(OrganizationORM.numbers))
                .options(selectinload(OrganizationORM.organization_actives))

            )
            res = await session.execute(query)

            result = res.unique().scalars().all()

            result_dto = [OrganizationRelNumbsAndActivity.model_validate(row, from_attributes=True) for row in result]

            return result_dto

    @staticmethod
    async def get_organizations_by_address(some_address: str = 'г. Москва, ул. Ленина 1, офис 17'):
        async with my_session() as session:
            query = (
                select(
                    OrganizationORM
                ).join(BuildingORM)
                .filter(BuildingORM.address == some_address)
            )
            res = await session.execute(query)
            result = res.scalars().all()

            result_dto = [OrganizationDTO.model_validate(row, from_attributes=True) for row in result]

            return result_dto

    @staticmethod
    async def get_organization_by_id(id_org: int = 3):
        async with my_session() as session:
            query = (
                select(
                    OrganizationORM,
                )
                .options(joinedload(OrganizationORM.building))
                .options(selectinload(OrganizationORM.numbers))
                .options(selectinload(OrganizationORM.organization_actives))
                .filter(OrganizationORM.id == id_org)
            )

            res = await session.execute(query)
            result = res.scalars().one_or_none()

            result_dto = OrganizationRelNumbsAndActivity.model_validate(result, from_attributes=True)

            return result_dto

    @staticmethod
    async def get_organization_by_activity(activity: str = 'Мясная продукция'):
        async with my_session() as session:
            """
            SELECT o.title AS organization_title
            FROM activity_table a
            JOIN organization_activity_table oa ON a.id = oa.activity_id
            JOIN organization_table o ON oa.organization_id = o.id
            WHERE a.name = 'Мясная продукция';
            """

            query = (
                select(OrganizationORM)
                .select_from(ActivityORM)

                .join(OrganizationActivityORM, OrganizationActivityORM.activity_id == ActivityORM.id)
                .join(OrganizationORM, OrganizationORM.id == OrganizationActivityORM.organization_id)
                .filter(ActivityORM.name == activity)

            )

            res = await session.execute(query)
            result = res.scalars().all()
            print(result)

            res_dto = [OrganizationDTO.model_validate(row, from_attributes=True) for row in result]

            return res_dto
