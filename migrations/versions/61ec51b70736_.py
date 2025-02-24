"""empty message

Revision ID: 61ec51b70736
Revises: 
Create Date: 2021-03-23 09:35:00.670466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ec51b70736'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('property_info', 'bathrooms',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('property_info', 'bedrooms',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('property_info', 'filename',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('property_info', 'propertyTitle',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('property_info', 'propertyTitle',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('property_info', 'filename',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('property_info', 'bedrooms',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('property_info', 'bathrooms',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
