"""WRITE_DOWN_EXPLANATIONS

Revision ID: 160be9072d47
Revises: 227ca71fa95c
Create Date: 2022-08-15 15:26:06.413905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '160be9072d47'
down_revision = '227ca71fa95c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posse_years',
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp'), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp on update current_timestamp'), nullable=False),
    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('year', sa.Float(), nullable=False),
    sa.Column('entrance_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.add_column('users', sa.Column('posse_year_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_foreign_key(None, 'users', 'posse_years', ['posse_year_id'], ['uuid'])
    op.drop_column('users', 'student_in_year_of_posse')
    op.add_column('users_input_curriculums', sa.Column('done', sa.Boolean(), nullable=False))
    op.add_column('users_output_curriculums', sa.Column('done', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_output_curriculums', 'done')
    op.drop_column('users_input_curriculums', 'done')
    op.add_column('users', sa.Column('student_in_year_of_posse', mysql.FLOAT(), nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'posse_year_id')
    op.drop_table('posse_years')
    # ### end Alembic commands ###
