from services.financial import simulate
from services.intelligence import opportunities,graph
def test_option_a_value(): assert simulate(99.8,2.7)['net_impact']==1240000
def test_priorities_are_sorted():
 rows=opportunities();assert rows[0]['priority_score']>=rows[-1]['priority_score']
def test_twin_has_connections(): assert len(graph()['edges'])>=5
