import openai
openai.api_key = ""

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Que es Azure?"
        }
    ]
)

print(completion.choices[0].message)