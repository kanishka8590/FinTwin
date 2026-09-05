from fastapi import APIRouter,Depends,Query
from pydantic import BaseModel,Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db
from models import Transaction
from services.financial import overview,simulate,investigate
from services.intelligence import risk_incidents,forecast,opportunities,graph,incident_detail
from agents.investigator import run as run_agent
from ml.analytics import anomaly_detection,customer_segmentation
router=APIRouter(prefix='/api')
class Scenario(BaseModel): payment_success:float=Field(94.8,ge=80,le=100); refund_rate:float=Field(2.7,ge=0,le=20)
class Question(BaseModel): question:str=Field(min_length=3,max_length=500)
@router.get('/health')
def health(): return {'status':'online','service':'FinTwin API'}
@router.get('/overview')
def get_overview(db:Session=Depends(get_db)): return overview(db)
@router.post('/investigations')
def create_investigation(payload:Question,db:Session=Depends(get_db)):
 result=investigate(db);result['question']=payload.question;result['agent_trace']=run_agent(db,payload.question);return result
@router.post('/simulations')
def create_simulation(payload:Scenario): return simulate(payload.payment_success,payload.refund_rate)
@router.get('/transactions')
def get_transactions(limit:int=Query(25,ge=1,le=100),db:Session=Depends(get_db)):
 rows=db.scalars(select(Transaction).order_by(Transaction.occurred_at.desc()).limit(limit)).all()
 return [{'id':x.external_id,'customer_id':x.customer_id,'amount':x.amount,'method':x.method,'status':x.status,'risk':x.risk,'occurred_at':x.occurred_at} for x in rows]
@router.get('/risk/incidents')
def get_incidents(db:Session=Depends(get_db)): return risk_incidents(db)
@router.get('/risk/incidents/{incident_id}')
def get_incident(incident_id:int,db:Session=Depends(get_db)):
 result=incident_detail(db,incident_id)
 if result is None: from fastapi import HTTPException; raise HTTPException(404,'Incident not found')
 return result
@router.get('/forecast')
def get_forecast(days:int=Query(30,ge=7,le=90),db:Session=Depends(get_db)): return forecast(db,days)
@router.get('/revenue/opportunities')
def get_opportunities(): return opportunities()
@router.get('/twin/graph')
def get_graph(): return graph()
@router.get('/analytics/anomalies')
def get_anomalies(db:Session=Depends(get_db)): return anomaly_detection(db)
@router.get('/analytics/segments')
def get_segments(db:Session=Depends(get_db)): return customer_segmentation(db)
