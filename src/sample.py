import os
import openai
from dotenv import load_dotenv

def main():
    openai.api_key = os.getenv("API_KEY")

    prompt = 'My favorite monster in Dragon Quest is'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        echo=True
    )

    print(response)

if __name__ == '__main__':
    load_dotenv()
    main()