"""empty message

Revision ID: 93671431113a
Revises: 37db8645926f
Create Date: 2023-11-18 00:46:00.883736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '93671431113a'
down_revision = '37db8645926f'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)

    columns = [col['name'] for col in inspector.get_columns('user')]

    with op.batch_alter_table('user', schema=None) as batch_op:
        if 'username' not in columns:
            batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=False))
        if 'places_visited' not in columns:
            batch_op.add_column(sa.Column('places_visited', sa.String(), nullable=True))  # Use String to store JSON

    # Create unique constraint after adding columns to avoid circular dependency
    with op.batch_alter_table('user', schema=None) as batch_op:
        if 'uq_user_username' not in [uc['name'] for uc in inspector.get_unique_constraints('user')]:
            batch_op.create_unique_constraint('uq_user_username', ['username'])

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('uq_user_username', type_='unique')
        batch_op.drop_column('places_visited')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
