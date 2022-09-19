"""empty message

Revision ID: 0fdcd2e101e4
Revises: 0c478a4c9bfd
Create Date: 2022-09-19 10:07:30.759258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0fdcd2e101e4'
down_revision = '0c478a4c9bfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.alter_column('comment', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('comment', 'text',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.alter_column('post', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('post', 'text',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'post_tags', 'post', ['post_id'], ['id'])
    op.create_foreign_key(None, 'post_tags', 'tag', ['tag_id'], ['id'])
    op.alter_column('tag', 'title',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.create_unique_constraint(None, 'tag', ['title'])
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint(None, 'tag', type_='unique')
    op.alter_column('tag', 'title',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint(None, 'post_tags', type_='foreignkey')
    op.drop_constraint(None, 'post_tags', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.alter_column('post', 'text',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('post', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.alter_column('comment', 'text',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('comment', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_table('role_users')
    op.drop_table('role')
    # ### end Alembic commands ###
