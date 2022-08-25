"""WRITE_DOWN_EXPLANATIONS

Revision ID: 0be347d4b2a2
Revises: cf961c9cb76b
Create Date: 2022-08-24 08:04:42.555381

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0be347d4b2a2'
down_revision = 'cf961c9cb76b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=256), nullable=False))
    op.add_column('users', sa.Column('hashed_password', sa.String(length=256), nullable=False))
    op.drop_index('cognito_user_id', table_name='users')
    op.drop_index('username', table_name='users')
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'cognito_user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('cognito_user_id', mysql.CHAR(length=32), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('username', 'users', ['username'], unique=True)
    op.create_index('cognito_user_id', 'users', ['cognito_user_id'], unique=True)
    op.drop_column('users', 'hashed_password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
