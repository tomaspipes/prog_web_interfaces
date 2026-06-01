"""
Fallback AI module using OpenRouter (https://openrouter.ai).
Exposes the same interface as ai.py — gerar_guia() and classificar_contacto().

OpenRouter provides free access to several models (e.g. google/gemma-3-27b-it:free).
No billing required; sign up at https://openrouter.ai and generate a free API key.

Set OPENROUTER_API_KEY in backend/.env to activate this fallback.
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

_OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Tried in order — if one is rate-limited, the next is attempted
_MODELS = [
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
    "moonshotai/kimi-k2.6:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
]


def _call(prompt: str) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY não definida no ambiente.")

    last_error = None
    for model in _MODELS:
        try:
            response = requests.post(
                _OPENROUTER_URL,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=30,
            )
            if response.status_code == 429:
                last_error = f"{model} rate-limited"
                continue
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.HTTPError:
            last_error = f"{model} failed ({response.status_code})"
            continue

    raise RuntimeError(f"Todos os modelos falharam. Último erro: {last_error}")


def gerar_guia(destino: str, tipo: str = "destino") -> str:
    """Gera um mini-guia turístico sobre um destino em Almada."""
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
    return _call(prompt)


def classificar_contacto(tipo_pedido: str, mensagem: str) -> str:
    """Classifica o pedido de contacto e gera uma resposta automática."""
    prompt = (
        "És um assistente virtual do site turístico de Almada, Portugal.\n"
        "O utilizador enviou um pedido de contacto.\n\n"
        f"Tipo de pedido selecionado: {tipo_pedido}\n"
        f"Mensagem do utilizador: {mensagem}\n\n"
        "Faz o seguinte:\n"
        "1. Classifica a urgência do pedido (baixa, média, alta)\n"
        "2. Identifica o tema principal (ex: restauração, praias, transportes, cultura, acessibilidade, outro)\n"
        "3. Gera uma resposta automática personalizada e útil para o utilizador, "
        "com sugestões concretas relacionadas com Almada.\n\n"
        "Responde em JSON com os campos: urgencia, tema, resposta.\n"
        "A resposta deve ser em português de Portugal, amigável e concisa (máx. 150 palavras)."
    )
    return _call(prompt)
