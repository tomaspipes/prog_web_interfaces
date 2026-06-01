# prog_web_interfaces

Repositório da cadeira de **Programação Web**.

Alunos:

- 20241740 Tomás Pereira
- 50031111 Joao Santos
- 20241565 Gonçalo Oliveira
- 20241591 Rui Grosso

## 🚀 Como correr a aplicação web (Almada)

### Pré-requisitos

- **Python 3.9+** instalado
- Um browser moderno (Chrome, Firefox, Safari)

### 1. Criar o ambiente virtual (só uma vez)

```bash
python3 -m venv venv
```

### 2. Ativar o ambiente virtual

```bash
# macOS / Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r backend/requirements.txt
```

### 4. Configurar as chaves de API

Cria o ficheiro `backend/.env` com as tuas chaves:

```
GEMINI_API_KEY=a_tua_chave_gemini_aqui
OPENROUTER_API_KEY=a_tua_chave_openrouter_aqui
```

Nao queremos API KEYS publicas, por isso o ficheiro `.env` foi
adicionado ao `.gitignore` para não ser versionado.

- **Gemini**: chave gratuita em [ai.google.dev](https://ai.google.dev). Atenção: utilizadores na UE/EEA precisam de ativar faturação no projeto Google Cloud (quota gratuita é 0 na UE).
- **OpenRouter** (fallback): chave gratuita em [openrouter.ai](https://openrouter.ai). Não requer cartão de crédito. Usada automaticamente se o Gemini falhar.

> Sem nenhuma das chaves, a app funciona normalmente — apenas as funcionalidades de IA ficam indisponíveis.

### 5. Inicializar a base de dados (só uma vez, ou para repor dados)

```bash
python backend/init_db.py
```

Isto cria o ficheiro `backend/almada.db` com todos os dados pré-carregados.

### 6. Arrancar o servidor Flask

```bash
python backend/app.py
```

O servidor arranca em `http://127.0.0.1:5001`.

### 7. Abrir o frontend

Abre o ficheiro `frontend/index.html` diretamente no browser, ou usa um servidor local:

```bash
# Opção simples com Python:
cd frontend
python3 -m http.server 8000
```

Depois abre [http://localhost:8000](http://localhost:8000) no browser.

### Estrutura do projeto

```
├── backend/
│   ├── app.py              # API Flask (porta 5001)
│   ├── db.py               # Helper SQLite
│   ├── ai.py               # Integração Gemini AI
│   ├── op_ai.py            # Integração OpenRouter AI (fallback)
│   ├── init_db.py          # Script de criação da BD
│   ├── almada.db           # Base de dados SQLite
│   ├── requirements.txt    # Dependências Python
│   └── .env                # Chave API (não versionar)
├── frontend/
│   ├── index.html          # Página principal
│   ├── pontos.html         # SPA — todos os pontos com filtros
│   ├── script-pontos.js    # Lógica JS específica da SPA
│   ├── styles.css          # Estilos (1210 linhas)
│   ├── script.js           # Lógica JS partilhada (1536 linhas)
│   ├── audio/              # Playlist de fado e música portuguesa
│   ├── imagens/
│   │   ├── passear/        # praias, parques, miradouros, historicos
│   │   ├── comer/          # peixe, tradicionais, bares
│   │   ├── cultura/        # arte, teatro, patrimonio
│   │   └── geral/          # background, mapa
│   └── pages/
│       ├── lista/          # praias, parques, miradouros, historicos, comer, cultura
│       └── detalhe/        # praia, parque, miradouro, historico, restaurante, espaco-cultural
├── funcionalidades.md      # Documento de funcionalidades
└── README.md
```

---
