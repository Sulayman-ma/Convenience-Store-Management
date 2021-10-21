"""Changed total_quantity column name to purchase_quantity

Revision ID: 75bed689eee8
Revises: 3d968c7ab0a1
Create Date: 2021-10-21 10:27:30.917524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75bed689eee8'
down_revision = '3d968c7ab0a1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('cart', 'total_quantity', new_column_name='purchase_quantity')


def downgrade():
    op.alter_column('cart', 'purchase_quantity', new_column_name='total_quantity')
