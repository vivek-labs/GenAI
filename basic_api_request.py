from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Write a one-sentence bedtime story about a unicorn."
)
print(response.output_text)

'''completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= [{"role": "user",
           "content":"Compose a poem that explains the concept of recursion in programming."}]
)
print(completion.choices[0].message.content)
'''

