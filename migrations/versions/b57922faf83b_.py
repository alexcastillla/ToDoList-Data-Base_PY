"""empty message

Revision ID: b57922faf83b
Revises: 94203142e21a
Create Date: 2020-11-10 12:06:37.054744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b57922faf83b'
down_revision = '94203142e21a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'user', ['parent_id'], ['id'])
    op.add_column('user', sa.Column('username', sa.String(length=120), nullable=False))
    op.drop_index('email', table_name='user')
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'email')
    op.drop_column('user', 'password')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_column('user', 'username')
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'parent_id')
    # ### end Alembic commands ###
