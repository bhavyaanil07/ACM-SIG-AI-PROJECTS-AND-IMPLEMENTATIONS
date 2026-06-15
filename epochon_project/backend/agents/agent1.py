from openai import OpenAI
client = OpenAI()

def agent1_analyze_case(user_query: str):
    prompt = f"""
    You are a legal case analyzer AI.
    Extract:
    - Charges
    - IPC sections
    - Punishments
    - Expected case duration
    - Severity
  
    Query: {user_query}
    """
    response = client.chat.completions.create(
        model="gpt-4.1", 
        messages=[{"role":"user", "content": prompt}]
    )
    return response.choices[0].message["content"]