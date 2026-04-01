import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

# in python class names are in CamelCase: 
# non-class names (e.g. function/variable) are in snake_case: 
class Chat:
    client = Groq()
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "Write the output in 1-2 sentences"
            }
        ]
    def send_message(self, message):
        self.messages.append(
            {
                # system: never change; user: changes a lot 
                # the message that you are sending to the AI
                'role': 'user', 
                'content': message
            }
        )
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="llama-3.1-8b-instant",
        )
        result = chat_completion.choices[0].message.content
        self.messages.append({
            'role': 'assistant',
            'content': result
        })
        # tell LLM what we were previously talking about
        return result

# this makes the user interface nicer by saying 'chat>'
if __name__ == '__main__': 
    chat = Chat()
    try:
        while True: 
                user_input = input('chat>')
                response = chat.send_message(user_input)
                print(response)
    except KeyboardInterrupt:
        print()

