"""Deterministic analytics used by the FinTwin services."""
def simulate(payment_success:float,refund_rate:float)->dict:
    impact=(payment_success-94.8)*2.48-(refund_rate-2.7)*.8
    return {'net_impact_lakh':round(impact,2),'revenue_crore':round(2.84+impact/100,3)}
def investigate()->dict:
    return {'root_cause':'UPI payment routing degraded during evening peak','success_before':96.1,'success_after':88.4,'affected':2841,'at_risk_lakh':4.2,'confidence':.91}
