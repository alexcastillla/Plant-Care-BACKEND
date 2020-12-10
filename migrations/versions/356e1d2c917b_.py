"""empty message

Revision ID: 356e1d2c917b
Revises: 93555bc8aa90
Create Date: 2020-12-08 14:43:42.917856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356e1d2c917b'
down_revision = '93555bc8aa90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('id_user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'plants', 'users', ['id_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plants', type_='foreignkey')
    op.drop_column('plants', 'id_user')
    # ### end Alembic commands ###
