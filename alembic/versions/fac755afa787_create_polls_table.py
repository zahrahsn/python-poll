"""create_polls_table

Revision ID: fac755afa787
Revises: f086b1467ad7
Create Date: 2022-07-26 12:00:27.695306

"""
import enum
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac755afa787'
down_revision = 'f086b1467ad7'
branch_labels = None
depends_on = None

class PollType(enum.Enum):
    text=1
    image=2

def upgrade() -> None:
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(PollType), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),

    )


def downgrade() -> None:
    op.drop_table('polls')
