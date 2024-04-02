"""create_users_to_roles_table

Revision ID: a07f7e0547cb
Revises: 1d3c0747776e
Create Date: 2024-03-30 02:04:08.168966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a07f7e0547cb'
down_revision: Union[str, None] = '1d3c0747776e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    create table users_to_roles (
        user_id int references users(id),
        role_id int references roles(id)
    )

""")


def downgrade() -> None:
    op.execute("drop table users_to_roles;")
