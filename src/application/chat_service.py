from domain import chat_repository

def send_user_message(chat_id, message):
  chat_repository.add_message(chat_id, message)
  # send to LLM
  return 'default response'

def list_chats():
  return chat_repository.describe_all()

def get_chat(chat_id):
  return chat_repository.get_messages(chat_id)

