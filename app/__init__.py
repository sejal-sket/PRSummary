from flask import Flask, render_template
from app.routes import review_bp

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.register_blueprint(review_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
