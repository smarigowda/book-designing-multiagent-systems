import asyncio
from picoagents import Agent
from picoagents.orchestration import RoundRobinOrchestrator
from picoagents.termination import MaxMessageTermination, TextMentionTermination
from picoagents.llm import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

client = OpenAIChatCompletionClient(
  model="gpt-4.1-mini",
  api_key=os.getenv("OPENAI_API_KEY")
)

# Create a haiku poet
poet = Agent(
  name="poet",
  description="Haiku poet.",
  instructions="You are a haiku poet.",
  model_client=client
)

# Create a poetry critic
critic = Agent(
  name="critic",
  description="Poet Critic who provides constructive feedback on haikus.",
  instructions="You are a haiku critic. \
    When you see a haiku, provide 2-3 specific, actionable \
    suggestions for improvement. Be constructive and brief. \
    If satisfied with the haiku, respond with 'APPROVED'",
    model_client=client
)

termination = (MaxMessageTermination(max_messages=8)) | TextMentionTermination(text="APPROVED")
orchestrator = RoundRobinOrchestrator(agents=[poet, critic], termination=termination, max_iterations=4)

# Run orchestration
async def run_orchestration():
  task = "Write a haiku about cherry blossoms in spring"
  stream = orchestrator.run_stream(task)
  async for message in stream:
    print(f"{message}")

asyncio.run(run_orchestration())

