from flask import Flask
from app.routes import review_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(review_bp)

    return app
