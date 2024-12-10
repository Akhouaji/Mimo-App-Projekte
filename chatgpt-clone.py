import os
from pip._vendor import requests

api_key = os.getenv("MIMO_OPENAI_API_KEY")

url = "https://ai.mimo.org/v1/openai/message"
headers = {"api-key": api_key}
current_thread_id = None

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new thread for you.\n")

while True:
  user_message = input("You: ")
  if user_message == "exit":
    break
  elif user_message == "new":
    current_thread_id = None
    print("A new Thread is about to start")
    continue
  else:
    def send_message(user_message, current_thread_id):
      body = {
        "message" : user_message
      }
      if current_thread_id is not None:
        body["threadId"] = current_thread_id
      response = requests.post(url, json=body, headers=headers)
      response_data = response.json()
      return response_data
        
    response_data = send_message(user_message, current_thread_id)

    latest_message = response_data.get("response")
    current_thread_id = response_data.get("threadId")

    print(f"GPT: {latest_message}")

threads = []
if current_thread_id is not None and current_thread_id not in threads:
  threads.append(current_thread_id)
