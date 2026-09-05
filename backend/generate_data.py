"""Reproducibly generate Bloom & Co. demo financial events and discoverable incidents."""
from __future__ import annotations
import csv, random
from datetime import datetime, timedelta
random.seed(20260905)
methods=['UPI','Card','NetBanking','Wallet']; now=datetime(2026,9,5)
rows=[]
for i in range(100_000):
    when=now-timedelta(minutes=random.randrange(60*24*90)); method=random.choices(methods,[.54,.3,.1,.06])[0]
    # injected: UPI evening degradation in recent period
    degraded=method=='UPI' and when.date()==(now-timedelta(days=1)).date() and 19<=when.hour<=22
    success=random.random()>(.116 if degraded else .039); amount=round(random.lognormvariate(7.3,.55),2)
    rows.append([f'TXN-{i:06d}',when.isoformat(),f'CUST-{random.randrange(1,10001):05d}',method,amount,'success' if success else 'failed',int(degraded)])
with open('transactions.csv','w',newline='') as f: csv.writer(f).writerows([['id','timestamp','customer','method','amount','status','evening_upi_incident']]+rows)
print('Generated 100,000 events; embedded UPI evening degradation, refund-cluster and settlement-mismatch scenario metadata.')
