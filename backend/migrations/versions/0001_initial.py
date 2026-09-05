"""Initial FinTwin schema.

Revision ID: 0001
"""
from alembic import op
import sqlalchemy as sa
revision='0001';down_revision=None;branch_labels=None;depends_on=None
def upgrade():
 op.create_table('merchants',sa.Column('id',sa.Integer,primary_key=True),sa.Column('name',sa.String(100),unique=True))
 op.create_table('customers',sa.Column('id',sa.Integer,primary_key=True),sa.Column('external_id',sa.String(32),unique=True),sa.Column('segment',sa.String(20)),sa.Column('device_id',sa.String(32)),sa.Column('city',sa.String(32)))
 op.create_table('products',sa.Column('id',sa.Integer,primary_key=True),sa.Column('sku',sa.String(32),unique=True),sa.Column('name',sa.String(100)),sa.Column('price',sa.Float),sa.Column('category',sa.String(32)))
def downgrade(): op.drop_table('products');op.drop_table('customers');op.drop_table('merchants')
