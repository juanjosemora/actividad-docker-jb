from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API activa y desplegada correctamente con CI/CD"})

if __name__ == '__main__':
    # nosec le indica a Bandit que valide este binding como seguro
    app.run(host='0.0.0.0', port=5000, debug=False)  # nosec