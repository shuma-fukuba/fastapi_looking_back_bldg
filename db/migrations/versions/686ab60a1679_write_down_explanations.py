"""WRITE_DOWN_EXPLANATIONS

Revision ID: 686ab60a1679
Revises: bc6e463d4609
Create Date: 2022-08-10 15:06:48.018257

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '686ab60a1679'
down_revision = 'bc6e463d4609'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('weeks_ibfk_1', 'weeks', type_='foreignkey')
    op.drop_column('weeks', 'week_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weeks', sa.Column('week_id', mysql.CHAR(length=32), nullable=False))
    op.create_foreign_key('weeks_ibfk_1', 'weeks', 'weeks', ['week_id'], ['uuid'])
    # ### end Alembic commands ###