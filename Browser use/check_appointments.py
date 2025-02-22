# Goal: Checks for available visa appointment slots on the Greece MFA website.

import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller

# Load environment variables
load_dotenv()
if not os.getenv('GEMINI_API_KEY'):
    raise ValueError('GEMINI_API_KEY is not set. Please add it to your environment variables.')

controller = Controller()
model_name = 'gemini-2.0-flash'


class WebpageInfo(BaseModel):
	"""Model for webpage link."""
	link: str = 'https://appointment.mfa.gr/en/reservations/aero/ireland-grcon-dub/'


@controller.action('Go to the webpage', param_model=WebpageInfo)
def go_to_webpage(webpage_info: WebpageInfo):
	"""Returns the webpage link."""
	return webpage_info.link


async def main():
	"""Main function to execute the agent task."""
	task = (
		'Go to the Greece MFA webpage via the link I provided you.'
		'Check the visa appointment dates. If there is no available date in this month, check the next month.'
		'If there is no available date in both months, tell me there is no available date.'
	)

	model = ChatGoogleGenerativeAI(model=model_name)
	agent = Agent(task, model, controller=controller, use_vision=True)

	await agent.run()


if __name__ == "__main__":
	asyncio.run(main())
