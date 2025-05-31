from flask import Flask, request, jsonify
import uuid
import os

app = Flask(__name__)

@app.route('/generate-stl', methods=['POST'])
def generate_stl():
    data = request.get_json()
    prompt = data.get('prompt', 'default prompt')
    name = data.get('name', 'model')
    
    # Simula geração STL
    filename = f"{uuid.uuid4()}.stl"
    path = os.path.join("generated", filename)
    os.makedirs("generated", exist_ok=True)
    
    with open(path, "w") as f:
        f.write(f"solid {name}\nendsolid {name}")
    
    # Simule a URL real (depois será substituída por link do Google Drive)
    fake_url = f"https://yourdomain.com/stl/{filename}"
    return jsonify({"stl_url": fake_url, "preview_url": None})
