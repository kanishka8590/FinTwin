"""Complete FinTwin operational schema.

Revision ID: 0002
Revises: 0001
"""
from alembic import op
import sqlalchemy as sa
revision='0002';down_revision='0001';branch_labels=None;depends_on=None
def upgrade():
 op.add_column('customers',sa.Column('city',sa.String(32),server_default='Mumbai'))
 op.create_table('orders',sa.Column('id',sa.Integer,primary_key=True),sa.Column('external_id',sa.String(32),unique=True),sa.Column('customer_id',sa.Integer,sa.ForeignKey('customers.id')),sa.Column('product_id',sa.Integer),sa.Column('total',sa.Float),sa.Column('status',sa.String(20)),sa.Column('occurred_at',sa.DateTime))
 op.create_table('transactions',sa.Column('id',sa.Integer,primary_key=True),sa.Column('external_id',sa.String(32),unique=True),sa.Column('customer_id',sa.Integer,sa.ForeignKey('customers.id')),sa.Column('order_id',sa.Integer,sa.ForeignKey('orders.id')),sa.Column('amount',sa.Float),sa.Column('method',sa.String(20)),sa.Column('status',sa.String(20)),sa.Column('occurred_at',sa.DateTime),sa.Column('risk',sa.String(12)))
 for name,cols in [('payments',[sa.Column('transaction_id',sa.Integer,sa.ForeignKey('transactions.id')),sa.Column('gateway',sa.String(32)),sa.Column('route',sa.String(32)),sa.Column('fee',sa.Float)]),('refunds',[sa.Column('transaction_id',sa.Integer,sa.ForeignKey('transactions.id')),sa.Column('amount',sa.Float),sa.Column('reason',sa.String(80)),sa.Column('occurred_at',sa.DateTime)]),('disputes',[sa.Column('transaction_id',sa.Integer,sa.ForeignKey('transactions.id')),sa.Column('amount',sa.Float),sa.Column('status',sa.String(24))]),('settlements',[sa.Column('reference',sa.String(32),unique=True),sa.Column('expected',sa.Float),sa.Column('received',sa.Float),sa.Column('occurred_at',sa.DateTime)]),('subscriptions',[sa.Column('customer_id',sa.Integer,sa.ForeignKey('customers.id')),sa.Column('plan',sa.String(32)),sa.Column('value',sa.Float),sa.Column('status',sa.String(24)),sa.Column('next_bill_at',sa.DateTime)]),('expenses',[sa.Column('category',sa.String(32)),sa.Column('amount',sa.Float),sa.Column('occurred_at',sa.DateTime)]),('devices',[sa.Column('fingerprint',sa.String(32),unique=True),sa.Column('ip_cluster',sa.String(32)),sa.Column('risk_score',sa.Float)]),('risk_events',[sa.Column('event_type',sa.String(64)),sa.Column('severity',sa.String(12)),sa.Column('entity_ref',sa.String(64)),sa.Column('impact',sa.Float),sa.Column('occurred_at',sa.DateTime),sa.Column('resolved',sa.Boolean,server_default=sa.false())])]: op.create_table(name,sa.Column('id',sa.Integer,primary_key=True),*cols)
def downgrade():
 for table in ['risk_events','devices','expenses','subscriptions','settlements','disputes','refunds','payments','transactions','orders']:op.drop_table(table)
 op.drop_column('customers','city')
