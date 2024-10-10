from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")

def home():
    return jsonify({"message": "Olá matrizes!"})

@app.route("/teste", methods=["GET"])
def teste():
    return jsonify({"status": "Lorem ipsum lorem lorem hihihi!"})

if __name__ == "__main__":
    app.run(debug=True)