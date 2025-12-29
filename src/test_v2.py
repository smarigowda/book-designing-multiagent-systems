import asyncio
from picoagents import Agent
from picoagents.llm import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

load_dotenv()

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

# Test the poet
async def test_poet():
  response = await poet.run("Write a hiaku about blossoms in spring")
  # print(f"Poet says: {response}")
  # print(dir(response))
  # print(response.messages)
  assistant_msg = response.messages[-1]
  print("Poet says:")
  print(assistant_msg.content)

async def test_critic():
  haiku = ("Cherry blossoms fall\n"
           "Petals dancing in spring breeze\n"
           "Nature's gentle song")
  response = await critic.run(f"Please critique this haiku: {haiku}")
  print(f"Critic says {response}")

asyncio.run(test_poet())
asyncio.run(test_critic())





