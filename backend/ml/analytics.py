"""Explainable, deterministic ML analytics over persisted financial events."""
import numpy as np
from sqlalchemy import select
from models import Transaction
def anomaly_detection(db):
 from sklearn.ensemble import IsolationForest
 rows=db.scalars(select(Transaction).limit(10000)).all()
 X=np.array([[x.amount,x.occurred_at.hour,1 if x.method=='UPI' else 0] for x in rows])
 if len(X)<20:return {'anomalies':0,'method':'IsolationForest','samples':len(X)}
 labels=IsolationForest(contamination=.025,random_state=20260905).fit_predict(X)
 return {'anomalies':int((labels==-1).sum()),'samples':len(X),'method':'IsolationForest','features':['amount','hour','is_upi']}
def customer_segmentation(db):
 from sklearn.cluster import KMeans
 rows=db.scalars(select(Transaction).limit(20000)).all(); buckets={}
 for t in rows:buckets.setdefault(t.customer_id,[0,0]);buckets[t.customer_id][0]+=t.amount;buckets[t.customer_id][1]+=1
 X=np.array(list(buckets.values()),dtype=float)
 if len(X)<3:return []
 labels=KMeans(n_clusters=3,random_state=20260905,n_init=10).fit_predict(X)
 return [{'segment':int(i),'customers':int((labels==i).sum())} for i in range(3)]
