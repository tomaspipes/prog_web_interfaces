const API = "http://127.0.0.1:5001";

document.addEventListener("DOMContentLoaded", function () {

    let todosPontos = [];
    let filtroAtivo = "todos";

    const grid = document.getElementById("spa-grid");
    const contagem = document.querySelector(".spa-contagem");
    const pesquisa = document.getElementById("pesquisa-pontos");
    const botoesFiltro = document.querySelectorAll(".spa-filtros .tag");
    const overlay = document.getElementById("spa-overlay");
    const btnFechar = document.getElementById("spa-fechar");

    const endpoints = [
        { url: "/api/praias",    categoria: "praias",    label: "Praia" },
        { url: "/api/parques",   categoria: "parques",   label: "Parque" },
        { url: "/api/miradouros",categoria: "miradouros",label: "Miradouro" },
        { url: "/api/historicos",categoria: "historicos",label: "Local Histórico" },
        { url: "/api/comer",     categoria: "comer",     label: "Restaurante" },
        { url: "/api/cultura",   categoria: "cultura",   label: "Cultura" },
    ];

    Promise.all(endpoints.map(ep =>
        fetch(API + ep.url)
            .then(r => r.json())
            .then(items => items.map(item => ({
                ...item,
                _categoria: ep.categoria,
                _label: ep.label
            })))
    ))
    .then(resultados => {
        todosPontos = resultados.flat();
        renderizar();
    })
    .catch(() => {
        contagem.textContent = "Erro ao carregar dados. Verifique se o servidor está ativo.";
    });

    botoesFiltro.forEach(btn => {
        btn.addEventListener("click", function () {
            botoesFiltro.forEach(b => b.classList.remove("ativo"));
            this.classList.add("ativo");
            filtroAtivo = this.dataset.filtro;
            renderizar();
        });
    });

    pesquisa.addEventListener("input", renderizar);

    function renderizar() {
        const termo = pesquisa.value.toLowerCase().trim();
        let filtrados = todosPontos;

        if (filtroAtivo !== "todos") {
            filtrados = filtrados.filter(p => p._categoria === filtroAtivo);
        }
        if (termo) {
            filtrados = filtrados.filter(p => {
                const nome = (p.nome || "").toLowerCase();
                const desc = (p.descricao || "").toLowerCase();
                const tags = Array.isArray(p.tags) ? p.tags.join(" ").toLowerCase() : "";
                return nome.includes(termo) || desc.includes(termo) || tags.includes(termo);
            });
        }

        contagem.textContent = `${filtrados.length} ponto${filtrados.length !== 1 ? "s" : ""} de interesse encontrado${filtrados.length !== 1 ? "s" : ""}`;

        grid.innerHTML = filtrados.map((p, idx) => {
            const nome = p.nome || "Sem nome";
            const desc = p.descricao || "";
            const tags = Array.isArray(p.tags) ? p.tags : [];
            const acessivel = p.acessivel ? '<span class="tag tag-acessivel">♿ Acessível</span>' : "";

            return `
                <article class="card card-clicavel" data-idx="${todosPontos.indexOf(p)}" tabindex="0" role="button" aria-label="Ver detalhe de ${nome}">
                    ${p.imagem ? `<img src="${p.imagem}" alt="${nome}" loading="lazy">` : ""}
                    <div class="card-body">
                        <span class="card-categoria">${p._label}</span>
                        <h3>${nome}</h3>
                        <p>${desc.substring(0, 110)}${desc.length > 110 ? "..." : ""}</p>
                        <div class="card-tags">
                            ${tags.map(t => `<span class="tag">${t}</span>`).join("")}
                            ${acessivel}
                        </div>
                    </div>
                </article>
            `;
        }).join("");

        grid.querySelectorAll(".card-clicavel").forEach(card => {
            card.addEventListener("click", function () {
                abrirDetalhe(todosPontos[parseInt(this.dataset.idx)]);
            });
            card.addEventListener("keydown", function (e) {
                if (e.key === "Enter" || e.key === " ") abrirDetalhe(todosPontos[parseInt(this.dataset.idx)]);
            });
        });
    }

    function abrirDetalhe(p) {
        const nome = p.nome || "Sem nome";
        const tags = Array.isArray(p.tags) ? p.tags : [];
        const proximidades = Array.isArray(p.pontos_proximos) ? p.pontos_proximos : [];
        const acessivel = p.acessivel ? '<span class="tag tag-acessivel">♿ Acessível</span>' : "";

        document.getElementById("spa-detalhe-titulo").textContent = nome;
        document.getElementById("spa-detalhe-categoria").textContent = p._label;
        document.getElementById("spa-detalhe-localizacao").textContent = p.localizacao || p.morada || "";
        document.getElementById("spa-detalhe-descricao").textContent = p.descricao || "";

        const imgEl = document.getElementById("spa-detalhe-img");
        if (p.imagem) {
            imgEl.src = p.imagem;
            imgEl.alt = nome;
            imgEl.hidden = false;
        } else {
            imgEl.hidden = true;
        }

        document.getElementById("spa-detalhe-tags").innerHTML =
            tags.map(t => `<span class="tag">${t}</span>`).join("") + acessivel;

        const proxEl = document.getElementById("spa-detalhe-proximidades");
        if (proximidades.length) {
            proxEl.innerHTML = "<strong>Pontos próximos:</strong> " +
                proximidades.map(pr => `<span class="tag">${pr}</span>`).join("");
        } else {
            proxEl.innerHTML = "";
        }

        overlay.hidden = false;
        document.body.style.overflow = "hidden";
        btnFechar.focus();
    }

    function fecharDetalhe() {
        overlay.hidden = true;
        document.body.style.overflow = "";
    }

    btnFechar.addEventListener("click", fecharDetalhe);

    overlay.addEventListener("click", function (e) {
        if (e.target === overlay) fecharDetalhe();
    });

    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && !overlay.hidden) fecharDetalhe();
    });

    const backToTop = document.querySelector(".back-to-top");
    if (backToTop) {
        window.addEventListener("scroll", function () {
            backToTop.classList.toggle("visivel", window.scrollY > 300);
        });
    }
});
