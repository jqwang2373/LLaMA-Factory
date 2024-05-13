#sk-proj-XkpxY8JoIeo5MdvAVycOT3BlbkFJmcFB3uj7Xbm8WSGsFg2y

from openai import OpenAI
OpenAI.api_key= "sk-proj-XkpxY8JoIeo5MdvAVycOT3BlbkFJmcFB3uj7Xbm8WSGsFg2y"
client = OpenAI(api_key="sk-proj-XkpxY8JoIeo5MdvAVycOT3BlbkFJmcFB3uj7Xbm8WSGsFg2y")
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are an AI assistant helping a user with a programming question for PyChrono. Please provide complete code and chain of thought to help the user."},
    {"role": "user", "content": "Can you provide a complete PyChrono script to simulate a dynamical system?"}
  ]
)
'''

messages = [
    {"role": "system",
     "content": "You are an AI assistant helping a user with a programming question for PyChrono. Please provide complete code and chain of thought to help the user."},
    {"role": "user", "content": "Can you provide a complete PyChrono script to simulate a dynamical system?"}
]

response = completion = client.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  #response_format= { "type":"json_object" }
)

print(completion.choices[0].message.content)

response = completion.choices[0].message.content

# To save the entire conversation automatically
with open("chat_completion.txt", "w") as file:
    for message in completion['model']["messages"]:
        if message["role"] == "system":
            file.write("System: " + message["content"] + "\n")
        else:
            file.write("User: " + message["content"] + "\n")

    # Write the response
    file.write("Model: " + response + "\n")