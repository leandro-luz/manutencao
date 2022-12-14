"""empty message

Revision ID: 5cb01d94cbd2
Revises: 2782f5926856
Create Date: 2022-09-10 19:58:07.224170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb01d94cbd2'
down_revision = '2782f5926856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_table('post_tags')
    op.drop_table('tag')
    # ### end Alembic commands ###
