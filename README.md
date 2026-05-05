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


