"""create tables roles

Revision ID: 61f25f7b3492
Revises: 
Create Date: 2024-03-30 00:11:11.285143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61f25f7b3492'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    create table roles (
        id serial primary key,
        name text not null unique        
    );

""")


def downgrade() -> None:
    op.execute("drop table roles")
