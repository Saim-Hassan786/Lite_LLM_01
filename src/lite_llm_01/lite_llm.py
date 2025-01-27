from litellm import completion
import os
os.environ["GEMINI_API_KEY"] = "AIzaSyBQFvTd1PBHg0i9s7UjNDCU9us_TK5IwMw"

def gemini_15():
    messages = [{"role":"user","content":"Tell Me About Yourself in 2 lines"}]
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages = messages,
        temperature = 0
    )
    print(response["choices"][0]["message"]["content"])


def gemini_20():
    messages = [{"role":"user","content":"Tell Me About Yourself in 2 lines"}]
    response= completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=messages,
        temperature = 0
    )
    print(response["choices"][0]["message"]["content"])


