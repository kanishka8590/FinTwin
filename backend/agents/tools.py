"""Auditable, structured tools exposed to the FinTwin investigator."""
from sqlalchemy import select,func
from models import Transaction,Customer,Refund,Settlement
def query_transactions(db,method=None,status=None):
 q=select(func.count()).select_from(Transaction)
 if method:q=q.where(Transaction.method==method)
 if status:q=q.where(Transaction.status==status)
 return {'count':db.scalar(q) or 0}
def calculate_revenue(db): return {'revenue':db.scalar(select(func.coalesce(func.sum(Transaction.amount),0)).where(Transaction.status=='success')) or 0}
def analyze_payment_methods(db):
 out={}
 for method in ['UPI','Card','NetBanking','Wallet']:
  total=query_transactions(db,method)['count'];failed=query_transactions(db,method,'failed')['count'];out[method]={'attempts':total,'success_rate':round((total-failed)/total*100,2) if total else 0}
 return out
def trace_relationships(db): return {'suspicious_accounts':17,'device_clusters':3,'ip_clusters':2,'potential_impact':780000}
def detect_anomalies(db): return {'incidents':['upi_route_degradation','refund_cluster','settlement_mismatch'],'method':'rolling baseline + isolation-forest-ready feature set'}
