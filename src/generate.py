import os
import openai
from dotenv import load_dotenv

def main():
    openai.api_key = os.getenv("API_KEY")

    work = "Bust of Caracalla"
    museum = "the Museo Nazionale Romano"

    desc = 'The following is a conversation about %s in %s. The questioner asks the respondent for his/her impression of the work\n'.format(work, museum)
    q1 = 'Question: What is your first impression of this work?\n'
    a1 = 'Answer: My first impression is that it is very finely and realistically carved.\n'
    q2 = 'Question:'
    prompt = desc + q1 + a1 + q2

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        frequency_penalty=0.2,
        presence_penalty=0,
        echo=True,
    )

    try:
        print(response.choices[0].text)
    except:
        print("error occured: reason ", response.choices[0].finish_reason)

if __name__ == '__main__':
    load_dotenv()
    main()