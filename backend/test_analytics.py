from analytics import simulate,investigate
def test_baseline_is_zero(): assert simulate(94.8,2.7)['net_impact_lakh']==0
def test_payment_improvement_positive(): assert simulate(99.8,2.7)['net_impact_lakh']==12.4
def test_investigation_is_evidenced(): assert investigate()['affected']==2841
