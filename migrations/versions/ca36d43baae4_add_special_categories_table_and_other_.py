"""Add special_categories table and other columns

Revision ID: ca36d43baae4
Revises: 1fe3ba8bc9f3
Create Date: 2024-10-15 16:31:16.717244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca36d43baae4'
down_revision = '1fe3ba8bc9f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('special_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('item_special_categories',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('special_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['special_category_id'], ['special_categories.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'special_category_id')
    )
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('offer_price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('items_available', sa.String(), nullable=True))
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('image_url',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
        batch_op.drop_column('items_available')
        batch_op.drop_column('offer_price')

    op.drop_table('item_special_categories')
    op.drop_table('special_categories')
    # ### end Alembic commands ###
