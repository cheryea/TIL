from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

messages = [
    {"role": "system", "content": "너는 친절한 터미널 챗봇이야"}
]

print("터미널 챗봇 시작! 종료하려면 'exit' 입력")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("챗봇 종료")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=500
        )

        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})
        print("AI:", assistant_message)

    except Exception as e:
        print("⚠️ OpenAI API 오류 발생")
        print(e)
        break
