from smolagents import CodeAgent, HfApiModel, GradioUI
from dotenv import load_dotenv

load_dotenv()

deepseek_qwen_32B = 'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B'
qwen_2_5__coder_32B = 'Qwen/Qwen2.5-Coder-32B-Instruct'
qwen_2_5_72B = 'Qwen/Qwen2.5-72B-Instruct'
model = HfApiModel(qwen_2_5_72B)


# Create a basic agent with default tools
agent = CodeAgent(
    tools=[],  # Empty list for basic functionality
    model=model,
    add_base_tools=True  # Adds default toolbox: python interpreter, search, visit webpage
)

task = """
Check out these docs to understand how to use Deckset syntax to format slides:
https://docs.deckset.com/

And use that syntax to create me a slide deck in markdown.

I want to create a presentation about AI agents.

First, come up with the outline of the presentation, 10-12 slides.

Here are a few topics you can cover:

How we started with LLMS and could only send text there and get a response.
Then, how these LLMs got function calling.
And then, how LLMs were expanded by tools allowing them to go to the internet and do literally anything that can be done in code.

Then, we you got the outline, create the slides in markdown in Deckset format.
"""

agent.run(task)

# Launch the Gradio interface
# GradioUI(agent).launch()
