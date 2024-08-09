"""
Init database
Revision ID: 0a5ed721f6bd
Revises:
Create Date: 2024-08-06 15:36:32.232094

"""
# pylint: disable=no-member
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '0a5ed721f6bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Update database schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(64), nullable=False),
        sa.Column('password', sa.Text(), nullable=False),
        sa.Column('email', sa.Text(), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade database schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
