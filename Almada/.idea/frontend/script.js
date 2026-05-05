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

    carregarSecao("http://127.0.0.1:5000/api/passear", "lista-passear");
    carregarSecao("http://127.0.0.1:5000/api/comer", "lista-comer");
    carregarSecao("http://127.0.0.1:5000/api/cultura", "lista-cultura");



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
                carregarSecao("http://127.0.0.1:5000/api/passear", "lista-passear");
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
        fetch("http://127.0.0.1:5000/api/praias")
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

        fetch("http://127.0.0.1:5000/api/praias")
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

});