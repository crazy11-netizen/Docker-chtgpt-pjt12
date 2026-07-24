from flask import Flask

from models import init_app

from routes import register_routes

app = Flask(__name__)

app.config.from_pyfile("config.py")

init_app(app)

register_routes(app)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
