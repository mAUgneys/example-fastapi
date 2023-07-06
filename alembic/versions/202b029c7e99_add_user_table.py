"""add user table

Revision ID: 202b029c7e99
Revises: cbf99a495023
Create Date: 2023-07-06 09:53:59.276673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202b029c7e99'
down_revision = 'cbf99a495023'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
