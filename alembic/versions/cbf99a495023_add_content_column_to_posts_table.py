"""add content column to posts table

Revision ID: cbf99a495023
Revises: 0875947a1c00
Create Date: 2023-07-06 08:45:19.514855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf99a495023'
down_revision = '0875947a1c00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
