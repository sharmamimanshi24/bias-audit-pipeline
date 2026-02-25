from google import genai

client = genai.Client(api_key="AIzaSyA-vn4iVfHwe5JIk4uVzdRHee7Nx4t4ZLY")

for model in client.models.list():
    print(model.name)
