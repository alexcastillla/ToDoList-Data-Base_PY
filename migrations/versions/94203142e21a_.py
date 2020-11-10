"""empty message

Revision ID: 94203142e21a
Revises: bad7659b8948
Create Date: 2020-11-10 11:36:02.621108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94203142e21a'
down_revision = 'bad7659b8948'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=120), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
