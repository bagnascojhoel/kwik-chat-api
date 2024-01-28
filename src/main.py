from flask import Flask
from flask_cors import CORS
from presentation.rest.chat import chat_blueprint
from presentation.static.swagger_ui import swagger_ui_blueprint

app = Flask("Kwik Chat API")

# Global config
CORS(app)

# Add blueprints
app.register_blueprint(chat_blueprint)
app.register_blueprint(swagger_ui_blueprint)
