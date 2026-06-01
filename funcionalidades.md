# Documento de Funcionalidades — Website Turístico de Almada

**Grupo Almada**

- 20241740 Tomás Pereira
- 50031111 Joao Santos
- 20241565 Gonçalo Oliveira
- 20241591 Rui Grosso

**Repositório GitHub:** https://github.com/tomaspipes/prog_web_interfaces

---

## API

- `GET /` — Verifica que a API está activa (`{"mensagem": "API Almada ativa"}`)
- `GET /api/passear` — Devolve todos os pontos de interesse gerais (4 registos)
- `GET /api/praias` — Devolve todas as praias do concelho (8 registos)
- `GET /api/parques` — Devolve todos os parques e jardins (3 registos)
- `GET /api/miradouros` — Devolve todos os miradouros (4 registos)
- `GET /api/historicos` — Devolve todos os locais históricos (5 registos)
- `GET /api/comer` — Devolve todos os restaurantes (14 registos)
- `GET /api/cultura` — Devolve todos os espaços culturais (11 registos)
- `POST /api/ai/guia` — Gera um mini-guia turístico com IA para um destino específico; recebe `{ "destino": "...", "tipo": "..." }`
- `POST /api/ai/contacto` — Classifica um pedido de contacto e gera uma resposta automática; recebe `{ "tipo_pedido": "...", "mensagem": "..." }`

---

## Página Principal (index.html)

### Navegação
- Barra lateral de navegação fixa com links para todas as secções da página
- Destaque automático do link da secção actualmente visível durante o scroll
- Índice no topo da página com âncoras para navegação rápida
- Botão "Voltar ao topo" que aparece ao fazer scroll para baixo

### Secção de Apresentação
- Texto introdutório sobre o município de Almada
- Imagem de destaque da cidade

### Secção de História
- Conteúdo dividido em quatro subsecções: origens, Almada medieval, património e rio, e Almada contemporânea

### Secção de Localização
- Mapa incorporado via Google Maps com a localização do município

### Secção de Freguesias
- Listagem das principais freguesias do concelho com descrição

### Secção Passear
- Cards de navegação para as quatro subcategorias: Praias, Parques e Jardins, Miradouros, Locais Históricos
- Cada card redireciona para a página de listagem correspondente

### Secção Comer
- Cards de navegação para três subcategorias: Restaurantes de peixe, Restaurantes tradicionais, Cafés e bares
- Os cards de subcategoria redirecionam para a página de listagem com filtro pré-aplicado por tipo

### Secção Cultura
- Cards de navegação para três subcategorias: Arte, Teatro e Eventos, Património e Museus
- Os cards de subcategoria redirecionam para a página de listagem com filtro pré-aplicado por tipo

### Secção Transportes
- Informação sobre os principais meios de transporte para e dentro de Almada (ferry, autocarro, metro sul do Tejo)

### Galeria
- Galeria fotográfica com imagens representativas do concelho organizadas por zonas

### Ligações Externas
- Lista de links úteis relacionados com Almada (Câmara Municipal, turismo, transportes, etc.)

### Formulário de Contacto
- Campo de nome com validação (obrigatório, mínimo 3 caracteres)
- Campo de e-mail com validação de formato
- Selector de tipo de pedido (informação, reclamação, sugestão, outro)
- Campo de mensagem com contador de caracteres em tempo real (máximo 300 caracteres)
- Validação completa do lado do cliente antes do envio
- Mensagem de sucesso após submissão válida
- Resposta automática gerada por IA (ver secção de IA abaixo)

### Animações
- Todas as secções entram com animação de fade-in ao tornarem-se visíveis (Intersection Observer API)

---

## Componente SPA (Single-Page Application)

### Página dedicada — `pontos.html`

A página `pontos.html` é a implementação central do modelo SPA. Acessível a partir da navegação principal como "Todos os Pontos (SPA)", agrega todos os pontos de interesse do concelho numa única página sem recarregamentos:

- **Carregamento paralelo de todas as categorias** — usa `Promise.all` para carregar os 6 endpoints da API em simultâneo; todos os dados ficam em memória
- **Filtros por categoria sem reload** — 7 botões (Todos, Praias, Parques, Miradouros, Históricos, Comer, Cultura) que filtram o DOM instantaneamente
- **Pesquisa em tempo real** — campo de texto que filtra por nome, descrição e tags enquanto o utilizador escreve
- **Contador dinâmico** — indica o número de resultados encontrados e actualiza em cada filtragem
- **Painel de detalhe inline (SPA)** — ao clicar num card, um overlay abre dentro da mesma página sem qualquer navegação; mostra imagem, nome, categoria, localização, descrição completa, tags e pontos próximos
- **Fecho do overlay** — por botão "×", clique fora do painel, ou tecla `Escape`
- **Animação de entrada** do painel de detalhe (`@keyframes spa-slide-in`)
- **Acessibilidade** — o card tem `role="button"` e `tabindex="0"` para navegação por teclado; o overlay tem `role="dialog"` e `aria-modal="true"`

### Comportamento SPA na página principal (`index.html`)

- **Navegação por âncoras** — toda a navegação é feita por `#section-id`, sem recarregamento da página
- **Detecção automática de profundidade de caminho** — o `script.js` calcula automaticamente o `PATH_PREFIX` conforme a localização do ficheiro HTML (raiz ou `pages/lista/` ou `pages/detalhe/`), garantindo que URLs funcionam correctamente em qualquer nível de directório
- **Carregamento dinâmico de conteúdo** — todos os cards são gerados via `fetch()` à API REST; não há dados estáticos no HTML
- **Destaque automático do link activo** — a barra lateral actualiza o link destacado em tempo real com base na secção visível durante o scroll

---

## Páginas de Listagem

Existem seis páginas de listagem, uma por categoria (`praias.html`, `parques.html`, `miradouros.html`, `historicos.html`, `comer.html`, `cultura.html`). Todas partilham as seguintes funcionalidades:

### Funcionalidades comuns
- Carregamento dinâmico de cards via API REST
- Campo de pesquisa por texto (filtra por nome em tempo real)
- Botão para limpar todos os filtros activos
- Botão "Voltar" para a página principal
- Mensagem de "sem resultados" quando nenhum item corresponde aos filtros

### Filtros específicos por categoria

**Praias**
- Filtro por acessibilidade (cadeira de rodas)
- Filtro por estacionamento disponível
- Filtro por restauração disponível
- Filtro por transportes públicos

**Parques**
- Filtro por acessibilidade
- Filtro adequado para famílias com crianças

**Miradouros**
- Filtro por acessibilidade
- Filtro por transportes públicos

**Locais Históricos**
- Filtro por acessibilidade
- Filtro por transportes públicos

**Restaurantes (Comer)**
- Filtro por tipo: peixe, tradicional, bar/esplanada
- Activação de filtro de tipo por URL (ao navegar da página principal pela subcategoria)

**Cultura**
- Filtro por tipo: arte, teatro/eventos, património
- Activação de filtro de tipo por URL (ao navegar da página principal pela subcategoria)

---

## Páginas de Detalhe

Existem seis páginas de detalhe (`praia.html`, `parque.html`, `miradouro.html`, `historico.html`, `restaurante.html`, `espaco-cultural.html`). Todas partilham:

- Imagem de destaque do local
- Nome, tipo, localização e morada
- Descrição completa
- Tags/etiquetas com características do local
- Lista de pontos de interesse próximos
- Botão "Ver no mapa" que abre o Google Maps com a localização
- Botão "Voltar" para a página de listagem correspondente
- Secção de mini-guia turístico gerado por IA (ver secção de IA)

---

## Utilização de APIs de IA

### Mini-guia turístico (páginas de detalhe)
- Botão "Gerar guia turístico" disponível em todas as páginas de detalhe
- Ao clicar, é enviado um pedido `POST /api/ai/guia` com o nome e tipo do local
- A IA gera um mini-guia estruturado com: introdução histórica, o que ver e fazer, melhor época para visitar, dicas práticas, e pontos de interesse próximos
- A resposta em Markdown é convertida para HTML e apresentada formatada na página
- O botão permite gerar um novo guia sem recarregar a página

### Resposta automática ao formulário de contacto
- Após submissão válida do formulário, é enviado um pedido `POST /api/ai/contacto`
- A IA analisa o tipo de pedido e a mensagem e gera uma resposta personalizada em português de Portugal
- A resposta é apresentada directamente na página, abaixo do formulário

### Arquitectura de fallback (resiliência)
- **Primário:** Google Gemini 2.0 Flash — modelo principal de geração de conteúdo
- **Fallback automático:** OpenRouter com Gemma 4 (31B) — activado automaticamente se o Gemini falhar por quota ou indisponibilidade
- **Cascata de modelos:** o fallback tenta até quatro modelos gratuitos em sequência antes de devolver erro
- A comutação entre primário e fallback é totalmente transparente para o utilizador

---

## Widget de Música Ambiente

- Painel lateral retrátil no canto inferior direito da página
- Playlist com cinco faixas de fado e música portuguesa relacionada com Almada
- Controlo de reprodução: play/pause, faixa anterior, faixa seguinte
- Controlo de volume deslizante
- Nome da faixa actual apresentado em tempo real
- Avanço automático para a próxima faixa no fim de cada música
- Volume inicial definido a 30% para não ser intrusivo

---

## Base de Dados e Conteúdo

- Base de dados SQLite com 7 tabelas e 49 registos no total
- Script `init_db.py` como fonte única de verdade — recria a base de dados completa com um único comando
- Conteúdo real sobre locais de Almada com moradas, descrições, tags, coordenadas e caminhos de imagem
- 49 fotografias organizadas por categoria em `frontend/imagens/`

---

## Aspectos Técnicos Adicionais

- **CORS** configurado no backend para permitir comunicação entre frontend e API em portos diferentes durante o desenvolvimento
- **Validação do lado do cliente** em todos os formulários, com mensagens de erro individuais por campo
- **Animações de entrada** em todas as secções da página principal (Intersection Observer API)
- **Codificação de URLs de áudio** (`encodeURI`) para suporte a nomes de ficheiros com caracteres especiais e espaços
- **`box-sizing: border-box`** na navegação para evitar corte de conteúdo com `calc(100vh)`
- **Responsive design** — layout adaptado para diferentes tamanhos de ecrã
- **Atributos `aria`** nos elementos interactivos do widget de áudio para acessibilidade básica
