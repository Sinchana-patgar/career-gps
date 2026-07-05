cd /Users/sinchanaapatgar/Documents/career-gps
cat > pages/Generate_Roadmap.py << 'EOF'
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("❌ OPENROUTER_API_KEY not found. Check Streamlit Cloud → Manage app → Settings → Secrets.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def generate_roadmap(user_info, goal):
    prompt = f"""
Act as a friendly and professional career roadmap mentor.
The student has the following background: {user_info}
Their career goal is: {goal}
Your job is to generate a **realistic and personalized** career roadmap to help the student reach their goal.
**Instructions**:
- Do NOT fix the roadmap to 8 weeks. Use your best judgment to decide how many weeks or phases are needed.
- For each week or phase, include:
  - A clear topic or goal
  - A short, engaging description
  - Links for learning resources
