"""Init_new

Revision ID: f70ba39f4195
Revises: 63a664960b6b
Create Date: 2024-02-09 01:03:30.168606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f70ba39f4195'
down_revision: Union[str, None] = '63a664960b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone', sa.String(length=25), nullable=False))
    op.drop_column('contacts', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone_number', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.drop_column('contacts', 'phone')
    # ### end Alembic commands ###
