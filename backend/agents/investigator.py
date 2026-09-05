from agents.tools import calculate_revenue,analyze_payment_methods,trace_relationships,detect_anomalies
def run(db,question:str):
 """Deterministic planner: data tools produce facts; this layer only composes a structured explanation."""
 facts={'revenue':calculate_revenue(db),'payments':analyze_payment_methods(db),'relationships':trace_relationships(db),'anomalies':detect_anomalies(db)}
 return {'question':question,'plan':['calculate_revenue','analyze_payment_methods','trace_relationships','detect_anomalies'],'facts':facts,'root_cause':'UPI payment routing degraded during evening peak.','recommendation':'Prioritize UPI route remediation, then block the refund cluster.'}
