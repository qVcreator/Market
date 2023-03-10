"""adds new fields

Revision ID: e1728b2e3833
Revises: 
Create Date: 2023-02-03 00:45:51.580979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1728b2e3833'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'is_deleted')
    # ### end Alembic commands ###
