"""create_users_table

Revision ID: e7cb6955c73a
Revises: 61f25f7b3492
Create Date: 2024-03-30 01:49:39.178242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7cb6955c73a'
down_revision: Union[str, None] = '61f25f7b3492'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    create table users (
        id serial primary key,
        username text not null unique,
        email text not null unique,
        password text
    )

""")


def downgrade() -> None:
    op.execute("drop table users;")
