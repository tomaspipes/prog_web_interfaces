# Relatório de Projeto — Website Turístico de Almada

**Unidade Curricular:** Programação de Interfaces Web  
**Projeto:** Website Turístico do Município de Almada  
**Tecnologias:** Python · Flask · SQLite · HTML5 · CSS3 · JavaScript · Google Gemini · OpenRouter

---

## 1. Introdução

O projeto consiste no desenvolvimento de um website turístico dedicado ao município de Almada, em Portugal. A plataforma permite a visitantes e residentes explorar os pontos de interesse do concelho — praias, parques, miradouros, locais históricos, restaurantes e espaços culturais — de forma interactiva e visualmente apelativa.

A aplicação integra ainda **Inteligência Artificial** para geração automática de conteúdo turístico e classificação de pedidos de contacto, tirando partido da API Google Gemini com um mecanismo de fallback robusto.

---

## 2. Arquitectura Geral

A aplicação segue uma arquitectura **cliente-servidor (full-stack)** com separação clara entre frontend e backend:

```
┌─────────────────────────────────────┐
│         FRONTEND (Browser)          │
│   HTML5 + CSS3 + JavaScript puro    │
│                                     │
│  index.html  ←→  script.js          │
│  pages/lista/*.html                 │
│  pages/detalhe/*.html               │
└────────────────┬────────────────────┘
                 │  fetch() / REST API (HTTP)
                 │  porta 5001
┌────────────────▼────────────────────┐
│         BACKEND (Flask)             │
│   Python · Flask · SQLite           │
│                                     │
│  app.py  ←→  db.py                  │
│  ai.py   ←→  op_ai.py              │
│  init_db.py                         │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│         BASE DE DADOS               │
│   SQLite — almada.db                │
│   7 tabelas · 49 registos           │
└─────────────────────────────────────┘
```

---

## 3. Backend — API REST com Flask

### 3.1 Estrutura de ficheiros

| Ficheiro | Responsabilidade |
|---|---|
| `app.py` | Servidor Flask; define todos os endpoints REST |
| `db.py` | Abstracção de acesso à base de dados SQLite |
| `init_db.py` | Criação e população da base de dados (fonte única de verdade) |
| `ai.py` | Integração com Google Gemini |
| `op_ai.py` | Módulo de fallback via OpenRouter (Gemma 4) |

### 3.2 Endpoints disponíveis

| Endpoint | Método | Descrição |
|---|---|---|
| `/api/passear` | GET | Pontos de interesse gerais |
| `/api/praias` | GET | Praias do concelho (8 registos) |
| `/api/parques` | GET | Parques e jardins (3 registos) |
| `/api/miradouros` | GET | Miradouros (4 registos) |
| `/api/historicos` | GET | Locais históricos (5 registos) |
| `/api/comer` | GET | Restaurantes (14 registos) |
| `/api/cultura` | GET | Espaços culturais (11 registos) |
| `/api/pontos` | GET | Alias para `/api/passear` |
| `/api/ai/guia` | POST | Gera mini-guia turístico com IA |
| `/api/ai/contacto` | POST | Classifica contacto e gera resposta automática |

### 3.3 Base de dados

A base de dados SQLite é gerida exclusivamente pelo ficheiro `init_db.py`, que funciona como **fonte única de verdade**: apagar e recriar o ficheiro `almada.db` com `python3 init_db.py` restaura o estado completo da aplicação.

```python
# init_db.py — exemplo de registo na tabela comer
(1, "Escondidinho de Cacilhas", "peixe", "Restaurante de peixe",
 "Cacilhas", "Rua Cândido dos Reis, Cacilhas",
 "Restaurante familiar especializado em peixe fresco...",
 json.dumps(["Peixe fresco", "Vista para o Tejo"]),
 json.dumps(["Cais de Cacilhas"]),
 "imagens/comer/peixe/cacilhas-restaurantes.jpg")
```

Todas as imagens são referenciadas com caminhos relativos à raiz do `frontend/`, seguindo a convenção `imagens/<categoria>/<subcategoria>/<ficheiro>`.

---

## 4. Frontend — Single-Page Application (SPA)

### 4.1 O que é uma SPA neste contexto

Embora o projecto não utilize um framework como React ou Vue, existem dois pontos onde o comportamento SPA é implementado:

**Página principal (`index.html`)** — comporta-se como uma SPA parcial: todo o conteúdo dinâmico (cards, filtros, detalhes) é carregado via `fetch()` sem recarregar a página. A navegação entre secções é feita por **âncoras HTML** (`#passear`, `#comer`, etc.), e a navegação para páginas de detalhe utiliza **query strings** (`?id=3`) para identificar o registo a carregar.

**Página dedicada (`pontos.html`)** — implementa o modelo SPA na totalidade: carrega todos os 6 endpoints da API em paralelo com `Promise.all`, permite filtrar por categoria sem qualquer recarregamento, e apresenta um painel de detalhe inline (overlay) ao clicar num card, também sem navegação. O overlay suporta fecho por botão, clique fora ou tecla `Escape`. Inclui ainda um contador dinâmico de resultados e campo de pesquisa em tempo real.

### 4.2 Detecção automática de profundidade de caminho

Um dos pontos críticos da arquitectura frontend é a detecção automática do caminho base, necessária porque o mesmo ficheiro `script.js` é partilhado por páginas em diferentes níveis de directório:

```javascript
// script.js — linhas 5-11
const PATH_PREFIX = (() => {
    const path = window.location.pathname;
    if (path.includes("/pages/lista/") || path.includes("/pages/detalhe/")) return "../../";
    return "";
})();

const DETALHE = PATH_PREFIX + "pages/detalhe/";
const LISTA   = PATH_PREFIX + "pages/lista/";
```

Desta forma, tanto `index.html` (raiz) como `pages/lista/praias.html` (dois níveis abaixo) conseguem construir URLs correctos para imagens e navegação sem configuração adicional.

### 4.3 Navegação activa com scroll

A barra de navegação lateral destaca automaticamente a secção visível no ecrã usando o evento `scroll` e `offsetTop`:

```javascript
// script.js — linhas 259-280
function atualizarLinkAtivo() {
    let secaoAtual = "";

    secoes.forEach(function (secao) {
        const topo = secao.offsetTop - 160;
        const altura = secao.offsetHeight;

        if (window.scrollY >= topo && window.scrollY < topo + altura) {
            secaoAtual = secao.getAttribute("id");
        }
    });

    linksMenu.forEach(function (link) {
        link.classList.remove("ativo");
        if (link.getAttribute("href") === `#${secaoAtual}`) {
            link.classList.add("ativo");
        }
    });
}

window.addEventListener("scroll", atualizarLinkAtivo);
```

### 4.4 Animação de entrada das secções

As secções entram com animação de fade-in ao tornarem-se visíveis, utilizando a **Intersection Observer API**:

```javascript
// script.js — linhas 285-301
const observer = new IntersectionObserver(
    function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add("visivel");
            }
        });
    },
    { threshold: 0.15 }
);

secoes.forEach(function (secao) {
    secao.classList.add("oculta");
    observer.observe(secao);
});
```

### 4.5 Carregamento de detalhes via query string

Cada página de detalhe lê o `id` da query string e carrega o registo correspondente da API:

```javascript
// Exemplo: pages/detalhe/praia.html
const params = new URLSearchParams(window.location.search);
const id = params.get("id");

fetch(API + "/api/praias")
    .then(res => res.json())
    .then(praias => {
        const praia = praias.find(p => String(p.id) === id);
        // renderizar conteúdo...
    });
```

### 4.6 Estrutura de páginas

```
frontend/
├── index.html                  ← Página principal (âncoras + fetch)
├── pontos.html                 ← SPA puro — todos os pontos com filtros inline
├── script-pontos.js            ← Lógica JS específica da página SPA
├── script.js                   ← Lógica partilhada (1536 linhas)
├── styles.css                  ← Estilos (1210 linhas)
├── audio/                      ← Playlist de fado e música portuguesa (.mp3, .m4a)
├── imagens/                    ← 49+ fotografias organizadas por categoria
└── pages/
    ├── lista/
    │   ├── praias.html
    │   ├── parques.html
    │   ├── miradouros.html
    │   ├── historicos.html
    │   ├── comer.html
    │   └── cultura.html
    └── detalhe/
        ├── praia.html
        ├── parque.html
        ├── miradouro.html
        ├── historico.html
        ├── restaurante.html
        └── espaco-cultural.html
```

---

## 5. Integração com Inteligência Artificial

### 5.1 Casos de uso

A IA está integrada em dois pontos distintos da aplicação:

1. **Mini-guia turístico** — em cada página de detalhe, o utilizador pode solicitar um guia gerado dinamicamente sobre aquele local específico.
2. **Resposta automática ao contacto** — após o envio do formulário de contacto, a IA analisa a mensagem e gera uma resposta personalizada.

### 5.2 Como activar o Gemini

A integração com o Google Gemini requer uma chave de API válida. Para a obter:

1. Aceder a [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Criar uma chave associada a um **novo projecto** (não reutilizar projectos existentes)
3. Criar o ficheiro `backend/.env` com o seguinte conteúdo:

```
GEMINI_API_KEY=A_SUA_CHAVE_AQUI
```

> **Nota importante:** O tier gratuito da API Gemini **não está disponível em países da UE/EEA**, incluindo Portugal, por razões de conformidade com o RGPD. Para contornar esta limitação existem duas opções:
> - Activar facturação no projecto Google Cloud (custo praticamente nulo para uso académico — cerca de €0,06 por 1 milhão de tokens)
> - Utilizar o mecanismo de fallback com OpenRouter (ver secção 5.4)

O cliente Gemini é inicializado de forma _lazy_ (apenas na primeira chamada):

```python
# ai.py — inicialização lazy do cliente
_client = None

def _get_client():
    global _client
    if _client is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY não definida no ambiente.")
        _client = genai.Client(api_key=api_key)
    return _client
```

### 5.3 Prompts de IA

O prompt do mini-guia instrui o modelo a estruturar a resposta com títulos Markdown (`##`), que são depois convertidos em HTML pelo frontend:

```python
# ai.py — prompt do mini-guia turístico
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
```

O frontend converte o Markdown da resposta em HTML:

```javascript
// script.js — conversão de Markdown para HTML
var html = data.guia
    .replace(/^## (.+)$/gm,    "<h2>$1</h2>")
    .replace(/^### (.+)$/gm,   "<h3>$1</h3>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n\n/g, "</p><p>")
    .replace(/\n/g,   "<br>");
aiResultado.innerHTML = "<p>" + html + "</p>";
```

### 5.4 Mecanismo de fallback (OpenRouter)

Para garantir resiliência quando o Gemini não está disponível, foi implementado um módulo alternativo (`op_ai.py`) que utiliza o serviço [OpenRouter](https://openrouter.ai) — que oferece acesso gratuito a vários modelos, incluindo Gemma 4 da Google.

A chave OpenRouter é configurada no mesmo ficheiro `.env`:

```
GEMINI_API_KEY=A_SUA_CHAVE_GEMINI
OPENROUTER_API_KEY=A_SUA_CHAVE_OPENROUTER
```

Para obter uma chave OpenRouter gratuita: [https://openrouter.ai](https://openrouter.ai) → Dashboard → API Keys → Create key. Não requer cartão de crédito.

O `app.py` orquestra o fallback de forma transparente:

```python
# app.py — fallback automático Gemini → OpenRouter
def gerar_guia(destino, tipo="destino"):
    try:
        return _gemini_guia(destino, tipo)   # tenta Gemini primeiro
    except Exception:
        return _op_ai.gerar_guia(destino, tipo)  # fallback OpenRouter
```

O `op_ai.py` tenta ainda múltiplos modelos em cascata, caso um esteja com _rate limit_:

```python
# op_ai.py — tentativa em cascata de modelos gratuitos
_MODELS = [
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
    "moonshotai/kimi-k2.6:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
]

for model in _MODELS:
    response = requests.post(...)
    if response.status_code == 429:
        continue   # rate limit — tenta o próximo
    return response.json()["choices"][0]["message"]["content"]
```

O fluxo completo é:

```
Pedido de IA
     │
     ▼
Gemini (Google) ──── OK ──────────────────► Resposta
     │
    FALHA (quota / chave inválida)
     │
     ▼
OpenRouter: gemma-4-31b ── OK ────────────► Resposta
     │
   429 (rate limit)
     │
     ▼
OpenRouter: gemma-4-26b ── OK ────────────► Resposta
     │
   ... (cascata)
```

---

## 6. Widget de Música

O painel lateral direito disponibiliza uma playlist de fado e música portuguesa relacionada com Almada. Os controlos incluem play/pause, faixa anterior/seguinte e volume.

Um ponto técnico relevante: os nomes dos ficheiros de áudio contêm caracteres acentuados e espaços (ex: `António Madeira - Isto É Almada.mp3`). Sem codificação, o browser não consegue resolver o URL. A solução é aplicar `encodeURI()` antes de atribuir o `src`:

```javascript
// script.js — codificação do caminho do áudio
function carregarMusica(index) {
    audio.src = encodeURI(playlist[index].src);
    trackName.textContent = playlist[index].nome;
}
```

---

## 7. Pontos Críticos do Código

### 7.1 `box-sizing: border-box` na navegação

Sem esta propriedade, o `padding` da `nav` é somado à `height: calc(100vh - 130px)`, empurrando o fundo da navegação para além do viewport e cortando o último item:

```css
/* styles.css — correcção crítica da navegação */
nav {
    height: calc(100vh - 130px);
    box-sizing: border-box; /* padding incluído na altura total */
    overflow-y: auto;
    padding: 28px 20px;
}
```

### 7.2 Limpeza da resposta JSON da IA

Os modelos de linguagem por vezes envolvem a resposta JSON em blocos de código Markdown (` ```json `). O backend limpa isto antes de devolver ao cliente:

```python
# app.py — limpeza da resposta do modelo
import re, json as _json

cleaned = re.sub(r"```(?:json)?\s*", "", raw).strip().rstrip("`").strip()

try:
    parsed = _json.loads(cleaned)
    resposta = parsed.get("resposta", cleaned)
except Exception:
    resposta = cleaned
```

### 7.3 Sincronização da base de dados com `init_db.py`

O script usa `INSERT OR REPLACE`, que apenas substitui linhas com IDs correspondentes. Registos com IDs não declarados no script persistem silenciosamente na base de dados. A solução é manter o `init_db.py` sempre sincronizado com o estado real da BD — qualquer novo registo adicionado directamente à BD deve ser imediatamente transposto para o script.

---

## 8. Como Executar o Projecto

### Pré-requisitos

```bash
pip install flask flask-cors google-genai python-dotenv requests
```

### Configuração

Criar o ficheiro `backend/.env`:

```
GEMINI_API_KEY=A_SUA_CHAVE_GEMINI
OPENROUTER_API_KEY=A_SUA_CHAVE_OPENROUTER
```

### Iniciar

```bash
# 1. Criar/recriar a base de dados
cd backend
python3 init_db.py

# 2. Iniciar o servidor Flask
python3 app.py
# API disponível em http://127.0.0.1:5001

# 3. Abrir o frontend
# Abrir frontend/index.html no browser
# ou usar um servidor local: python3 -m http.server 8080 (dentro de frontend/)
```

---

## 9. Conclusão

O projecto cumpre os objectivos propostos: uma aplicação web full-stack funcional, com conteúdo real sobre o município de Almada, navegação fluida com comportamento SPA, integração com IA generativa (Gemini) com fallback automático para OpenRouter, e uma experiência de utilizador cuidada com animações, filtros e música ambiente.

A arquitectura modular — backend REST separado do frontend estático, base de dados gerida por script declarativo, e módulos de IA independentes com estratégia de fallback em cascata — torna o projecto extensível e resiliente face a limitações externas como quotas de API.
