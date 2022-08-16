import os
import openai
from dotenv import load_dotenv

def main():
    openai.api_key = os.getenv("API_KEY")

    desc = 'The following is a conversation with an AI assistant about Bust of Caracalla in the Museo Nazionale Romano. The assistant is helpful, creative, clever, and very friendly.\n'
    human1 = 'Human: What is your first impression of this work?\n'
    ai1 = 'AI: My first impression is that it is very finely and realistically carved.\n'
    human2 = 'Human:How about his eyebrows?\n'
    ai2 = 'AI:Eyebrows are drawn together to add intensity to the facial expression. It is not overly ornate and looks more like a military leader than a ruler.\n'
    human3 = 'Human:'
    prompt = desc + human1 + ai1 + human2 + ai2 + human3

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        frequency_penalty=0.2,
        presence_penalty=0,
    )

    print(response)

if __name__ == '__main__':
    load_dotenv()
    main()