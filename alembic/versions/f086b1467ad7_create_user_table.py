"""create_user_table

Revision ID: f086b1467ad7
Revises: 
Create Date: 2022-07-25 16:42:18.582300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f086b1467ad7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('users')
