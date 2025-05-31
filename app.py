from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

# CORS completo com suporte a credentials e headers exigidos pela base44
CORS(app, resources={r"/generate": {"origins": [
    "https://app--3-d-creator-a326a441.base44.app"
]}}, supports_credentials=True)

@app.route("/generate", methods=["POST", "OPTIONS"])
def generate_model():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "https://app--3-d-creator-a326a441.base44.app")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST,OPTIONS")
        return response

    try:
        data = request.json
        print(f"Received data: {data}")

        # simulação de resposta real
        return jsonify({
            "stl_url": "https://example.com/model.stl",
            "preview_url": "https://example.com/preview.png"
        })
    except Exception as e:
        print("Erro:", str(e))
        return jsonify({"error": str(e)}), 500
