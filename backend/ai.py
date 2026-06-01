import os
from google import genai
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

_client = None


def _get_client():
    global _client
    if _client is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY não definida no ambiente.")
        _client = genai.Client(api_key=api_key)
    return _client


def gerar_guia(destino, tipo="destino"):
    """
    Gera um mini-guia turístico sobre um destino em Almada usando o Gemini.
    """
    prompt = (
        f"Gera um mini-guia turístico sobre «{destino}» em Almada, Portugal.\n"
        f"Tipo de local: {tipo}.\n\n"
        "Inclui as seguintes secções (usa títulos com ##):\n"
        "1. Breve introdução histórica\n"
        "2. O que ver e fazer\n"
        "3. Melhor época para visitar\n"
        "4. Dicas práticas (acessos, horários, preços aproximados)\n"
        "5. O que ver nas proximidades\n\n"
        "Responde em português de Portugal, com linguagem acessível mas informativa. "
        "Máximo 400 palavras."
    )

    client = _get_client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text
