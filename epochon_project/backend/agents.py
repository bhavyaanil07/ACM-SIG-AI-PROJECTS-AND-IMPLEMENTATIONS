import os
import json
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- AGENT 1 : CASE ANALYZER ----------
def agent1_case_analysis(user_query: str):
    prompt = f"""
You are a legal analysis AI.
Analyze the following legal issue based on Indian law.
Return ONLY valid JSON.

User Query:
{user_query}

JSON Format:
{{
  "case_type": "",
  "summary": "",
  "possible_punishments": [],
  "severity": ""
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)


# ---------- AGENT 2 : RISK & SOLUTION ----------
def agent2_risk_strategy(case_data: dict):
    prompt = f"""
You are a legal risk advisor.
Use ONLY the following case data:

{json.dumps(case_data)}

Return ONLY valid JSON.

JSON Format:
{{
  "legal_risks": [],
  "recommended_actions": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)


# ---------- AGENT 3 : LAWYER RECOMMENDER ----------
def agent3_lawyer_selector(case_type: str):
    df = pd.read_csv("lawyers.csv")

    filtered = df[df["specialization"].str.contains(case_type, case=False)]

    if filtered.empty:
        filtered = df

    lawyer = filtered.sort_values(
        by="experience_years", ascending=False
    ).iloc[0]

    return {
        "name": lawyer["name"],
        "specialization": lawyer["specialization"],
        "experience_years": int(lawyer["experience_years"]),
        "contact": lawyer["contact"]
    }
