from flask import Flask, jsonify, request
from flask_cors import CORS
from db import query_db
from ai import gerar_guia as _gemini_guia, classificar_contacto as _gemini_contacto
import op_ai as _op_ai


def gerar_guia(destino, tipo="destino"):
    """Try Gemini first; fall back to OpenRouter if Gemini fails."""
    try:
        return _gemini_guia(destino, tipo)
    except Exception:
        return _op_ai.gerar_guia(destino, tipo)


def classificar_contacto(tipo_pedido, mensagem):
    """Try Gemini first; fall back to OpenRouter if Gemini fails."""
    try:
        return _gemini_contacto(tipo_pedido, mensagem)
    except Exception:
        return _op_ai.classificar_contacto(tipo_pedido, mensagem)

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


@app.route("/api/ai/contacto", methods=["POST"])
def contacto_ai():
    """Classifica pedido de contacto e gera resposta automática com IA."""
    dados = request.get_json()

    if not dados or "mensagem" not in dados:
        return jsonify({"erro": "Campo 'mensagem' é obrigatório."}), 400

    tipo_pedido = dados.get("tipo_pedido", "geral")
    mensagem = dados["mensagem"]

    try:
        raw = classificar_contacto(tipo_pedido, mensagem)

        # Strip ```json ... ``` or ``` ... ``` fences the model sometimes adds
        import re, json as _json
        cleaned = re.sub(r"```(?:json)?\s*", "", raw).strip().rstrip("`").strip()

        # Parse JSON and return only the 'resposta' field
        try:
            parsed = _json.loads(cleaned)
            resposta = parsed.get("resposta", cleaned)
        except Exception:
            resposta = cleaned

        return jsonify({"resultado": resposta})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
