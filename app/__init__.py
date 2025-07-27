from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import summarize_bp
    app.register_blueprint(summarize_bp)

    return app
