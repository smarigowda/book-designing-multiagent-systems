import asyncio
from picoagents import Agent
from picoagents.llm import OpenAIChatCompletionClient
import os

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


