"""empty message

Revision ID: f034224d84f3
Revises: 4cb2fda77332
Create Date: 2022-09-10 19:22:47.050649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f034224d84f3'
down_revision = '4cb2fda77332'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    # ### end Alembic commands ###
