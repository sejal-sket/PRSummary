from flask import Flask, render_template
from app.routes import bp

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.register_blueprint(bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
