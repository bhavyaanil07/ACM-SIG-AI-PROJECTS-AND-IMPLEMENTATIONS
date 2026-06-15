from fastapi import FastAPI
from pydantic import BaseModel
from agents import (
    agent1_case_analysis,
    agent2_risk_strategy,
    agent3_lawyer_selector
)

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    # AGENT 1
    case_analysis = agent1_case_analysis(query.message)

    # AGENT 2
    risk_strategy = agent2_risk_strategy(case_analysis)

    # AGENT 3
    lawyer = agent3_lawyer_selector(case_analysis["case_type"])

    # FINAL AGGREGATION
    final_response = {
        "case_analysis": case_analysis,
        "risk_and_strategy": risk_strategy,
        "recommended_lawyer": lawyer,
        "disclaimer": "This response is for informational purposes only."
    }

    return final_response
