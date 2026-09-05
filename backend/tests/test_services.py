from services.financial import simulate
def test_simulation_baseline(): assert simulate(94.8,2.7)['net_impact']==0
def test_simulation_payment_upside(): assert simulate(99.8,2.7)['net_impact']==1240000
