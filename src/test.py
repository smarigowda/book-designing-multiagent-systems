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

poet = Agent(
  name="poet",
  description="Haiku poet.",
  instructions="You are a haiku poet.",
  model_client=client
)

# Test the poet
async def test_poet():
  response = await poet.run("Write a hiaku about blossoms in spring")
  print(f"Poet says: {response}")

asyncio.run(test_poet())


