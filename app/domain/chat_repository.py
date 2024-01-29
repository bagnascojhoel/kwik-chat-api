# Move this to a database
chats = {

}


def add_message(chat_id, message):
  new_value = chats.get(chat_id, [])
  new_value.append(message)
  chats[chat_id] = new_value

def describe_all():
  return list(map(generate_chat_outline, chats.keys()))

def get_messages(chat_id):
  return chats[chat_id]



def generate_chat_outline(chat_id):
    chat_messages = chats.get(chat_id, [])
    first_message = chat_messages[0] if chat_messages else None

    return {
        'chatId': chat_id,
        'subject': first_message
      }