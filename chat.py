import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

# in python class names are in CamelCase: 
# non-class names (e.g. function/variable) are in snake_case: 
class Chat:
    client = Groq()
    def __init__(self, message):
        self.messages = [
            {
                "role": "system",
                "content": "Write the output in 1-2 sentences"
            },
            {
                "role": "user",
                "content": message,
            }
        ]
    def send_message(self):
        self.messages.append(
            {
                'role': 'user', 
                'content': message
            }
        )
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="llama-3.1-8b-instant",
        )
        result = chat_completion.choices[0].message.content
        messages.append({
            'role': 'assistant',
            'content': result
        })
        # tell LLM what we were previously talking about
        return result

'''
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    # messages is the most important thing to modify
    messages=[
        {
            "role": "system",
            "content": "Write the output in 1-2 sentences"
        },
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="llama-3.1-8b-instant",
    # model is the second most important thing to modify 
    # tempting to always use the best model which is llama-3.3-70b-versatile 
    # but you should only use that for important work bc of usage limits
)
print(chat_completion.choices[0].message.content)
'''
