"""insert test data

Revision ID: 4e876f4139b0
Revises: 26874e649095
Create Date: 2025-01-22 12:49:30.949880

"""

from typing import Sequence, Union
from sqlalchemy.sql import table, column
from sqlalchemy import String, INTEGER, FLOAT
from alembic import op



# revision identifiers, used by Alembic.
revision: str = "4e876f4139b0"
down_revision: Union[str, None] = "26874e649095"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    users_table = table(
    'users',
    column('id', Integer),
    column('name', String),
    column('email', String),
)

    # Начальные данные
    seed_data = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'},
    ]

    def upgrade():
        op.bulk_insert(users_table, seed_data)

"""
    organization_table = table(
        "organization_table",
        column('title', String),
        column("building_id", INTEGER)
    )
    organization_data = [
        {'title':'ООО "Рога и Копыта"', "building_id": 2},
        {'title': 'ООО "Водка-Пиво"', "building_id": 2},
        {'title': 'ООО "Аграр"', "building_id": 2},
        {'title': 'ООО "Дорблю"', "building_id": 1},
        {'title': 'ООО “Малина”', "building_id": 1},
    ]

    building_table = table(
        "building_table",
        column("address", String),
        column("latitude", FLOAT),
        column("longitude", FLOAT),

    )
    building_data = [
        {'address': "г. Москва, ул. Ленина 1, офис 17", "latitude": 1.33, "longitude": 30.44},
        {'address': "г. Москва, ул. Cталина 4, офис 3", "latitude": 25.33, "longitude": 75.44},
    ]


    number_table = table(
        'number_table',
        column("phone", String),
        column("organization_id", INTEGER)
    )

    numbers_data = [
        {"phone": "+7999222222", "organization_id": 1},
        {"phone": "+7999233222", "organization_id": 1},
        {"phone": "+7977922222", "organization_id": 2},
        {"phone": "+7977922242", "organization_id": 3},
        {"phone": "+7933664542", "organization_id": 3},
        {"phone": "+7755544477", "organization_id": 3},
        {"phone": "+7978877956", "organization_id": 4},
        {"phone": "+7977556687", "organization_id": 4},
        {"phone": "+7977554872", "organization_id": 5},
        {"phone": "+7797794587", "organization_id": 5},

    ]

    class_activity_table = table(
        "activity_classification_table",
        column("title", String),
    )

    class_activity_data = [
        {"title": "Еда"},
        {"title": "Автомобили"},
        {"title": "Ремонт"},
    ]


    activity_table = table(
        "activity_table",
        column("name", String),
        column("class_activity_id", INTEGER)
    )
    activity_data = [
        {"name": "Мясная продукция", "class_activity_id": 1},
        {"name": "Молочная продукция", "class_activity_id": 1},
        {"name": "Легковые", "class_activity_id": 2},
        {"name": "Грузовые", "class_activity_id": 2},
        {"name": "Обувь", "class_activity_id": 3},
        {"name": "Мебель", "class_activity_id": 3},
        {"name": "Квартира", "class_activity_id": 3},

    ]
    op.bulk_insert(organization_table, organization_data)
    op.bulk_insert(building_table, building_data)
    op.bulk_insert(number_table, numbers_data)
    op.bulk_insert(class_activity_table, class_activity_data)
    op.bulk_insert(activity_table, activity_data)

def downgrade() -> None:
    """def downgrade():
        # Используем `op.execute` для удаления конкретных строк, если необходимо
        op.execute(
            "DELETE FROM users WHERE id IN (1, 2, 3);"
        )

    """
    op.execute(
        "DELETE FROM organization_table"
    )
    op.execute(
        "DELETE FROM building_table"
    )
    op.execute(
        "DELETE FROM number_table"
    )
    op.execute(
        "DELETE FROM activity_classification_table"
    )
    op.execute(
        "DELETE FROM activity_table"
    )
