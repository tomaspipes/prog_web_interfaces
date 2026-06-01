// Executa o código apenas depois de todo o HTML estar carregado
document.addEventListener("DOMContentLoaded", function () {

    /* ================= FORMULÁRIO DE CONTACTO ================= */

    // Seleção dos campos do formulário
    const form = document.getElementById("form-contacto");
    const nomeInput = document.getElementById("nome");
    const emailInput = document.getElementById("email");
    const tipoPedidoInput = document.getElementById("tipo-pedido");
    const mensagemInput = document.getElementById("mensagem");

    // Seleção das mensagens de erro e sucesso
    const erroNome = document.getElementById("erro-nome");
    const erroEmail = document.getElementById("erro-email");
    const erroMensagem = document.getElementById("erro-mensagem");
    const mensagemSucesso = document.getElementById("mensagem-sucesso");
    const contadorMensagem = document.getElementById("contador-mensagem");

    // Filtro
    let filtroAcessivel = false;
    let filtroEstacionamento = false;
    let filtroRestauracao = false;
    let filtroTransportes = false;

    // Mostra erro visual e textual num campo
    function mostrarErro(input, elementoErro, mensagem) {
        input.classList.add("erro-campo");
        input.classList.remove("valido");

        if (elementoErro) {
            elementoErro.textContent = mensagem;
        }
    }

    // Remove erro visual e textual de um campo
    function limparErro(input, elementoErro) {
        input.classList.remove("erro-campo");

        if (elementoErro) {
            elementoErro.textContent = "";
        }
    }

    // Marca campo como válido
    function marcarValido(input) {
        input.classList.remove("erro-campo");
        input.classList.add("valido");
    }

    // Validação do nome
    function validarNome() {
        const nome = nomeInput.value.trim();

        if (nome === "") {
            mostrarErro(nomeInput, erroNome, "O nome é obrigatório.");
            return false;
        }

        if (nome.length < 2) {
            mostrarErro(nomeInput, erroNome, "O nome deve ter pelo menos 2 caracteres.");
            return false;
        }

        limparErro(nomeInput, erroNome);
        marcarValido(nomeInput);
        return true;
    }

    // Validação do email
    function validarEmail() {
        const email = emailInput.value.trim();
        const padraoEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (email === "") {
            mostrarErro(emailInput, erroEmail, "O email é obrigatório.");
            return false;
        }

        if (!padraoEmail.test(email)) {
            mostrarErro(emailInput, erroEmail, "Introduz um email válido.");
            return false;
        }

        limparErro(emailInput, erroEmail);
        marcarValido(emailInput);
        return true;
    }

    // Validação do tipo de pedido
    function validarTipoPedido() {
        if (!tipoPedidoInput) {
            return true;
        }

        if (tipoPedidoInput.value === "") {
            tipoPedidoInput.classList.add("erro-campo");
            tipoPedidoInput.classList.remove("valido");
            return false;
        }

        tipoPedidoInput.classList.remove("erro-campo");
        tipoPedidoInput.classList.add("valido");
        return true;
    }

    // Validação da mensagem
    function validarMensagem() {
        const mensagem = mensagemInput.value.trim();

        if (mensagem === "") {
            mostrarErro(mensagemInput, erroMensagem, "A mensagem é obrigatória.");
            return false;
        }

        if (mensagem.length < 10) {
            mostrarErro(mensagemInput, erroMensagem, "A mensagem deve ter pelo menos 10 caracteres.");
            return false;
        }

        limparErro(mensagemInput, erroMensagem);
        marcarValido(mensagemInput);
        return true;
    }

    // Atualização do contador da mensagem
    function atualizarContador() {
        if (contadorMensagem && mensagemInput) {
            const total = mensagemInput.value.length;
            contadorMensagem.textContent = `${total} / 300`;
        }
    }

    // Eventos do formulário
    if (form) {
        nomeInput.addEventListener("input", validarNome);
        emailInput.addEventListener("input", validarEmail);

        if (tipoPedidoInput) {
            tipoPedidoInput.addEventListener("change", validarTipoPedido);
        }

        mensagemInput.addEventListener("input", function () {
            atualizarContador();
            validarMensagem();
        });

        // Submissão do formulário
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const nomeValido = validarNome();
            const emailValido = validarEmail();
            const tipoPedidoValido = validarTipoPedido();
            const mensagemValida = validarMensagem();

            if (nomeValido && emailValido && tipoPedidoValido && mensagemValida) {
                mensagemSucesso.textContent = "Pedido enviado com sucesso. Será preparado um resumo com base na informação indicada.";

                form.reset();

                nomeInput.classList.remove("valido");
                emailInput.classList.remove("valido");
                mensagemInput.classList.remove("valido");

                if (tipoPedidoInput) {
                    tipoPedidoInput.classList.remove("valido");
                }

                atualizarContador();
            } else {
                mensagemSucesso.textContent = "";
            }
        });
    }

    atualizarContador();

    /* ================= BOTÃO VOLTAR AO TOPO ================= */

    const backToTop = document.querySelector(".back-to-top");

    if (backToTop) {
        function controlarBotaoTopo() {
            if (window.scrollY > 300) {
                backToTop.classList.add("visivel");
            } else {
                backToTop.classList.remove("visivel");
            }
        }

        window.addEventListener("scroll", controlarBotaoTopo);
        controlarBotaoTopo();
    }

    /* ================= MENU ATIVO CONFORME SCROLL ================= */

    const secoes = document.querySelectorAll("main section");
    const linksMenu = document.querySelectorAll("nav a");

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
    atualizarLinkAtivo();

    /* ================= ANIMAÇÃO DAS SECÇÕES ================= */

    const observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visivel");
                }
            });
        },
        {
            threshold: 0.15
        }
    );

    secoes.forEach(function (secao) {
        secao.classList.add("oculta");
        observer.observe(secao);
    });

    /* ================= INTERAÇÃO COM O TÍTULO ================= */

    const titulo = document.querySelector("header h1");

    if (titulo) {
        titulo.addEventListener("click", function () {
            titulo.textContent = "Almada";
        });

        titulo.addEventListener("dblclick", function () {
            titulo.textContent = "Almada";
        });
    }

    /* ================= PLAYLIST DE ÁUDIO ================= */

    const audio = document.getElementById("bg-audio");
    const playPauseBtn = document.getElementById("play-pause-btn");
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");
    const volumeControl = document.getElementById("volume-control");
    const trackName = document.getElementById("track-name");
    const audioWidget = document.getElementById("audio-widget");
    const toggleWidgetBtn = document.getElementById("toggle-widget");

// Lista de músicas
    const playlist = [
        {
            nome: "António Madeira - Isto É Almada",
            src: "audio/António Madeira - Isto É Almada.mp3"
        },
        {
            nome: "António Madeira - Fado Cacilhas",
            src: "audio/António Madeira - Fado Cacilhas.mp3"
        },
        {
            nome: "António Madeira - Eu Sou Almada",
            src: "audio/António Madeira - Eu Sou Almada.mp3"
        },
        {
            nome: "António Madeira - Costa da Caparica",
            src: "audio/António Madeira - Costa da Caparica.mp3"
        },
        {
            nome: "Margem Sul",
            src: "audio/margem-sul.mp3"
        }
    ];

    let musicaAtual = 0;

// Carregar música
    function carregarMusica(index) {
        if (!audio || !trackName) return;

        audio.src = playlist[index].src;
        trackName.textContent = playlist[index].nome;
    }

// Próxima música
    function proximaMusica() {
        if (!audio) return;

        musicaAtual = (musicaAtual + 1) % playlist.length;
        carregarMusica(musicaAtual);
        audio.play();
    }

// Música anterior
    function musicaAnterior() {
        if (!audio) return;

        musicaAtual = (musicaAtual - 1 + playlist.length) % playlist.length;
        carregarMusica(musicaAtual);
        audio.play();
    }

// Inicializar
    if (audio) {
        carregarMusica(musicaAtual);
        audio.volume = 0.3;
    }

// Play / Pause
    if (audio && playPauseBtn) {
        playPauseBtn.addEventListener("click", function () {
            if (audio.paused) {
                audio.play();
                playPauseBtn.textContent = "⏸ Pausar";
            } else {
                audio.pause();
                playPauseBtn.textContent = "▶ Tocar";
            }
        });
    }

// Próxima
    if (nextBtn) {
        nextBtn.addEventListener("click", proximaMusica);
    }

// Anterior
    if (prevBtn) {
        prevBtn.addEventListener("click", musicaAnterior);
    }

// Quando música acaba → próxima automática
    if (audio) {
        audio.addEventListener("ended", proximaMusica);
    }

// Volume
    if (volumeControl) {
        volumeControl.addEventListener("input", function () {
            audio.volume = volumeControl.value;
        });
    }

    //Abri & Fechar aba
    if (audioWidget && toggleWidgetBtn) {
        toggleWidgetBtn.addEventListener("click", function () {
            const estaFechado = audioWidget.classList.toggle("fechado");
            toggleWidgetBtn.setAttribute("aria-expanded", String(!estaFechado));
        });
    }

    /* ================= CARREGAR PONTOS DA API ================= */

    function criarCard(ponto) {
        const card = document.createElement("article");
        card.classList.add("interesse-card");

        const tagsHTML = ponto.tags
            .map(function (tag) {
                return `<span class="tag">${tag}</span>`;
            })
            .join("");

        const locaisHTML = ponto.locais
            .map(function (local) {
                return `<li>${local}</li>`;
            })
            .join("");

        card.innerHTML = `
        <h3>${ponto.titulo}</h3>

        ${tagsHTML}

        <p>${ponto.descricao}</p>

        <ul>
            ${locaisHTML}
        </ul>

        <p><strong>Como chegar:</strong> ${ponto.como_chegar}</p>
    `;

        return card;
    }

    function carregarSecao(url, containerId) {
        fetch(url)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                const container = document.getElementById(containerId);

                if (!container) return;

                container.innerHTML = "";

                let dadosFiltrados = data;

                if (containerId === "lista-passear" && filtroAcessivel) {
                    dadosFiltrados = data.filter(item => item.acessivel === true);
                }

                dadosFiltrados.forEach(function (item) {
                    const card = criarCard(item);
                    container.appendChild(card);
                });
            })
            .catch(function (error) {
                console.error("Erro ao carregar secao:", error);
            });
    }

    carregarSecao("http://127.0.0.1:5001/api/passear", "lista-passear");



    /*Filtro*/
    const btnFiltro = document.getElementById("filtro-acessivel");
    const btnFiltroEstacionamento = document.getElementById("filtro-estacionamento");
    const btnFiltroRestauracao = document.getElementById("filtro-restauracao");
    const btnFiltroTransportes = document.getElementById("filtro-transportes");
    const inputPesquisa = document.getElementById("pesquisa-praia");
    const btnLimpar = document.getElementById("limpar-filtros");

    let termoPesquisa = "";

    if (inputPesquisa) {
        inputPesquisa.addEventListener("input", function () {
            termoPesquisa = this.value.toLowerCase();
            carregarPraias();
        });
    }

    if (btnFiltro) {
        btnFiltro.addEventListener("click", function () {
            filtroAcessivel = !filtroAcessivel;

            this.classList.toggle("ativo");

            btnFiltro.textContent = filtroAcessivel
                ? "Mostrar todos"
                : "Mostrar só acessíveis";

            if (document.getElementById("lista-praias")) {
                carregarPraias();
            } else {
                carregarSecao("http://127.0.0.1:5001/api/passear", "lista-passear");
            }
        });
    }

    if (btnFiltroEstacionamento) {
        btnFiltroEstacionamento.addEventListener("click", function () {
            filtroEstacionamento = !filtroEstacionamento;

            this.classList.toggle("ativo");

            btnFiltroEstacionamento.textContent = filtroEstacionamento
                ? "Mostrar todos"
                : "Com estacionamento";

            carregarPraias();
        });
    }

    if (btnFiltroRestauracao) {
        btnFiltroRestauracao.addEventListener("click", function () {
            filtroRestauracao = !filtroRestauracao;

            this.classList.toggle("ativo");

            btnFiltroRestauracao.textContent = filtroRestauracao
                ? "Mostrar todos"
                : "Com restauração";

            carregarPraias();
        });
    }

    if (btnFiltroTransportes) {
        btnFiltroTransportes.addEventListener("click", function () {
            filtroTransportes = !filtroTransportes;

            this.classList.toggle("ativo");

            btnFiltroTransportes.textContent = filtroTransportes
                ? "Mostrar todos"
                : "Com transportes";

            carregarPraias();
        });
    }

    if (btnLimpar) {
        btnLimpar.addEventListener("click", function () {

            // Reset estados
            filtroAcessivel = false;
            filtroEstacionamento = false;
            filtroRestauracao = false;
            filtroTransportes = false;
            termoPesquisa = "";

            // Reset input pesquisa
            if (inputPesquisa) {
                inputPesquisa.value = "";
            }

            // Remover estado visual dos botões
            btnFiltro?.classList.remove("ativo");
            btnFiltroEstacionamento?.classList.remove("ativo");
            btnFiltroRestauracao?.classList.remove("ativo");
            btnFiltroTransportes?.classList.remove("ativo");

            // Reset textos dos botões
            if (btnFiltro) btnFiltro.textContent = "Só acessíveis";
            if (btnFiltroEstacionamento) btnFiltroEstacionamento.textContent = "Com estacionamento";
            if (btnFiltroRestauracao) btnFiltroRestauracao.textContent = "Com restauração";
            if (btnFiltroTransportes) btnFiltroTransportes.textContent = "Com transportes";

            // Recarregar lista
            carregarPraias();
        });
    }

    /* Praias */

    function carregarPraias() {
        fetch("http://127.0.0.1:5001/api/praias")
            .then(function (res) {
                return res.json();
            })
            .then(function (data) {
                const container = document.getElementById("lista-praias");

                if (!container) return;

                container.innerHTML = "";

                let praiasFiltradas = data;

                if (filtroAcessivel) {
                    praiasFiltradas = praiasFiltradas.filter(function (praia) {
                        return praia.acessivel === true;
                    });
                }

                if (filtroEstacionamento) {
                    praiasFiltradas = praiasFiltradas.filter(function (praia) {
                        return praia.estacionamento === true;
                    });
                }

                if (filtroRestauracao) {
                    praiasFiltradas = praiasFiltradas.filter(function (praia) {
                        return praia.restauracao === true;
                    });
                }

                if (filtroTransportes) {
                    praiasFiltradas = praiasFiltradas.filter(function (praia) {
                        return praia.transportes === true;
                    });
                }

                if (termoPesquisa) {
                    praiasFiltradas = praiasFiltradas.filter(function (praia) {
                        return praia.nome.toLowerCase().includes(termoPesquisa);
                    });
                }

                if (praiasFiltradas.length === 0) {
                    container.innerHTML = `
                        <p class="sem-resultados">Não foram encontradas praias com os filtros selecionados.</p>
                    `;
                    return;
                }

                praiasFiltradas.forEach(function (praia) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card", "praia-card");

                    // torna o card clicável
                    card.style.cursor = "pointer";

                    card.addEventListener("click", function () {
                        window.location.href = `praia.html?id=${praia.id}`;
                    });
                    card.classList.add("interesse-card", "praia-card");

                    const idealParaHTML = praia.ideal_para
                        .map(function (item) {
                            return `<span class="tag">${item}</span>`;
                        })
                        .join("");

                    card.innerHTML = `
                    <img src="${praia.imagem}" alt="Imagem de ${praia.nome}" class="card-img">
                    <div class="acoes-card"> 
                        <button class="btn-detalhes">Ver detalhes</button> 
                    </div>

                    <h3>${praia.nome}</h3>

                    ${praia.acessivel ? '<span class="tag">Acessível</span>' : '<span class="tag tag-alerta">Acesso difícil</span>'}
                    ${praia.estacionamento ? '<span class="tag">Estacionamento</span>' : ''}
                    ${praia.restauracao ? '<span class="tag">Restauração</span>' : ''}
                    ${praia.transportes ? '<span class="tag">Transportes</span>' : ''}

                    <p>${praia.descricao}</p>

                    <p><strong>Zona:</strong> ${praia.zona}</p>
                    <p><strong>Localização:</strong> ${praia.localizacao}</p>
                    <p><strong>Tipo de mar:</strong> ${praia.tipo_mar}</p>

                    <ul>
                        <li><strong>Estacionamento:</strong> ${praia.estacionamento ? "Sim" : "Não"}</li>
                        <li><strong>Restauração:</strong> ${praia.restauracao ? "Sim" : "Não"}</li>
                        <li><strong>Transportes:</strong> ${praia.transportes ? "Sim" : "Limitado"}</li>
                    </ul>

                    <p><strong>Ideal para:</strong></p>
                    <div>${idealParaHTML}</div>
                `;
                    
                    card.querySelector(".btn-detalhes").addEventListener("click", function (e) {
                        e.stopPropagation(); // impede duplo trigger do card
                        window.location.href = `praia.html?id=${praia.id}`;
                    });

                    container.appendChild(card);
                });
            })
            .catch(function (error) {
                console.error("Erro ao carregar praias:", error);
            });
    }

    carregarPraias();

    /* ================= PARQUES ================= */

    let filtroParqueAcessivel = false;
    let filtroParqueFamilias = false;
    let termoPesquisaParque = "";

    const btnFiltroParqueAcessivel = document.getElementById("filtro-parque-acessivel");
    const btnFiltroParqueFamilias = document.getElementById("filtro-parque-familias");
    const btnLimparParques = document.getElementById("limpar-filtros-parques");
    const inputPesquisaParque = document.getElementById("pesquisa-parque");

    function carregarParques() {
        fetch("http://127.0.0.1:5001/api/parques")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const container = document.getElementById("lista-parques");
                if (!container) return;
                container.innerHTML = "";
                let filtrados = data;
                if (filtroParqueAcessivel) filtrados = filtrados.filter(p => p.acessivel === true);
                if (filtroParqueFamilias) filtrados = filtrados.filter(p => p.familias === true);
                if (termoPesquisaParque) filtrados = filtrados.filter(p => p.nome.toLowerCase().includes(termoPesquisaParque));
                if (filtrados.length === 0) { container.innerHTML = '<p class="sem-resultados">Nenhum resultado encontrado.</p>'; return; }
                filtrados.forEach(function(parque) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card");
                    card.style.cursor = "pointer";
                    card.addEventListener("click", function() { window.location.href = "parque.html?id=" + parque.id; });
                    const tagsHTML = (parque.ideal_para || []).map(t => `<span class="tag">${t}</span>`).join("");
                    card.innerHTML = `
                        <img src="${parque.imagem}" alt="Imagem de ${parque.nome}" class="card-img">
                        <div class="acoes-card"><button class="btn-detalhes">Ver detalhes</button></div>
                        <h3>${parque.nome}</h3>
                        ${parque.acessivel ? '<span class="tag">Acessível</span>' : '<span class="tag tag-alerta">Acesso difícil</span>'}
                        ${parque.familias ? '<span class="tag">Ideal para famílias</span>' : ''}
                        ${parque.transportes ? '<span class="tag">Transportes</span>' : ''}
                        <p>${parque.descricao}</p>
                        <p><strong>Zona:</strong> ${parque.zona}</p>
                        <p><strong>Ideal para:</strong></p>
                        <div>${tagsHTML}</div>
                    `;
                    card.querySelector(".btn-detalhes").addEventListener("click", function(e) {
                        e.stopPropagation();
                        window.location.href = "parque.html?id=" + parque.id;
                    });
                    container.appendChild(card);
                });
            })
            .catch(function(err) { console.error("Erro ao carregar parques:", err); });
    }

    if (inputPesquisaParque) {
        inputPesquisaParque.addEventListener("input", function() { termoPesquisaParque = this.value.toLowerCase(); carregarParques(); });
    }
    if (btnFiltroParqueAcessivel) {
        btnFiltroParqueAcessivel.addEventListener("click", function() {
            filtroParqueAcessivel = !filtroParqueAcessivel;
            this.classList.toggle("ativo");
            this.textContent = filtroParqueAcessivel ? "Mostrar todos" : "Só acessíveis";
            carregarParques();
        });
    }
    if (btnFiltroParqueFamilias) {
        btnFiltroParqueFamilias.addEventListener("click", function() {
            filtroParqueFamilias = !filtroParqueFamilias;
            this.classList.toggle("ativo");
            this.textContent = filtroParqueFamilias ? "Mostrar todos" : "Ideal para famílias";
            carregarParques();
        });
    }
    if (btnLimparParques) {
        btnLimparParques.addEventListener("click", function() {
            filtroParqueAcessivel = false; filtroParqueFamilias = false; termoPesquisaParque = "";
            if (inputPesquisaParque) inputPesquisaParque.value = "";
            btnFiltroParqueAcessivel?.classList.remove("ativo"); btnFiltroParqueFamilias?.classList.remove("ativo");
            if (btnFiltroParqueAcessivel) btnFiltroParqueAcessivel.textContent = "Só acessíveis";
            if (btnFiltroParqueFamilias) btnFiltroParqueFamilias.textContent = "Ideal para famílias";
            carregarParques();
        });
    }

    carregarParques();

    function carregarDetalheParque() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");
        const container = document.getElementById("detalhe-parque");
        const titulo = document.getElementById("titulo-parque");
        if (!container || !titulo) return;
        if (!id) { titulo.textContent = "Parque não encontrado"; container.innerHTML = "<p>Não foi indicado nenhum parque.</p>"; return; }
        fetch("http://127.0.0.1:5001/api/parques")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const parque = data.find(p => p.id == id);
                if (!parque) { titulo.textContent = "Parque não encontrado"; container.innerHTML = "<p>O parque selecionado não existe.</p>"; return; }
                titulo.textContent = parque.nome;
                const tagsHTML = (parque.ideal_para || []).map(t => `<span class="tag">${t}</span>`).join("");
                container.innerHTML = `
                    <img src="${parque.imagem}" class="detalhe-img" alt="Imagem de ${parque.nome}">
                    <p>${parque.descricao}</p>
                    <div class="detalhe-grid">
                        <div><strong>Zona:</strong> ${parque.zona}</div>
                        <div><strong>Localização:</strong> ${parque.localizacao}</div>
                        <div><strong>Tipo:</strong> ${parque.tipo}</div>
                        <div><strong>Acessibilidade:</strong> ${parque.acessivel ? "Acessível" : "Acesso mais difícil"}</div>
                        <div><strong>Famílias:</strong> ${parque.familias ? "Sim" : "Não"}</div>
                        <div><strong>Transportes:</strong> ${parque.transportes ? "Disponíveis" : "Limitados"}</div>
                        <div><strong>Estacionamento:</strong> ${parque.estacionamento ? "Disponível" : "Não indicado"}</div>
                    </div>
                    <p><strong>Ideal para:</strong></p>
                    <div>${tagsHTML}</div>
                    <div class="acoes-praia">
                        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(parque.nome + ' ' + parque.localizacao)}" target="_blank" class="btn-mapa">Ver no mapa</a>
                    </div>
                `;
            })
            .catch(function() { titulo.textContent = "Erro ao carregar"; container.innerHTML = "<p>Não foi possível carregar a informação.</p>"; });
    }

    carregarDetalheParque();

    /* ================= MIRADOUROS ================= */

    let filtroMiradouroAcessivel = false;
    let filtroMiradouroTransportes = false;
    let termoPesquisaMiradouro = "";

    const btnFiltroMiradouroAcessivel = document.getElementById("filtro-miradouro-acessivel");
    const btnFiltroMiradouroTransportes = document.getElementById("filtro-miradouro-transportes");
    const btnLimparMiradouros = document.getElementById("limpar-filtros-miradouros");
    const inputPesquisaMiradouro = document.getElementById("pesquisa-miradouro");

    function carregarMiradouros() {
        fetch("http://127.0.0.1:5001/api/miradouros")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const container = document.getElementById("lista-miradouros");
                if (!container) return;
                container.innerHTML = "";
                let filtrados = data;
                if (filtroMiradouroAcessivel) filtrados = filtrados.filter(m => m.acessivel === true);
                if (filtroMiradouroTransportes) filtrados = filtrados.filter(m => m.transportes === true);
                if (termoPesquisaMiradouro) filtrados = filtrados.filter(m => m.nome.toLowerCase().includes(termoPesquisaMiradouro));
                if (filtrados.length === 0) { container.innerHTML = '<p class="sem-resultados">Nenhum resultado encontrado.</p>'; return; }
                filtrados.forEach(function(miradouro) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card");
                    card.style.cursor = "pointer";
                    card.addEventListener("click", function() { window.location.href = "miradouro.html?id=" + miradouro.id; });
                    const tagsHTML = (miradouro.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                    card.innerHTML = `
                        <img src="${miradouro.imagem}" alt="Imagem de ${miradouro.nome}" class="card-img">
                        <div class="acoes-card"><button class="btn-detalhes">Ver detalhes</button></div>
                        <h3>${miradouro.nome}</h3>
                        ${miradouro.acessivel ? '<span class="tag">Acessível</span>' : '<span class="tag tag-alerta">Acesso difícil</span>'}
                        ${miradouro.transportes ? '<span class="tag">Transportes</span>' : ''}
                        <p>${miradouro.descricao}</p>
                        <p><strong>Zona:</strong> ${miradouro.zona}</p>
                        <div>${tagsHTML}</div>
                    `;
                    card.querySelector(".btn-detalhes").addEventListener("click", function(e) {
                        e.stopPropagation();
                        window.location.href = "miradouro.html?id=" + miradouro.id;
                    });
                    container.appendChild(card);
                });
            })
            .catch(function(err) { console.error("Erro ao carregar miradouros:", err); });
    }

    if (inputPesquisaMiradouro) {
        inputPesquisaMiradouro.addEventListener("input", function() { termoPesquisaMiradouro = this.value.toLowerCase(); carregarMiradouros(); });
    }
    if (btnFiltroMiradouroAcessivel) {
        btnFiltroMiradouroAcessivel.addEventListener("click", function() {
            filtroMiradouroAcessivel = !filtroMiradouroAcessivel;
            this.classList.toggle("ativo");
            this.textContent = filtroMiradouroAcessivel ? "Mostrar todos" : "Só acessíveis";
            carregarMiradouros();
        });
    }
    if (btnFiltroMiradouroTransportes) {
        btnFiltroMiradouroTransportes.addEventListener("click", function() {
            filtroMiradouroTransportes = !filtroMiradouroTransportes;
            this.classList.toggle("ativo");
            this.textContent = filtroMiradouroTransportes ? "Mostrar todos" : "Com transportes";
            carregarMiradouros();
        });
    }
    if (btnLimparMiradouros) {
        btnLimparMiradouros.addEventListener("click", function() {
            filtroMiradouroAcessivel = false; filtroMiradouroTransportes = false; termoPesquisaMiradouro = "";
            if (inputPesquisaMiradouro) inputPesquisaMiradouro.value = "";
            btnFiltroMiradouroAcessivel?.classList.remove("ativo"); btnFiltroMiradouroTransportes?.classList.remove("ativo");
            if (btnFiltroMiradouroAcessivel) btnFiltroMiradouroAcessivel.textContent = "Só acessíveis";
            if (btnFiltroMiradouroTransportes) btnFiltroMiradouroTransportes.textContent = "Com transportes";
            carregarMiradouros();
        });
    }

    carregarMiradouros();

    function carregarDetalheMiradouro() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");
        const container = document.getElementById("detalhe-miradouro");
        const titulo = document.getElementById("titulo-miradouro");
        if (!container || !titulo) return;
        if (!id) { titulo.textContent = "Miradouro não encontrado"; container.innerHTML = "<p>Não foi indicado nenhum miradouro.</p>"; return; }
        fetch("http://127.0.0.1:5001/api/miradouros")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const miradouro = data.find(m => m.id == id);
                if (!miradouro) { titulo.textContent = "Miradouro não encontrado"; container.innerHTML = "<p>O miradouro selecionado não existe.</p>"; return; }
                titulo.textContent = miradouro.nome;
                const tagsHTML = (miradouro.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                const idealHTML = (miradouro.ideal_para || []).map(t => `<span class="tag">${t}</span>`).join("");
                container.innerHTML = `
                    <img src="${miradouro.imagem}" class="detalhe-img" alt="Imagem de ${miradouro.nome}">
                    <p>${miradouro.descricao}</p>
                    <div class="detalhe-grid">
                        <div><strong>Zona:</strong> ${miradouro.zona}</div>
                        <div><strong>Localização:</strong> ${miradouro.localizacao}</div>
                        <div><strong>Acessibilidade:</strong> ${miradouro.acessivel ? "Acessível" : "Acesso mais difícil"}</div>
                        <div><strong>Transportes:</strong> ${miradouro.transportes ? "Disponíveis" : "Limitados"}</div>
                        <div><strong>Estacionamento:</strong> ${miradouro.estacionamento ? "Disponível" : "Não indicado"}</div>
                    </div>
                    <div>${tagsHTML}</div>
                    <p><strong>Ideal para:</strong></p>
                    <div>${idealHTML}</div>
                    <div class="acoes-praia">
                        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(miradouro.nome + ' ' + miradouro.localizacao)}" target="_blank" class="btn-mapa">Ver no mapa</a>
                    </div>
                `;
            })
            .catch(function() { titulo.textContent = "Erro ao carregar"; container.innerHTML = "<p>Não foi possível carregar a informação.</p>"; });
    }

    carregarDetalheMiradouro();

    /* ================= HISTÓRICOS ================= */

    let filtroHistoricoAcessivel = false;
    let filtroHistoricoTransportes = false;
    let termoPesquisaHistorico = "";

    const btnFiltroHistoricoAcessivel = document.getElementById("filtro-historico-acessivel");
    const btnFiltroHistoricoTransportes = document.getElementById("filtro-historico-transportes");
    const btnLimparHistoricos = document.getElementById("limpar-filtros-historicos");
    const inputPesquisaHistorico = document.getElementById("pesquisa-historico");

    function carregarHistoricos() {
        fetch("http://127.0.0.1:5001/api/historicos")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const container = document.getElementById("lista-historicos");
                if (!container) return;
                container.innerHTML = "";
                let filtrados = data;
                if (filtroHistoricoAcessivel) filtrados = filtrados.filter(h => h.acessivel === true);
                if (filtroHistoricoTransportes) filtrados = filtrados.filter(h => h.transportes === true);
                if (termoPesquisaHistorico) filtrados = filtrados.filter(h => h.nome.toLowerCase().includes(termoPesquisaHistorico));
                if (filtrados.length === 0) { container.innerHTML = '<p class="sem-resultados">Nenhum resultado encontrado.</p>'; return; }
                filtrados.forEach(function(historico) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card");
                    card.style.cursor = "pointer";
                    card.addEventListener("click", function() { window.location.href = "historico.html?id=" + historico.id; });
                    const tagsHTML = (historico.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                    card.innerHTML = `
                        <img src="${historico.imagem}" alt="Imagem de ${historico.nome}" class="card-img">
                        <div class="acoes-card"><button class="btn-detalhes">Ver detalhes</button></div>
                        <h3>${historico.nome}</h3>
                        ${historico.acessivel ? '<span class="tag">Acessível</span>' : '<span class="tag tag-alerta">Acesso difícil</span>'}
                        ${historico.transportes ? '<span class="tag">Transportes</span>' : ''}
                        <p>${historico.descricao}</p>
                        <p><strong>Zona:</strong> ${historico.zona}</p>
                        <div>${tagsHTML}</div>
                    `;
                    card.querySelector(".btn-detalhes").addEventListener("click", function(e) {
                        e.stopPropagation();
                        window.location.href = "historico.html?id=" + historico.id;
                    });
                    container.appendChild(card);
                });
            })
            .catch(function(err) { console.error("Erro ao carregar históricos:", err); });
    }

    if (inputPesquisaHistorico) {
        inputPesquisaHistorico.addEventListener("input", function() { termoPesquisaHistorico = this.value.toLowerCase(); carregarHistoricos(); });
    }
    if (btnFiltroHistoricoAcessivel) {
        btnFiltroHistoricoAcessivel.addEventListener("click", function() {
            filtroHistoricoAcessivel = !filtroHistoricoAcessivel;
            this.classList.toggle("ativo");
            this.textContent = filtroHistoricoAcessivel ? "Mostrar todos" : "Só acessíveis";
            carregarHistoricos();
        });
    }
    if (btnFiltroHistoricoTransportes) {
        btnFiltroHistoricoTransportes.addEventListener("click", function() {
            filtroHistoricoTransportes = !filtroHistoricoTransportes;
            this.classList.toggle("ativo");
            this.textContent = filtroHistoricoTransportes ? "Mostrar todos" : "Com transportes";
            carregarHistoricos();
        });
    }
    if (btnLimparHistoricos) {
        btnLimparHistoricos.addEventListener("click", function() {
            filtroHistoricoAcessivel = false; filtroHistoricoTransportes = false; termoPesquisaHistorico = "";
            if (inputPesquisaHistorico) inputPesquisaHistorico.value = "";
            btnFiltroHistoricoAcessivel?.classList.remove("ativo"); btnFiltroHistoricoTransportes?.classList.remove("ativo");
            if (btnFiltroHistoricoAcessivel) btnFiltroHistoricoAcessivel.textContent = "Só acessíveis";
            if (btnFiltroHistoricoTransportes) btnFiltroHistoricoTransportes.textContent = "Com transportes";
            carregarHistoricos();
        });
    }

    carregarHistoricos();

    function carregarDetalheHistorico() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");
        const container = document.getElementById("detalhe-historico");
        const titulo = document.getElementById("titulo-historico");
        if (!container || !titulo) return;
        if (!id) { titulo.textContent = "Local não encontrado"; container.innerHTML = "<p>Não foi indicado nenhum local.</p>"; return; }
        fetch("http://127.0.0.1:5001/api/historicos")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const historico = data.find(h => h.id == id);
                if (!historico) { titulo.textContent = "Local não encontrado"; container.innerHTML = "<p>O local selecionado não existe.</p>"; return; }
                titulo.textContent = historico.nome;
                const tagsHTML = (historico.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                const idealHTML = (historico.ideal_para || []).map(t => `<span class="tag">${t}</span>`).join("");
                container.innerHTML = `
                    <img src="${historico.imagem}" class="detalhe-img" alt="Imagem de ${historico.nome}">
                    <p>${historico.descricao}</p>
                    <div class="detalhe-grid">
                        <div><strong>Zona:</strong> ${historico.zona}</div>
                        <div><strong>Localização:</strong> ${historico.localizacao}</div>
                        <div><strong>Tipo:</strong> ${historico.tipo}</div>
                        <div><strong>Acessibilidade:</strong> ${historico.acessivel ? "Acessível" : "Acesso mais difícil"}</div>
                        <div><strong>Transportes:</strong> ${historico.transportes ? "Disponíveis" : "Limitados"}</div>
                    </div>
                    <div>${tagsHTML}</div>
                    <p><strong>Ideal para:</strong></p>
                    <div>${idealHTML}</div>
                    <div class="acoes-praia">
                        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(historico.nome + ' ' + historico.localizacao)}" target="_blank" class="btn-mapa">Ver no mapa</a>
                    </div>
                `;
            })
            .catch(function() { titulo.textContent = "Erro ao carregar"; container.innerHTML = "<p>Não foi possível carregar a informação.</p>"; });
    }

    carregarDetalheHistorico();

    /* ================= COMER ================= */

    let filtroComerPeixe = false;
    let filtroComerTradicional = false;
    let filtroComerBar = false;
    let termoPesquisaComer = "";

    const btnFiltroComerPeixe = document.getElementById("filtro-comer-peixe");
    const btnFiltroComerTradicional = document.getElementById("filtro-comer-tradicional");
    const btnFiltroComerBar = document.getElementById("filtro-comer-bar");
    const btnLimparComer = document.getElementById("limpar-filtros-comer");
    const inputPesquisaComer = document.getElementById("pesquisa-comer");

    function carregarComer() {
        fetch("http://127.0.0.1:5001/api/comer")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const container = document.getElementById("lista-comer");
                if (!container) return;
                container.innerHTML = "";
                let filtrados = data;
                if (filtroComerPeixe) filtrados = filtrados.filter(c => c.categoria === "peixe");
                if (filtroComerTradicional) filtrados = filtrados.filter(c => c.categoria === "tradicional");
                if (filtroComerBar) filtrados = filtrados.filter(c => c.categoria === "bar");
                if (termoPesquisaComer) filtrados = filtrados.filter(c => c.nome.toLowerCase().includes(termoPesquisaComer));
                if (filtrados.length === 0) { container.innerHTML = '<p class="sem-resultados">Nenhum resultado encontrado.</p>'; return; }
                filtrados.forEach(function(item) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card");
                    card.style.cursor = "pointer";
                    card.addEventListener("click", function() { window.location.href = "restaurante.html?id=" + item.id; });
                    const tagsHTML = (item.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                    card.innerHTML = `
                        <img src="${item.imagem}" alt="Imagem de ${item.nome}" class="card-img">
                        <div class="acoes-card"><button class="btn-detalhes">Ver detalhes</button></div>
                        <h3>${item.nome}</h3>
                        <p>${item.descricao}</p>
                        <p><strong>Zona:</strong> ${item.zona}</p>
                        <div>${tagsHTML}</div>
                    `;
                    card.querySelector(".btn-detalhes").addEventListener("click", function(e) {
                        e.stopPropagation();
                        window.location.href = "restaurante.html?id=" + item.id;
                    });
                    container.appendChild(card);
                });
            })
            .catch(function(err) { console.error("Erro ao carregar comer:", err); });
    }

    if (inputPesquisaComer) {
        inputPesquisaComer.addEventListener("input", function() { termoPesquisaComer = this.value.toLowerCase(); carregarComer(); });
    }
    if (btnFiltroComerPeixe) {
        btnFiltroComerPeixe.addEventListener("click", function() {
            filtroComerPeixe = !filtroComerPeixe; filtroComerTradicional = false; filtroComerBar = false;
            this.classList.toggle("ativo");
            btnFiltroComerTradicional?.classList.remove("ativo"); btnFiltroComerBar?.classList.remove("ativo");
            if (btnFiltroComerTradicional) btnFiltroComerTradicional.textContent = "Tradicional";
            if (btnFiltroComerBar) btnFiltroComerBar.textContent = "Bares e cafés";
            this.textContent = filtroComerPeixe ? "Mostrar todos" : "Peixe e marisco";
            carregarComer();
        });
    }
    if (btnFiltroComerTradicional) {
        btnFiltroComerTradicional.addEventListener("click", function() {
            filtroComerTradicional = !filtroComerTradicional; filtroComerPeixe = false; filtroComerBar = false;
            this.classList.toggle("ativo");
            btnFiltroComerPeixe?.classList.remove("ativo"); btnFiltroComerBar?.classList.remove("ativo");
            if (btnFiltroComerPeixe) btnFiltroComerPeixe.textContent = "Peixe e marisco";
            if (btnFiltroComerBar) btnFiltroComerBar.textContent = "Bares e cafés";
            this.textContent = filtroComerTradicional ? "Mostrar todos" : "Tradicional";
            carregarComer();
        });
    }
    if (btnFiltroComerBar) {
        btnFiltroComerBar.addEventListener("click", function() {
            filtroComerBar = !filtroComerBar; filtroComerPeixe = false; filtroComerTradicional = false;
            this.classList.toggle("ativo");
            btnFiltroComerPeixe?.classList.remove("ativo"); btnFiltroComerTradicional?.classList.remove("ativo");
            if (btnFiltroComerPeixe) btnFiltroComerPeixe.textContent = "Peixe e marisco";
            if (btnFiltroComerTradicional) btnFiltroComerTradicional.textContent = "Tradicional";
            this.textContent = filtroComerBar ? "Mostrar todos" : "Bares e cafés";
            carregarComer();
        });
    }
    if (btnLimparComer) {
        btnLimparComer.addEventListener("click", function() {
            filtroComerPeixe = false; filtroComerTradicional = false; filtroComerBar = false; termoPesquisaComer = "";
            if (inputPesquisaComer) inputPesquisaComer.value = "";
            btnFiltroComerPeixe?.classList.remove("ativo"); btnFiltroComerTradicional?.classList.remove("ativo"); btnFiltroComerBar?.classList.remove("ativo");
            if (btnFiltroComerPeixe) btnFiltroComerPeixe.textContent = "Peixe e marisco";
            if (btnFiltroComerTradicional) btnFiltroComerTradicional.textContent = "Tradicional";
            if (btnFiltroComerBar) btnFiltroComerBar.textContent = "Bares e cafés";
            carregarComer();
        });
    }

    /* Auto-apply filter from URL param (e.g. comer.html?filtro=peixe) */
    var filtroComerURL = new URLSearchParams(window.location.search).get("filtro");
    if (filtroComerURL === "peixe") {
        filtroComerPeixe = true;
        if (btnFiltroComerPeixe) { btnFiltroComerPeixe.classList.add("ativo"); btnFiltroComerPeixe.textContent = "Mostrar todos"; }
    } else if (filtroComerURL === "tradicional") {
        filtroComerTradicional = true;
        if (btnFiltroComerTradicional) { btnFiltroComerTradicional.classList.add("ativo"); btnFiltroComerTradicional.textContent = "Mostrar todos"; }
    } else if (filtroComerURL === "bar") {
        filtroComerBar = true;
        if (btnFiltroComerBar) { btnFiltroComerBar.classList.add("ativo"); btnFiltroComerBar.textContent = "Mostrar todos"; }
    }

    carregarComer();

    function carregarDetalheRestaurante() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");
        const container = document.getElementById("detalhe-restaurante");
        const titulo = document.getElementById("titulo-restaurante");
        if (!container || !titulo) return;
        if (!id) { titulo.textContent = "Espaço não encontrado"; container.innerHTML = "<p>Não foi indicado nenhum espaço.</p>"; return; }
        fetch("http://127.0.0.1:5001/api/comer")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const item = data.find(c => c.id == id);
                if (!item) { titulo.textContent = "Espaço não encontrado"; container.innerHTML = "<p>O espaço selecionado não existe.</p>"; return; }
                titulo.textContent = item.nome;
                const tagsHTML = (item.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                const locaisHTML = (item.locais || []).map(l => `<li>${l}</li>`).join("");
                container.innerHTML = `
                    <img src="${item.imagem}" class="detalhe-img" alt="Imagem de ${item.nome}">
                    <p>${item.descricao}</p>
                    <div class="detalhe-grid">
                        <div><strong>Zona:</strong> ${item.zona}</div>
                        <div><strong>Localização:</strong> ${item.localizacao}</div>
                        <div><strong>Tipo:</strong> ${item.tipo}</div>
                    </div>
                    <div>${tagsHTML}</div>
                    ${locaisHTML.length > 0 ? `<p><strong>Locais de referência:</strong></p><ul>${locaisHTML}</ul>` : ""}
                    <div class="acoes-praia">
                        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.nome + ' ' + item.localizacao)}" target="_blank" class="btn-mapa">Ver no mapa</a>
                    </div>
                `;
            })
            .catch(function() { titulo.textContent = "Erro ao carregar"; container.innerHTML = "<p>Não foi possível carregar a informação.</p>"; });
    }

    carregarDetalheRestaurante();

    /* ================= CULTURA ================= */

    let filtroCulturaArte = false;
    let filtroCulturaTeatro = false;
    let filtroCulturaPatrimonio = false;
    let termoPesquisaCultura = "";

    const btnFiltroCulturaArte = document.getElementById("filtro-cultura-arte");
    const btnFiltroCulturaTeatro = document.getElementById("filtro-cultura-teatro");
    const btnFiltroCulturaPatrimonio = document.getElementById("filtro-cultura-patrimonio");
    const btnLimparCultura = document.getElementById("limpar-filtros-cultura");
    const inputPesquisaCultura = document.getElementById("pesquisa-cultura");

    function carregarCultura() {
        fetch("http://127.0.0.1:5001/api/cultura")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const container = document.getElementById("lista-cultura");
                if (!container) return;
                container.innerHTML = "";
                let filtrados = data;
                if (filtroCulturaArte) filtrados = filtrados.filter(c => c.categoria === "arte");
                if (filtroCulturaTeatro) filtrados = filtrados.filter(c => c.categoria === "teatro");
                if (filtroCulturaPatrimonio) filtrados = filtrados.filter(c => c.categoria === "patrimonio");
                if (termoPesquisaCultura) filtrados = filtrados.filter(c => c.nome.toLowerCase().includes(termoPesquisaCultura));
                if (filtrados.length === 0) { container.innerHTML = '<p class="sem-resultados">Nenhum resultado encontrado.</p>'; return; }
                filtrados.forEach(function(item) {
                    const card = document.createElement("article");
                    card.classList.add("interesse-card");
                    card.style.cursor = "pointer";
                    card.addEventListener("click", function() { window.location.href = "espaco-cultural.html?id=" + item.id; });
                    const tagsHTML = (item.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                    card.innerHTML = `
                        <img src="${item.imagem}" alt="Imagem de ${item.nome}" class="card-img">
                        <div class="acoes-card"><button class="btn-detalhes">Ver detalhes</button></div>
                        <h3>${item.nome}</h3>
                        <p>${item.descricao}</p>
                        <p><strong>Zona:</strong> ${item.zona}</p>
                        <div>${tagsHTML}</div>
                    `;
                    card.querySelector(".btn-detalhes").addEventListener("click", function(e) {
                        e.stopPropagation();
                        window.location.href = "espaco-cultural.html?id=" + item.id;
                    });
                    container.appendChild(card);
                });
            })
            .catch(function(err) { console.error("Erro ao carregar cultura:", err); });
    }

    if (inputPesquisaCultura) {
        inputPesquisaCultura.addEventListener("input", function() { termoPesquisaCultura = this.value.toLowerCase(); carregarCultura(); });
    }
    if (btnFiltroCulturaArte) {
        btnFiltroCulturaArte.addEventListener("click", function() {
            filtroCulturaArte = !filtroCulturaArte; filtroCulturaTeatro = false; filtroCulturaPatrimonio = false;
            this.classList.toggle("ativo");
            btnFiltroCulturaTeatro?.classList.remove("ativo"); btnFiltroCulturaPatrimonio?.classList.remove("ativo");
            if (btnFiltroCulturaTeatro) btnFiltroCulturaTeatro.textContent = "Teatro e eventos";
            if (btnFiltroCulturaPatrimonio) btnFiltroCulturaPatrimonio.textContent = "Património e museus";
            this.textContent = filtroCulturaArte ? "Mostrar todos" : "Arte";
            carregarCultura();
        });
    }
    if (btnFiltroCulturaTeatro) {
        btnFiltroCulturaTeatro.addEventListener("click", function() {
            filtroCulturaTeatro = !filtroCulturaTeatro; filtroCulturaArte = false; filtroCulturaPatrimonio = false;
            this.classList.toggle("ativo");
            btnFiltroCulturaArte?.classList.remove("ativo"); btnFiltroCulturaPatrimonio?.classList.remove("ativo");
            if (btnFiltroCulturaArte) btnFiltroCulturaArte.textContent = "Arte";
            if (btnFiltroCulturaPatrimonio) btnFiltroCulturaPatrimonio.textContent = "Património e museus";
            this.textContent = filtroCulturaTeatro ? "Mostrar todos" : "Teatro e eventos";
            carregarCultura();
        });
    }
    if (btnFiltroCulturaPatrimonio) {
        btnFiltroCulturaPatrimonio.addEventListener("click", function() {
            filtroCulturaPatrimonio = !filtroCulturaPatrimonio; filtroCulturaArte = false; filtroCulturaTeatro = false;
            this.classList.toggle("ativo");
            btnFiltroCulturaArte?.classList.remove("ativo"); btnFiltroCulturaTeatro?.classList.remove("ativo");
            if (btnFiltroCulturaArte) btnFiltroCulturaArte.textContent = "Arte";
            if (btnFiltroCulturaTeatro) btnFiltroCulturaTeatro.textContent = "Teatro e eventos";
            this.textContent = filtroCulturaPatrimonio ? "Mostrar todos" : "Património e museus";
            carregarCultura();
        });
    }
    if (btnLimparCultura) {
        btnLimparCultura.addEventListener("click", function() {
            filtroCulturaArte = false; filtroCulturaTeatro = false; filtroCulturaPatrimonio = false; termoPesquisaCultura = "";
            if (inputPesquisaCultura) inputPesquisaCultura.value = "";
            btnFiltroCulturaArte?.classList.remove("ativo"); btnFiltroCulturaTeatro?.classList.remove("ativo"); btnFiltroCulturaPatrimonio?.classList.remove("ativo");
            if (btnFiltroCulturaArte) btnFiltroCulturaArte.textContent = "Arte";
            if (btnFiltroCulturaTeatro) btnFiltroCulturaTeatro.textContent = "Teatro e eventos";
            if (btnFiltroCulturaPatrimonio) btnFiltroCulturaPatrimonio.textContent = "Património e museus";
            carregarCultura();
        });
    }

    /* Auto-apply filter from URL param (e.g. cultura.html?filtro=arte) */
    var filtroCulturaURL = new URLSearchParams(window.location.search).get("filtro");
    if (filtroCulturaURL === "arte") {
        filtroCulturaArte = true;
        if (btnFiltroCulturaArte) { btnFiltroCulturaArte.classList.add("ativo"); btnFiltroCulturaArte.textContent = "Mostrar todos"; }
    } else if (filtroCulturaURL === "teatro") {
        filtroCulturaTeatro = true;
        if (btnFiltroCulturaTeatro) { btnFiltroCulturaTeatro.classList.add("ativo"); btnFiltroCulturaTeatro.textContent = "Mostrar todos"; }
    } else if (filtroCulturaURL === "patrimonio") {
        filtroCulturaPatrimonio = true;
        if (btnFiltroCulturaPatrimonio) { btnFiltroCulturaPatrimonio.classList.add("ativo"); btnFiltroCulturaPatrimonio.textContent = "Mostrar todos"; }
    }

    carregarCultura();

    function carregarDetalheCultura() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");
        const container = document.getElementById("detalhe-cultura");
        const titulo = document.getElementById("titulo-cultura");
        if (!container || !titulo) return;
        if (!id) { titulo.textContent = "Espaço não encontrado"; container.innerHTML = "<p>Não foi indicado nenhum espaço.</p>"; return; }
        fetch("http://127.0.0.1:5001/api/cultura")
            .then(function(res) { return res.json(); })
            .then(function(data) {
                const item = data.find(c => c.id == id);
                if (!item) { titulo.textContent = "Espaço não encontrado"; container.innerHTML = "<p>O espaço selecionado não existe.</p>"; return; }
                titulo.textContent = item.nome;
                const tagsHTML = (item.tags || []).map(t => `<span class="tag">${t}</span>`).join("");
                const locaisHTML = (item.locais || []).map(l => `<li>${l}</li>`).join("");
                container.innerHTML = `
                    <img src="${item.imagem}" class="detalhe-img" alt="Imagem de ${item.nome}">
                    <p>${item.descricao}</p>
                    <div class="detalhe-grid">
                        <div><strong>Zona:</strong> ${item.zona}</div>
                        <div><strong>Localização:</strong> ${item.localizacao}</div>
                        <div><strong>Tipo:</strong> ${item.tipo}</div>
                    </div>
                    <div>${tagsHTML}</div>
                    ${locaisHTML.length > 0 ? `<p><strong>Locais:</strong></p><ul>${locaisHTML}</ul>` : ""}
                    <div class="acoes-praia">
                        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.nome + ' ' + item.localizacao)}" target="_blank" class="btn-mapa">Ver no mapa</a>
                    </div>
                `;
            })
            .catch(function() { titulo.textContent = "Erro ao carregar"; container.innerHTML = "<p>Não foi possível carregar a informação.</p>"; });
    }

    carregarDetalheCultura();

    function carregarDetalhePraia() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");

        const container = document.getElementById("detalhe-praia");
        const titulo = document.getElementById("titulo-praia");

        if (!container || !titulo) return;

        if (!id) {
            titulo.textContent = "Praia não encontrada";
            container.innerHTML = "<p>Não foi indicada nenhuma praia para mostrar.</p>";
            return;
        }

        fetch("http://127.0.0.1:5001/api/praias")
            .then(function (res) {
                return res.json();
            })
            .then(function (data) {
                const praia = data.find(function (p) {
                    return p.id == id;
                });

                if (!praia) {
                    titulo.textContent = "Praia não encontrada";
                    container.innerHTML = "<p>A praia selecionada não existe ou deixou de estar disponível.</p>";
                    return;
                }

                titulo.textContent = praia.nome;

                const idealParaHTML = praia.ideal_para
                    .map(function (item) {
                        return `<span class="tag">${item}</span>`;
                    })
                    .join("");

                container.innerHTML = `
                <img src="${praia.imagem}" class="detalhe-img" alt="Imagem de ${praia.nome}">

                <p>${praia.descricao}</p>

                <div class="detalhe-grid">
                    <div><strong>Zona:</strong> ${praia.zona}</div>
                    <div><strong>Localização:</strong> ${praia.localizacao}</div>
                    <div><strong>Tipo de mar:</strong> ${praia.tipo_mar}</div>
                    <div><strong>Acessibilidade:</strong> ${praia.acessivel ? "Acessível" : "Acesso mais difícil"}</div>
                    <div><strong>Estacionamento:</strong> ${praia.estacionamento ? "Disponível" : "Não indicado"}</div>
                    <div><strong>Restauração:</strong> ${praia.restauracao ? "Existe na zona" : "Limitada"}</div>
                    <div><strong>Transportes:</strong> ${praia.transportes ? "Com opção de transporte" : "Limitado"}</div>
                </div>

                <p><strong>Ideal para:</strong></p>
                <div>${idealParaHTML}</div>

                <div class="acoes-praia">
                    <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(praia.nome + ' ' + praia.localizacao)}" target="_blank" class="btn-mapa">
                        Ver no mapa
                    </a>
                </div>
            `;
            })
            .catch(function () {
                titulo.textContent = "Erro ao carregar";
                container.innerHTML = "<p>Não foi possível carregar a informação. Verifica se a API está ligada.</p>";
            });
    }

    /*botao voltar / retornar */
    const btnVoltar = document.getElementById("btn-voltar");

    if (btnVoltar) {
        btnVoltar.addEventListener("click", function () {
            window.location.href = "praias.html";
        });
    }

    carregarDetalhePraia();

    /* ================= IA — Guia Turístico (Gemini) ================= */

    function inicializarAI() {
        var aiSection = document.getElementById("ai-section");
        var btnAI = document.getElementById("btn-ai-guia");
        var aiLoading = document.getElementById("ai-loading");
        var aiResultado = document.getElementById("ai-resultado");

        if (!aiSection || !btnAI) return;

        // Detect which detail page we're on and get the destination name
        var tituloElement =
            document.getElementById("titulo-praia") ||
            document.getElementById("titulo-parque") ||
            document.getElementById("titulo-miradouro") ||
            document.getElementById("titulo-historico") ||
            document.getElementById("titulo-restaurante") ||
            document.getElementById("titulo-cultura");

        if (!tituloElement) return;

        // Determine the type based on which title element was found
        var tipoMap = {
            "titulo-praia": "praia",
            "titulo-parque": "parque",
            "titulo-miradouro": "miradouro",
            "titulo-historico": "local histórico",
            "titulo-restaurante": "restaurante",
            "titulo-cultura": "espaço cultural"
        };
        var tipo = tipoMap[tituloElement.id] || "destino";

        // Wait for the detail to load before showing the AI button
        var checkInterval = setInterval(function () {
            var nome = tituloElement.textContent;
            if (nome && nome !== "A carregar..." && !nome.includes("não encontrad")) {
                clearInterval(checkInterval);
                aiSection.style.display = "block";

                btnAI.addEventListener("click", function () {
                    btnAI.disabled = true;
                    btnAI.textContent = "⏳ A gerar...";
                    aiLoading.style.display = "flex";
                    aiResultado.classList.remove("visivel");
                    aiResultado.innerHTML = "";

                    fetch("http://127.0.0.1:5001/api/ai/guia", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ destino: nome, tipo: tipo })
                    })
                        .then(function (res) { return res.json(); })
                        .then(function (data) {
                            aiLoading.style.display = "none";
                            if (data.erro) {
                                aiResultado.innerHTML = '<p class="ai-erro">⚠️ ' + data.erro + '</p>';
                            } else {
                                // Convert markdown-like headings to HTML
                                var html = data.guia
                                    .replace(/^### (.+)$/gm, "<h3>$1</h3>")
                                    .replace(/^## (.+)$/gm, "<h2>$1</h2>")
                                    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
                                    .replace(/\n\n/g, "</p><p>")
                                    .replace(/\n/g, "<br>");
                                aiResultado.innerHTML = "<p>" + html + "</p>";
                            }
                            aiResultado.classList.add("visivel");
                            btnAI.textContent = "🤖 Gerar novo guia";
                            btnAI.disabled = false;
                        })
                        .catch(function () {
                            aiLoading.style.display = "none";
                            aiResultado.innerHTML = '<p class="ai-erro">⚠️ Não foi possível contactar a API de IA. Verifica se o servidor está a correr.</p>';
                            aiResultado.classList.add("visivel");
                            btnAI.textContent = "🤖 Tentar novamente";
                            btnAI.disabled = false;
                        });
                });
            }
        }, 500);
    }

    inicializarAI();

});
