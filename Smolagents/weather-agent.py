import requests
from smolagents import CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool, LiteLLMModel, PythonInterpreterTool, tool
from typing import Optional
import os

from dotenv import load_dotenv
load_dotenv()

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash",
                     api_key=os.getenv("GEMINI_API_KEY"))

search_tool = DuckDuckGoSearchTool()


@tool
def get_weather(latitude: float, longitude: float) -> str:
    """
    This is a publically available API that returns the weather for a given location
    Args:
        latitude: the latitude of the location
        longitude: the longitude of the location
    """
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        )
    data = response.json()
    return data["current"]

agent = CodeAgent(
    tools=[get_weather, search_tool],
    model=model,
    additional_authorized_imports=["requests", "json", "bs4"]
)

answer = agent.run("What is the weather in Tokyo?")
print(answer)