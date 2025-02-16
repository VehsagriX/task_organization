"""create tables

Revision ID: fedf9921ddfa
Revises: 
Create Date: 2025-01-22 14:53:14.351603

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fedf9921ddfa"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "activity_classification_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "building_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "activity_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("class_activity_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["class_activity_id"],
            ["activity_classification_table.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "organization_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["building_id"], ["building_table.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "number_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("organization_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organization_table.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "organization_activity_table",
        sa.Column("organization_id", sa.Integer(), nullable=False),
        sa.Column("activity_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["activity_id"], ["activity_table.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organization_table.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("organization_id", "activity_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("organization_activity_table")
    op.drop_table("number_table")
    op.drop_table("organization_table")
    op.drop_table("activity_table")
    op.drop_table("building_table")
    op.drop_table("activity_classification_table")
    # ### end Alembic commands ###
