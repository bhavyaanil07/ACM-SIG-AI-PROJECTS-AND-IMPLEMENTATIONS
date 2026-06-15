import os
from dotenv import load_dotenv

load_dotenv()

print("KEY VALUE:", os.getenv("OPENAI_API_KEY"))
print("KEY EXISTS:", os.getenv("OPENAI_API_KEY") is not None)
