from flask import Flask, jsonify
from app.api.notes import notes_bp
from app.config.settings import DevelopmentConfig

app = Flask(__name__) 

@app.route("/")
def home():
    return jsonify(
        {
            "message": "Hello from Kubenotes!"
        }
    )

app.register_blueprint(notes_bp, url_prefix = "/api/notes")

if __name__ == "__main__":
    app.run(
        host = DevelopmentConfig.HOST,
        port = DevelopmentConfig.PORT,
        debug = DevelopmentConfig.DEBUG
    )