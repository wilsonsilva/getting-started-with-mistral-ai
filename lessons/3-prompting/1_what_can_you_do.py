from helper import load_mistral_api_key, mistral
load_mistral_api_key()

response = mistral("hello, what can you do?")

print(response)

# Hello! I can assist with a variety of tasks such as answering questions, setting reminders, providing information on
# weather, news, sports, and much more. I can also help with scheduling appointments, sending messages, and explaining
# concepts in a simple and understandable way. However, my capabilities are based on the functions provided by the
# platform I'm on. Is there a specific task or question you have in mind? I'd be happy to help!
