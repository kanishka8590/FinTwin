"""Reproducible 100k-event Bloom & Co. database seed with discoverable incidents."""
from datetime import datetime,timedelta
import random
from database import Base,engine,SessionLocal
from models import *
def seed(n=100000):
 Base.metadata.create_all(engine);db=SessionLocal()
 if db.query(Transaction).first(): return
 rng=random.Random(20260905);now=datetime(2026,9,5);db.add(Merchant(name='Bloom & Co.'))
 db.bulk_save_objects([Customer(external_id=f'CUST-{i:05}',segment=rng.choice(['new','repeat','high_value']),device_id=f'DEV-{i%900:04}',city=rng.choice(['Mumbai','Bengaluru','Delhi','Pune','Hyderabad'])) for i in range(1,10001)])
 db.bulk_save_objects([Product(sku=f'BC-{i:03}',name=f'Bloom collection {i}',price=599+i*130,category=rng.choice(['care','home','gift'])) for i in range(1,31)]);db.commit()
 orders=[];tx=[];refunds=[];risks=[]
 for i in range(n):
  when=now-timedelta(minutes=rng.randrange(90*24*60));customer=(i%10000)+1;method=rng.choices(['UPI','Card','NetBanking','Wallet'],[54,30,10,6])[0]; degraded=method=='UPI' and when.date()==datetime(2026,9,4).date() and 19<=when.hour<=22; status='failed' if rng.random()<(0.116 if degraded else .039) else 'success';amount=round(rng.lognormvariate(7.3,.55),2)
  if i<25000: orders.append(Order(external_id=f'ORD-{i:06}',customer_id=customer,product_id=i%30+1,total=amount,status='paid' if status=='success' else 'abandoned',occurred_at=when))
  tx.append(Transaction(external_id=f'TXN-{i:06}',customer_id=customer,order_id=(i%25000)+1 if i>=25000 else i+1,amount=amount,method=method,status=status,occurred_at=when,risk='high' if i<17 else 'low'))
 db.bulk_save_objects(orders);db.commit();db.bulk_save_objects(tx);db.commit()
 for i in range(17): refunds.append(Refund(transaction_id=i+1,amount=46000+rng.randrange(15000),reason='coordinated cluster',occurred_at=now-timedelta(days=2)));risks.append(RiskEvent(event_type='refund_cluster',severity='high',entity_ref=f'DEV-{i%3:04}',impact=470000,occurred_at=now-timedelta(days=2)))
 risks += [RiskEvent(event_type='upi_route_degradation',severity='medium',entity_ref='UPI-EVENING',impact=420000,occurred_at=now-timedelta(days=1)),RiskEvent(event_type='settlement_mismatch',severity='low',entity_ref='SET-ANOM-001',impact=190000,occurred_at=now-timedelta(days=1))]
 db.bulk_save_objects(refunds+risks);db.add(Settlement(reference='SET-ANOM-001',expected=190000,received=171000,occurred_at=now-timedelta(days=1)));db.commit();db.close()
if __name__=='__main__': seed()
