from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class ImageUrl(BaseModel):
    url: str


app = FastAPI()


@app.post("/collection")
async def analyze_image(item: ImageUrl, status_code=201):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", 
                     "text": "I use the term \"shelf unit\" to represent a group of \"shelves\". The image is of board games as well as board game expansions on a single shelf unit. Analyze the board games and expansions on the shelf unit using the following steps: "\
                     "1. Identify the model of shelf unit, if the model isn't identifiable default to IKEA kallax\n"\
                     "2. Identify the number of shelves inside of the shelf unit\n"\
                     "3. Identify which board games are on top of the shelf unit\n"\
                     "4. Identify which board games are on each individual shelf\n"\
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": item.url,
                        },
                    },
                ],
            }
        ]
    )

    return response.choices[0]