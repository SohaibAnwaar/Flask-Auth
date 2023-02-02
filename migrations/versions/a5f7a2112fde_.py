"""empty message

Revision ID: a5f7a2112fde
Revises: 
Create Date: 2023-02-03 00:18:53.280744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5f7a2112fde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('gender', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('membership', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('remarks', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'remarks')
    op.drop_column('user', 'membership')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###