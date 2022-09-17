"""empty message

Revision ID: 0c478a4c9bfd
Revises: f9d20dd870b4
Create Date: 2022-09-17 15:55:17.373068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c478a4c9bfd'
down_revision = 'f9d20dd870b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'post_tags', 'post', ['post_id'], ['id'])
    op.create_foreign_key(None, 'post_tags', 'tag', ['tag_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post_tags', type_='foreignkey')
    op.drop_constraint(None, 'post_tags', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    # ### end Alembic commands ###