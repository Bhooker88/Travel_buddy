"""empty message

Revision ID: 37db8645926f
Revises: 0bc8dcdf1da0
Create Date: 2023-11-18 00:46:00.883736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37db8645926f'
down_revision = '0bc8dcdf1da0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('places_visited', sa.ARRAY(sa.String()), nullable=True))
        batch_op.create_unique_constraint('uq_user_username', ['username'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint('uq_user_username', type_='unique')
        batch_op.drop_column('places_visited')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
