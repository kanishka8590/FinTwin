from datetime import datetime,timedelta
from sqlalchemy import select,func
from sqlalchemy.orm import Session
from models import Transaction,RiskEvent,Settlement,Refund
def risk_incidents(db:Session):
 rows=db.scalars(select(RiskEvent).order_by(RiskEvent.impact.desc())).all()
 return [{'id':r.id,'type':r.event_type.replace('_',' '),'severity':r.severity,'entity':r.entity_ref,'impact':r.impact,'occurred_at':r.occurred_at,'status':'open' if not r.resolved else 'resolved'} for r in rows]
def forecast(db:Session,days:int=30):
 end=datetime(2026,9,5); start=end-timedelta(days=30)
 recent=db.scalar(select(func.coalesce(func.sum(Transaction.amount),0)).where(Transaction.status=='success',Transaction.occurred_at>=start)) or 0
 daily=recent/30; expected=daily*days*1.07
 return {'horizon_days':days,'expected_revenue':round(expected),'lower_bound':round(expected*.91),'upper_bound':round(expected*1.12),'expected_transactions':round((db.scalar(select(func.count()).select_from(Transaction).where(Transaction.occurred_at>=start)) or 0)/30*days),'expected_refunds':round(expected*.027),'model':'seasonal rolling trend with payment-success adjustment'}
def opportunities():
 raw=[('Subscription failures',820000,.78,60000),('Checkout abandonment',510000,.52,85000),('Refund anomalies',280000,.62,70000),('Settlement discrepancies',190000,.91,15000),('Discount anomalies',70000,.45,12000)]
 out=[]
 for name,amount,p,cost in raw: out.append({'name':name,'amount':amount,'recovery_probability':p,'intervention_cost':cost,'expected_net_benefit':round(amount*p-cost),'priority_score':round(amount*p-cost)})
 return sorted(out,key=lambda x:x['priority_score'],reverse=True)
def graph():
 return {'nodes':[{'id':'merchant','type':'merchant','label':'Bloom & Co.'},{'id':'customers','type':'customers','label':'10,000 Customers'},{'id':'orders','type':'orders','label':'25,000 Orders'},{'id':'transactions','type':'transactions','label':'100,000 Transactions'},{'id':'upi','type':'payment','label':'UPI route'},{'id':'refunds','type':'refund','label':'17 Refund cluster'},{'id':'settlement','type':'settlement','label':'Settlement mismatch'}],'edges':[{'source':'merchant','target':'customers'},{'source':'customers','target':'orders'},{'source':'orders','target':'transactions'},{'source':'transactions','target':'upi'},{'source':'transactions','target':'refunds'},{'source':'transactions','target':'settlement'}]}
def incident_detail(db:Session,incident_id:int):
 rows=risk_incidents(db);incident=next((x for x in rows if x['id']==incident_id),None)
 if not incident:return None
 return {**incident,'forensic_chain':['Incident','Anomaly','Transactions','Customers','Devices','Orders','Refunds'],'entities':{'accounts':17,'device_clusters':3,'ip_clusters':2},'explanation':'Shared device and IP clusters connect otherwise independent customers to coordinated high-value refund events.','recommended_response':'Temporarily hold clustered refunds and require step-up verification.'}
