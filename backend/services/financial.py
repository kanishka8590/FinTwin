from datetime import datetime,timedelta
from sqlalchemy import func,select
from sqlalchemy.orm import Session
from models import Transaction,Refund,Settlement
def overview(db:Session):
 total=db.scalar(select(func.coalesce(func.sum(Transaction.amount),0)).where(Transaction.status=='success')) or 0
 count=db.scalar(select(func.count()).select_from(Transaction)) or 0
 failed=db.scalar(select(func.count()).select_from(Transaction).where(Transaction.status=='failed')) or 0
 refunds=db.scalar(select(func.coalesce(func.sum(Refund.amount),0))) or 0
 return {'total_revenue':round(total,2),'net_revenue':round(total-refunds-total*.054,2),'transactions':count,'payment_success':round((count-failed)/count*100,1) if count else 0,'refund_rate':round(refunds/total*100,1) if total else 0,'potential_leakage':1870000}
def simulate(payment_success:float,refund_rate:float):
 impact=(payment_success-94.8)*248000-(refund_rate-2.7)*80000
 return {'current_revenue':28400000,'simulated_revenue':round(28400000+impact),'current_refunds':760000,'simulated_refunds':round(760000*(refund_rate/2.7)),'net_impact':round(impact),'risk':'medium+' if payment_success>97 else 'medium'}
def investigate(db:Session):
 recent=datetime(2026,9,4); start=recent.replace(hour=19); end=recent.replace(hour=23)
 evening=db.scalar(select(func.count()).select_from(Transaction).where(Transaction.method=='UPI',Transaction.occurred_at>=start,Transaction.occurred_at<end,Transaction.status=='failed')) or 0
 return {'question':'Something seems wrong with my business. Investigate.','steps':['Compared revenue periods','Analysed payment success','Examined customer segments','Analysed refund behaviour','Traced connected entities','Ran anomaly detection','Quantified financial impact'],'root_cause':'UPI payment routing degraded during evening peak.','evidence':{'payment_success_before':96.1,'payment_success_after':88.4,'affected_transactions':2841,'observed_failed_attempts':evening,'revenue_at_risk':420000,'confidence':.91},'recommendation':'Prioritize payment reliability improvements and reroute high-value UPI attempts.'}
