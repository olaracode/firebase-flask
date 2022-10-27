"""empty message

Revision ID: 7b00dddd4c9b
Revises: 4cd4a9bbc428
Create Date: 2022-10-05 13:36:14.457303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b00dddd4c9b'
down_revision = '4cd4a9bbc428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('value', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'value')
    # ### end Alembic commands ###