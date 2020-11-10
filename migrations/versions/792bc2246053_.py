"""empty message

Revision ID: 792bc2246053
Revises: b57922faf83b
Create Date: 2020-11-10 15:14:14.921951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '792bc2246053'
down_revision = 'b57922faf83b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('todo_ibfk_1', 'todo', type_='foreignkey')
    op.create_foreign_key(None, 'todo', 'user', ['user_id'], ['id'])
    op.drop_column('todo', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('parent_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.create_foreign_key('todo_ibfk_1', 'todo', 'user', ['parent_id'], ['id'])
    op.drop_column('todo', 'user_id')
    # ### end Alembic commands ###
