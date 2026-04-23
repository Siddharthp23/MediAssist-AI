from groq import Groq
from app.core.config import GROQ_API_KEY
from app.prompts.templates import PLAN_PROMPT
from app.agents.planner_agent import PlannerAgent

client = Groq(api_key=GROQ_API_KEY)

agent = PlannerAgent()

def generate_plan(input_text: str):
    # Step 1: Agent reasoning
    steps = agent.decompose(input_text)

    # Step 2: LLM enhancement
    prompt = PLAN_PROMPT.format(input_text=input_text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    llm_plan = response.choices[0].message.content

    return {
        "agent_steps": steps,
        "final_plan": llm_plan
    }