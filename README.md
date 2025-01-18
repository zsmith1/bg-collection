# bg-collection
This is my playground for AI prompting, combined with my passion for board games. The long term goal is to be able to prompt a LLM (currently gpt-4o) to accurately identify all board games in a picture and automatically update an online collection (potentially on boardgamegeek.com)

## Dependencies
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [OpenAI API](https://platform.openai.com)

## Usage
- `poetry install`
- `poetry run fastapi dev main.py`
- `curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/collection" -d '{"url": {url of picture"}}'`
