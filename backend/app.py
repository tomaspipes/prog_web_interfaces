from flask import Flask, jsonify, request
from flask_cors import CORS
from db import query_db
from ai import gerar_guia

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"mensagem": "API Almada ativa"})


@app.route("/api/passear")
def listar_passear():
    return jsonify(query_db("SELECT * FROM passear"))


@app.route("/api/comer")
def listar_comer():
    return jsonify(query_db("SELECT * FROM comer"))


@app.route("/api/cultura")
def listar_cultura():
    return jsonify(query_db("SELECT * FROM cultura"))


@app.route("/api/miradouros")
def listar_miradouros():
    return jsonify(query_db("SELECT * FROM miradouros"))


@app.route("/api/historicos")
def listar_historicos():
    return jsonify(query_db("SELECT * FROM historicos"))


@app.route("/api/praias")
def listar_praias():
    return jsonify(query_db("SELECT * FROM praias"))


@app.route("/api/parques")
def listar_parques():
    return jsonify(query_db("SELECT * FROM parques"))


@app.route("/api/pontos")
def listar_pontos():
    return listar_passear()


# ── Endpoint de Inteligência Artificial ──

@app.route("/api/ai/guia", methods=["POST"])
def guia_ai():
    """Gera um mini-guia turístico com IA (Google Gemini)."""
    dados = request.get_json()

    if not dados or "destino" not in dados:
        return jsonify({"erro": "Campo 'destino' é obrigatório."}), 400

    destino = dados["destino"]
    tipo = dados.get("tipo", "destino")

    try:
        texto = gerar_guia(destino, tipo)
        return jsonify({"destino": destino, "guia": texto})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
