from flask import Blueprint, jsonify as toJson, request
from application import chat_service
from uuid import uuid4


blueprint = Blueprint('chat', __name__)


@blueprint.route('/chats/<uuid:chat_id>', methods=['POST'])
def add_message(chat_id):
  user_message = request.get_json().get('message')
  ai_message = chat_service.send_user_message(chat_id, user_message)
  return toJson({'response': [ai_message]}), 200

@blueprint.route('/chats', methods=['POST'])
def create_chat():
  chat_id = uuid4()
  user_message = request.get_json().get('message')
  ai_message = chat_service.send_user_message(chat_id, user_message)
  return toJson({'response': [ai_message], 'chatId': chat_id}), 200

@blueprint.route('/chats', methods=['GET'])
def get_all_chats():
  chats = chat_service.list_chats()
  return toJson(chats)

@blueprint.route('/chats/<uuid:chat_id>', methods=['GET'])
def get_chat(chat_id):
  messages = chat_service.get_chat(chat_id)
  return toJson(messages)