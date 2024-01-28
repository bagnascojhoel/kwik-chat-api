from flask import Flask
from flask_cors import CORS
from presentation import chat_routes

app = Flask("Kwik Chat API")

# Global config
CORS(app)

# Add routes
app.register_blueprint(chat_routes.blueprint)

