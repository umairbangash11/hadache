"""insert_roles

Revision ID: 1d3c0747776e
Revises: e7cb6955c73a
Create Date: 2024-03-30 01:54:57.298847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d3c0747776e'
down_revision: Union[str, None] = 'e7cb6955c73a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    insert into roles (name) values ('ROLES_USERS');
    insert into roles (name) values ('ROLES_MODERATORS');
    insert into roles (name) values ('ROLES_ADMIN');
""")


def downgrade() -> None:
    op.execute("""
    delete from roles where name in ('ROLES_ADMIN', 'ROLES_MODERATORS', 'ROLES_USERS');
""")
