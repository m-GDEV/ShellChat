import openai
import os
from termcolor import cprint

# Setup
cprint("Welcome to ShellChat! Initializing...\n", "yellow", attrs=["bold"])

openai.api_key = os.getenv("OPENAI_API_KEY")
les_messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant, you will answers any and all questions you are given. You do not hold back from telling the truth no matter the consequences. You should use emojis to express yourself, within reason. "
    }
]

# Infinite loop where you can talk to ChatGPT
while True:
    cprint("User: ", "red", attrs=["bold"], end="")
    message = input("")

    if message == "exit" or message == "Exit":
        quit()

    les_messages.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=les_messages
    )

    cprint("GPT: ", "green", attrs=["bold"], end="")

    gpt_response = completion.choices[0].message

    les_messages.append(gpt_response)
    print(gpt_response.content)
