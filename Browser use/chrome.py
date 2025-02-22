import os
import sys
from datetime import datetime
from dotenv import load_dotenv

from browser_use.browser.browser import BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI


browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

load_dotenv()

linkedin_task = """Go to a list of connections using this link: https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=wJH&titleFreeText=Frontend%20Engineer&page=33.
		The goal is to connect to 6 people who have the green banner on their avatar.
        The green banner is always on the avatar, on the bottom left corner of the round picture.
		Send them a connection request without a message. Don't send Follow requests or messages.
		Do not ever scroll down, all you need is on the page and viewport you are on.
		If there are no people with the green banner on the page, just go to the next page.
		When you click on a Connect button in the list, there is always a confirmation popup, do not forget about it.
        Never withdraw an existing connection request.
        Connect to 6 people who have that green banner and finish.
		"""

facebook_task = """Go to Facebook Marketplace search page https://www.facebook.com/marketplace/toronto/search?query=macbook%20pro%2064
    Login with x_name and x_password if you need to.
	and find me the best deal for a Macbook Pro 64GB.
    Consider what's the CPU (M1/M2/M3 pro or max) and what's the storage (512GB/1TB/2TB/4TB).
    In your response, create a table with the CPU info, RAM and price.
	"""

daily_burn_research = """I'm interviewing at a company called Daily Burn. Find me the latest news on the company. Also, their values, team size, mission and stuff like that.
Bonus point for highlighting their current challenges and how they are doing. Your goal is to help me prepare for the interview by better understanding the company.
"""

linkedin_connect_live_task = """Behave like a human browsing LinkedIn. Open the feed. Like some posts that are about AI and Startups. Don't like anything about war or politics.
Then scroll, open some posts and read them. The goal is to Connect (not to follow!) to 12 people who have more than 2000 followers. Connect by coming to the person's profile from the feed.
If there is a Follow button on the page, click More and choose Connect from the dropdown.
In between of connecting, like a post or two. DO NOT withdraw existing connection requests! If there is a Pending button on the page, just ignore it and move forward.
"""

sensitive_data = {'x_name': 'youremail@test.com', 'x_password': 'yourPassword'} # feel free to extract to .env file

model_name: str = 'gemini-2.0-flash'
model = ChatGoogleGenerativeAI(model=model_name)

async def main():
	agent = Agent(
		task=linkedin_connect_live_task,
		llm=model,
		browser=browser,
		save_conversation_path='logs/conversation.log' + datetime.now().strftime('%Y%m%d_%H%M%S'),
		sensitive_data=sensitive_data,
	)

	await agent.run(max_steps=100)
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
