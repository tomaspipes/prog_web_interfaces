# prog_web_interfaces

Repositório da cadeira de **Programação de Interfaces Web**.

> 🚫 **Não é permitido fazer push direto para `master`.** Todo o trabalho deve ser submetido através de um Pull Request (PR). Vê as instruções abaixo.

---

## 📋 Índice

1. [Pré-requisitos](#1-pré-requisitos)
2. [Clonar o repositório](#2-clonar-o-repositório)
3. [Criar uma branch](#3-criar-uma-branch)
4. [Fazer alterações e commit](#4-fazer-alterações-e-commit)
5. [Enviar a branch para o GitHub](#5-enviar-a-branch-para-o-github)
6. [Criar um Pull Request (PR)](#6-criar-um-pull-request-pr)
7. [Regras do repositório](#7-regras-do-repositório)

---

## 1. Pré-requisitos

Antes de começar, garante que tens o Git instalado no teu computador.

- **Verificar se já está instalado** — abre o terminal e corre:
  ```bash
  git --version
  ```
  Se aparecer algo como `git version 2.x.x`, já está instalado.

- **Instalar Git** (caso não esteja):
  - macOS: `brew install git` ou descarrega em [git-scm.com](https://git-scm.com)
  - Windows: descarrega em [git-scm.com](https://git-scm.com) e segue o instalador
  - Linux: `sudo apt install git`

- **Configurar o teu nome e email** (só precisas fazer isto uma vez):
  ```bash
  git config --global user.name "O Teu Nome"
  git config --global user.email "o_teu_email@exemplo.com"
  ```

---

## 2. Clonar o repositório

"Clonar" significa fazer uma cópia do repositório no teu computador.

1. Abre o terminal na pasta onde queres guardar o projeto.
2. Corre o seguinte comando:

```bash
git clone https://github.com/tomaspipes/prog_web_interfaces.git
```

3. Entra na pasta criada:

```bash
cd prog_web_interfaces
```

> 💡 Só precisas de clonar **uma vez**. Da próxima vez, basta entrar na pasta e atualizar com `git pull`.

---

## 3. Criar uma branch

Uma **branch** é uma cópia isolada do projeto onde podes trabalhar sem afetar o código dos outros.

> 🚫 **Nunca trabalhes diretamente na `master`.**

1. Primeiro, garante que tens a versão mais recente da `master`:

```bash
git checkout master
git pull
```

2. Cria uma nova branch com o teu nome ou o nome do teu trabalho:

```bash
git checkout -b nome-do-teu-trabalho
```

Exemplos:
```bash
git checkout -b joao-trabalho1
git checkout -b maria-projeto-css
```

3. Confirma que estás na branch certa:

```bash
git branch
```
A branch ativa aparece com um `*` à frente.

---

## 4. Fazer alterações e commit

Depois de editares ou criares ficheiros, tens de os "guardar" no Git através de um **commit**.

1. Vê o estado dos teus ficheiros:

```bash
git status
```

2. Adiciona os ficheiros que queres incluir no commit:

```bash
# Adicionar um ficheiro específico:
git add nome-do-ficheiro.html

# Ou adicionar tudo de uma vez:
git add .
```

3. Cria o commit com uma mensagem descritiva:

```bash
git commit -m "Adiciona página inicial do Trabalho 1"
```

> 💡 A mensagem deve descrever **o que fizeste**, não "alterações" ou "update".

---

## 5. Enviar a branch para o GitHub

Depois de teres os teus commits, envia a branch para o GitHub:

```bash
git push origin nome-da-tua-branch
```

Exemplo:
```bash
git push origin joao-trabalho1
```

> Se for a primeira vez que envias esta branch, o Git pode sugerir o comando completo — basta copiá-lo e correr.

---

## 6. Criar um Pull Request (PR)

Um **Pull Request** é o pedido para integrar o teu trabalho na `master`. É assim que o teu trabalho é revisto e aceite.

1. Vai a [github.com/tomaspipes/prog_web_interfaces](https://github.com/tomaspipes/prog_web_interfaces)
2. Deverás ver um aviso amarelo com a tua branch e um botão **"Compare & pull request"** — clica nele.
   - Se não aparecer, vai ao separador **"Pull requests"** → **"New pull request"** → seleciona a tua branch.
3. Preenche:
   - **Título**: descreve o que submeteste (ex: `Trabalho 1 - João Silva`)
   - **Descrição**: podes adicionar notas relevantes
4. Clica em **"Create pull request"**.

Aguarda feedback. Podes continuar a fazer commits na mesma branch — o PR atualiza automaticamente.

---

## 7. Regras do repositório

| Regra | Porquê |
|-------|--------|
| 🚫 Não fazer push para `master` | Para não sobrescrever o trabalho dos outros |
| ✅ Criar sempre uma branch por trabalho/aluno | Mantém o histórico organizado |
| ✅ Commits com mensagens claras | Facilita perceber o que foi feito |
| ✅ Submeter via Pull Request | Permite revisão antes de integrar |

---

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

### 4. Configurar a chave da API (Gemini AI)

Cria o ficheiro `backend/.env` com a tua chave:

```bash
echo 'GEMINI_API_KEY=a_tua_chave_aqui' > backend/.env
```

> Podes obter uma chave gratuita em [ai.google.dev](https://ai.google.dev). Sem chave, a app funciona normalmente — apenas o botão de IA ficará indisponível.

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
│   ├── init_db.py          # Script de criação da BD
│   ├── almada.db           # Base de dados SQLite
│   ├── requirements.txt    # Dependências Python
│   └── .env                # Chave API (não versionar)
├── frontend/
│   ├── index.html          # Página principal
│   ├── styles.css          # Estilos (design acessível)
│   ├── script.js           # Lógica JS + filtros + IA
│   ├── *.html              # Páginas de detalhe
│   └── imagens/
│       ├── passear/        # praias, parques, miradouros, historicos
│       ├── comer/          # peixe, tradicionais, bares
│       ├── cultura/        # arte, teatro, patrimonio
│       └── geral/          # background, mapa
└── README.md
```

---

## ❓ Problemas comuns

**"Permission denied" ao fazer push**
→ Garante que tens acesso ao repositório. Fala com o responsável do repo.

**"Your branch is behind master"**
→ Corre `git pull origin master` para atualizar a tua branch com as últimas alterações.

**Esqueci-me de criar uma branch e fiz alterações na `master`**
→ Não entres em pânico. Corre:
```bash
git checkout -b nome-da-tua-branch
git push origin nome-da-tua-branch
```
As tuas alterações ficam guardadas na nova branch.


