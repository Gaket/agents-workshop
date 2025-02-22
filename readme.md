This project contains two parts:

1. Smolagents example
2. Browser use example

Both of them are set up to use Gemini API.

To run the project, you need to set the `GEMINI_API_KEY` environment variable.

You can get the key from [here](https://aistudio.google.com/app/apikey).

Then, paste the key into the `.env` file in the root of the project, similarly to the `.env.example` file.

Steps to run the project:

1. Create a virtual environment

MacOs/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python weather-agent.py
```

```bash
python check_appointments.py
```

And don't forget to navigate to the respective project folder before running the commands!