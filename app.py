from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ⚠️ IMPORTANTE: Substitua pelo domínio real do seu app Base44
CORS(app, resources={r"/generate": {"origins": ["https://app--3-d-creator-a326a441.base44.app
"]}})

@app.route('/generate', methods=['POST'])
def generate_route():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        # Lógica da geração STL aqui...
        return jsonify({
            "stl_url": "https://exemplo.com/seu_modelo.stl",
            "preview_url": "https://exemplo.com/imagem.png"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
