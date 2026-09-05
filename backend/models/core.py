from datetime import datetime
from sqlalchemy import String,Float,DateTime,ForeignKey,Boolean,Index
from sqlalchemy.orm import Mapped,mapped_column
from database import Base
class Merchant(Base):
 __tablename__='merchants'; id:Mapped[int]=mapped_column(primary_key=True); name:Mapped[str]=mapped_column(String(100),unique=True)
class Customer(Base):
 __tablename__='customers'; id:Mapped[int]=mapped_column(primary_key=True); external_id:Mapped[str]=mapped_column(String(32),unique=True,index=True); segment:Mapped[str]=mapped_column(String(20)); device_id:Mapped[str]=mapped_column(String(32),index=True); city:Mapped[str]=mapped_column(String(32),default='Mumbai')
class Product(Base):
 __tablename__='products'; id:Mapped[int]=mapped_column(primary_key=True); sku:Mapped[str]=mapped_column(String(32),unique=True); name:Mapped[str]=mapped_column(String(100)); price:Mapped[float]=mapped_column(Float); category:Mapped[str]=mapped_column(String(32))
class Order(Base):
 __tablename__='orders'; id:Mapped[int]=mapped_column(primary_key=True); external_id:Mapped[str]=mapped_column(String(32),unique=True,index=True); customer_id:Mapped[int]=mapped_column(ForeignKey('customers.id'),index=True); product_id:Mapped[int]=mapped_column(ForeignKey('products.id')); total:Mapped[float]=mapped_column(Float); status:Mapped[str]=mapped_column(String(20)); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True)
class Transaction(Base):
 __tablename__='transactions'; id:Mapped[int]=mapped_column(primary_key=True); external_id:Mapped[str]=mapped_column(String(32),unique=True,index=True); customer_id:Mapped[int]=mapped_column(ForeignKey('customers.id'),index=True); order_id:Mapped[int|None]=mapped_column(ForeignKey('orders.id'),nullable=True); amount:Mapped[float]=mapped_column(Float); method:Mapped[str]=mapped_column(String(20),index=True); status:Mapped[str]=mapped_column(String(20),index=True); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True); risk:Mapped[str]=mapped_column(String(12),default='low')
 __table_args__=(Index('ix_tx_time_method','occurred_at','method'),)
class Payment(Base):
 __tablename__='payments'; id:Mapped[int]=mapped_column(primary_key=True); transaction_id:Mapped[int]=mapped_column(ForeignKey('transactions.id'),index=True); gateway:Mapped[str]=mapped_column(String(32)); route:Mapped[str]=mapped_column(String(32)); fee:Mapped[float]=mapped_column(Float)
class Refund(Base):
 __tablename__='refunds'; id:Mapped[int]=mapped_column(primary_key=True); transaction_id:Mapped[int]=mapped_column(ForeignKey('transactions.id'),index=True); amount:Mapped[float]=mapped_column(Float); reason:Mapped[str]=mapped_column(String(80)); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True)
class Dispute(Base):
 __tablename__='disputes'; id:Mapped[int]=mapped_column(primary_key=True); transaction_id:Mapped[int]=mapped_column(ForeignKey('transactions.id')); amount:Mapped[float]=mapped_column(Float); status:Mapped[str]=mapped_column(String(24))
class Settlement(Base):
 __tablename__='settlements'; id:Mapped[int]=mapped_column(primary_key=True); reference:Mapped[str]=mapped_column(String(32),unique=True); expected:Mapped[float]=mapped_column(Float); received:Mapped[float]=mapped_column(Float); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True)
class Subscription(Base):
 __tablename__='subscriptions'; id:Mapped[int]=mapped_column(primary_key=True); customer_id:Mapped[int]=mapped_column(ForeignKey('customers.id')); plan:Mapped[str]=mapped_column(String(32)); value:Mapped[float]=mapped_column(Float); status:Mapped[str]=mapped_column(String(24)); next_bill_at:Mapped[datetime]=mapped_column(DateTime)
class Expense(Base):
 __tablename__='expenses'; id:Mapped[int]=mapped_column(primary_key=True); category:Mapped[str]=mapped_column(String(32)); amount:Mapped[float]=mapped_column(Float); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True)
class Device(Base):
 __tablename__='devices'; id:Mapped[int]=mapped_column(primary_key=True); fingerprint:Mapped[str]=mapped_column(String(32),unique=True); ip_cluster:Mapped[str]=mapped_column(String(32)); risk_score:Mapped[float]=mapped_column(Float)
class RiskEvent(Base):
 __tablename__='risk_events'; id:Mapped[int]=mapped_column(primary_key=True); event_type:Mapped[str]=mapped_column(String(64),index=True); severity:Mapped[str]=mapped_column(String(12)); entity_ref:Mapped[str]=mapped_column(String(64)); impact:Mapped[float]=mapped_column(Float); occurred_at:Mapped[datetime]=mapped_column(DateTime,index=True); resolved:Mapped[bool]=mapped_column(Boolean,default=False)
