from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "mensagem": "API Almada ativa"
    })


@app.route("/api/passear")
def listar_passear():
    passear = [
        {
            "id": 1,
            "titulo": "Praias",
            "categoria": "praias",
            "descricao": "Praias atlânticas do concelho de Almada, com destaque para a Costa da Caparica e Fonte da Telha.",
            "tags": ["Atlântico", "Lazer"],
            "locais": ["Costa da Caparica", "Fonte da Telha", "São João da Caparica", "Cova do Vapor"],
            "como_chegar": "Consultar transportes e acessos rodoviários na secção Transportes.",
            "acessivel": True
        },
        {
            "id": 2,
            "titulo": "Parques e jardins",
            "categoria": "parques",
            "descricao": "Espaços verdes adequados para passeios calmos, descanso e contacto com a natureza.",
            "tags": ["Acessível", "Descanso"],
            "locais": ["Parque da Paz", "Jardim do Rio", "Jardim do Castelo"],
            "como_chegar": "Consultar transportes públicos próximos e acessos pedonais.",
            "acessivel": True
        },
        {
            "id": 3,
            "titulo": "Miradouros",
            "categoria": "miradouros",
            "descricao": "Locais com vista panorâmica sobre Lisboa, o rio Tejo e a frente ribeirinha de Almada.",
            "tags": ["Vista sobre Lisboa"],
            "locais": ["Cristo Rei", "Boca do Vento", "Almada Velha"],
            "como_chegar": "Verificar acessos, transportes e existência de zonas inclinadas.",
            "acessivel": False
        },
        {
            "id": 4,
            "titulo": "Locais históricos",
            "categoria": "historico",
            "descricao": "Espaços com valor histórico, religioso e cultural ligados à identidade de Almada.",
            "tags": ["Património", "História"],
            "locais": ["Castelo de Almada", "Casa da Cerca", "Convento dos Capuchos"],
            "como_chegar": "Confirmar acessibilidade e transportes disponíveis antes da visita.",
            "acessivel": False
        }
    ]

    return jsonify(passear)


@app.route("/api/comer")
def listar_comer():
    comer = [
        {
            "id": 1,
            "nome": "Restaurantes de peixe de Cacilhas",
            "categoria": "peixe",
            "tipo": "Restaurante de peixe",
            "zona": "Cacilhas",
            "localizacao": "Cacilhas, Almada",
            "descricao": "Zona ribeirinha conhecida por restaurantes de peixe fresco com vista para o Tejo e Lisboa. Destaque para o camarão, linguado e outros frutos do mar típicos da margem sul.",
            "tags": ["Peixe fresco", "Vista para o Tejo"],
            "locais": ["Cais do Ginjal", "Rua Cândido dos Reis", "Cacilhas"],
            "imagem": "imagens/almada/cacilhas-restaurantes.jpg"
        },
        {
            "id": 2,
            "nome": "Restaurantes de peixe da Costa da Caparica",
            "categoria": "peixe",
            "tipo": "Restaurante de peixe",
            "zona": "Costa da Caparica",
            "localizacao": "Costa da Caparica, Almada",
            "descricao": "Restaurantes junto à praia atlântica com peixe e marisco frescos, ideais após um dia de praia.",
            "tags": ["Peixe fresco", "Praia"],
            "locais": ["Costa da Caparica", "Fonte da Telha"],
            "imagem": "imagens/almada/caparica-restaurantes.jpg"
        },
        {
            "id": 3,
            "nome": "Restaurantes tradicionais de Almada Velha",
            "categoria": "tradicional",
            "tipo": "Restaurante tradicional",
            "zona": "Almada Velha",
            "localizacao": "Almada Velha, Almada",
            "descricao": "Cozinha portuguesa com pratos regionais, bacalhau e sopas tradicionais, em ambiente familiar e histórico.",
            "tags": ["Comida portuguesa", "Ambiente histórico"],
            "locais": ["Almada Velha", "Cova da Piedade"],
            "imagem": "imagens/almada/almada-velha-restaurantes.jpg"
        },
        {
            "id": 4,
            "nome": "Cafés e esplanadas de Cacilhas",
            "categoria": "bar",
            "tipo": "Café e esplanada",
            "zona": "Cacilhas",
            "localizacao": "Cacilhas, Almada",
            "descricao": "Esplanadas com vista para o rio Tejo e Lisboa, ideais para uma pausa com café ou petisco junto ao ferry.",
            "tags": ["Esplanada", "Vista para Lisboa"],
            "locais": ["Largo Alfredo Dinis", "Boca do Vento"],
            "imagem": "imagens/almada/cacilhas-cafes.jpg"
        },
        {
            "id": 5,
            "nome": "Bares de praia da Costa da Caparica",
            "categoria": "bar",
            "tipo": "Bar de praia",
            "zona": "Costa da Caparica",
            "localizacao": "Costa da Caparica, Almada",
            "descricao": "Bares de praia com ambiente descontraído, bebidas frescas e petiscos, junto ao areal atlântico.",
            "tags": ["Praia", "Ambiente jovem"],
            "locais": ["Costa da Caparica", "Praia da Morena", "Fonte da Telha"],
            "imagem": "imagens/almada/caparica-bares.jpg"
        }
    ]

    return jsonify(comer)


@app.route("/api/cultura")
def listar_cultura():
    cultura = [
        {
            "id": 1,
            "nome": "Casa da Cerca",
            "categoria": "arte",
            "tipo": "Centro de Arte Contemporânea",
            "zona": "Almada",
            "localizacao": "Rua Casa da Cerca, Almada",
            "descricao": "Centro de Arte Contemporânea situado num edifício histórico com jardim botânico e vista panorâmica sobre o Tejo e Lisboa. Alberga exposições de artistas nacionais e internacionais.",
            "tags": ["Arte contemporânea", "Vista para o Tejo"],
            "locais": ["Casa da Cerca", "Jardim Botânico O Chão das Artes"],
            "imagem": "imagens/almada/casa-da-cerca.jpg"
        },
        {
            "id": 2,
            "nome": "Teatro Municipal Joaquim Benite",
            "categoria": "teatro",
            "tipo": "Teatro",
            "zona": "Almada",
            "localizacao": "Praça de Portugal, Almada",
            "descricao": "Principal sala de espetáculos de Almada, com programação regular de teatro, dança e música. Sede do afamado Festival Internacional de Teatro de Almada.",
            "tags": ["Teatro", "Festival"],
            "locais": ["Teatro Municipal Joaquim Benite"],
            "imagem": "imagens/almada/teatro-municipal.jpg"
        },
        {
            "id": 3,
            "nome": "Fórum Municipal Romeu Correia",
            "categoria": "teatro",
            "tipo": "Espaço cultural multiusos",
            "zona": "Almada",
            "localizacao": "Almada",
            "descricao": "Espaço cultural com programação diversificada que inclui teatro, música, cinema e eventos municipais.",
            "tags": ["Eventos", "Cultura local"],
            "locais": ["Fórum Municipal Romeu Correia"],
            "imagem": "imagens/almada/forum-romeu-correia.jpg"
        },
        {
            "id": 4,
            "nome": "Museu Naval de Almada",
            "categoria": "patrimonio",
            "tipo": "Museu",
            "zona": "Cacilhas",
            "localizacao": "Cacilhas, Almada",
            "descricao": "Museu dedicado à história naval portuguesa, com peças, embarcações e documentos ligados à tradição marítima da margem sul do Tejo.",
            "tags": ["História", "Marítimo"],
            "locais": ["Cacilhas"],
            "imagem": "imagens/almada/museu-naval.jpg"
        },
        {
            "id": 5,
            "nome": "Almada Velha",
            "categoria": "patrimonio",
            "tipo": "Zona histórica",
            "zona": "Almada Velha",
            "localizacao": "Almada Velha, Almada",
            "descricao": "Núcleo histórico de Almada com ruas medievais, miradouros, igrejas e o antigo castelo. Zona de grande valor patrimonial e identitário do concelho.",
            "tags": ["Património", "Medieval"],
            "locais": ["Castelo de Almada", "Igreja de São João Baptista", "Boca do Vento"],
            "imagem": "imagens/almada/almada-velha.jpg"
        }
    ]

    return jsonify(cultura)


@app.route("/api/miradouros")
def listar_miradouros():
    miradouros = [
        {
            "id": 1,
            "nome": "Cristo Rei",
            "zona": "Alto do Pragal",
            "localizacao": "Alto do Pragal, Almada",
            "descricao": "Monumento icónico com vista de 360° sobre Lisboa, o Tejo e toda a área metropolitana. Inclui elevador panorâmico e plataforma de observação a 82 metros de altura.",
            "acessivel": True,
            "transportes": True,
            "estacionamento": True,
            "tags": ["Vista 360°", "Religioso", "Monumento"],
            "ideal_para": ["fotografia", "visita cultural", "família"],
            "imagem": "imagens/almada/cristo-rei.jpg"
        },
        {
            "id": 2,
            "nome": "Boca do Vento",
            "zona": "Cacilhas",
            "localizacao": "Cacilhas, Almada",
            "descricao": "Miradouro com elevador público sobre o Tejo, com vista direta para Lisboa e a Ponte 25 de Abril. Um dos locais mais fotogénicos e acessíveis da margem sul.",
            "acessivel": True,
            "transportes": True,
            "estacionamento": False,
            "tags": ["Vista para Lisboa", "Ribeirinho"],
            "ideal_para": ["fotografia", "passeio", "casal"],
            "imagem": "imagens/almada/boca-do-vento.jpg"
        },
        {
            "id": 3,
            "nome": "Miradouro de Almada Velha",
            "zona": "Almada Velha",
            "localizacao": "Almada Velha, Almada",
            "descricao": "Vista sobre o Tejo a partir do núcleo histórico de Almada, com enquadramento único entre as ruínas do castelo medieval e a frente ribeirinha.",
            "acessivel": False,
            "transportes": True,
            "estacionamento": False,
            "tags": ["Vista histórica", "Medieval"],
            "ideal_para": ["fotografia", "história", "passeio"],
            "imagem": "imagens/almada/miradouro-almada-velha.jpg"
        },
        {
            "id": 4,
            "nome": "Miradouro da Costa da Caparica",
            "zona": "Costa da Caparica",
            "localizacao": "Costa da Caparica, Almada",
            "descricao": "Vista sobre o oceano Atlântico e a extensa linha costeira da Caparica. Ideal para observar o pôr-do-sol sobre o mar.",
            "acessivel": True,
            "transportes": True,
            "estacionamento": True,
            "tags": ["Vista para o Atlântico", "Pôr-do-sol"],
            "ideal_para": ["fotografia", "relaxamento", "família"],
            "imagem": "imagens/almada/miradouro-caparica.jpg"
        }
    ]

    return jsonify(miradouros)


@app.route("/api/historicos")
def listar_historicos():
    historicos = [
        {
            "id": 1,
            "nome": "Castelo de Almada",
            "zona": "Almada Velha",
            "localizacao": "Almada Velha, Almada",
            "tipo": "Castelo medieval",
            "descricao": "Ruínas do castelo medieval de Almada, com origem mourisca e reconstrução posterior. Está integrado no núcleo histórico e oferece vista sobre o Tejo.",
            "acessivel": False,
            "transportes": True,
            "tags": ["Medieval", "Arqueologia", "Ruínas"],
            "ideal_para": ["história", "fotografia", "arqueologia"],
            "imagem": "imagens/almada/castelo-almada.jpg"
        },
        {
            "id": 2,
            "nome": "Casa da Cerca",
            "zona": "Almada",
            "localizacao": "Rua Casa da Cerca, Almada",
            "tipo": "Edifício histórico / Centro de arte",
            "descricao": "Antiga quinta histórica do século XVII, hoje reconvertida em centro de arte contemporânea. Inclui jardim botânico e vista panorâmica sobre o Tejo.",
            "acessivel": True,
            "transportes": True,
            "tags": ["Século XVII", "Arte", "Jardim histórico"],
            "ideal_para": ["arte", "história", "família"],
            "imagem": "imagens/almada/casa-da-cerca.jpg"
        },
        {
            "id": 3,
            "nome": "Convento dos Capuchos",
            "zona": "Costa da Caparica",
            "localizacao": "Caparica, Almada",
            "tipo": "Convento",
            "descricao": "Convento franciscano do século XVI inserido numa paisagem natural de grande valor. Um dos exemplos mais bem preservados da arquitectura religiosa na margem sul.",
            "acessivel": False,
            "transportes": False,
            "tags": ["Século XVI", "Religioso", "Franciscano"],
            "ideal_para": ["história", "religião", "fotografia"],
            "imagem": "imagens/almada/convento-capuchos.jpg"
        },
        {
            "id": 4,
            "nome": "Igreja de Nossa Senhora do Cabo",
            "zona": "Almada Velha",
            "localizacao": "Almada Velha, Almada",
            "tipo": "Igreja",
            "descricao": "Igreja com grande valor histórico e religioso, integrada no núcleo antigo de Almada. Destaca-se pela arquitectura e pelo enquadramento junto às muralhas.",
            "acessivel": False,
            "transportes": True,
            "tags": ["Religioso", "Património"],
            "ideal_para": ["história", "religião", "arquitetura"],
            "imagem": "imagens/almada/igreja-nossa-senhora-cabo.jpg"
        },
        {
            "id": 5,
            "nome": "Museu Naval de Almada",
            "zona": "Cacilhas",
            "localizacao": "Cacilhas, Almada",
            "tipo": "Museu",
            "descricao": "Museu dedicado à história naval portuguesa e à tradição marítima da margem sul do Tejo, com embarcações, instrumentos e documentos históricos.",
            "acessivel": True,
            "transportes": True,
            "tags": ["Marítimo", "Museu", "História"],
            "ideal_para": ["história", "família", "educação"],
            "imagem": "imagens/almada/museu-naval.jpg"
        }
    ]

    return jsonify(historicos)


@app.route("/api/praias")
def listar_praias():
    praias = [
        {
            "id": 1,
            "nome": "Costa da Caparica",
            "zona": "Costa da Caparica",
            "descricao": "Extensa frente atlântica com areais longos, forte procura balnear, apoios de praia, restauração e condições para surf.",
            "acessivel": True,
            "estacionamento": True,
            "restauracao": True,
            "transportes": True,
            "tipo_mar": "Ondas",
            "ideal_para": ["famílias", "surf", "passeio"],
            "localizacao": "Costa da Caparica",
            "imagem": "imagens/almada/costa-caparica.jpg"
        },
        {
            "id": 2,
            "nome": "Fonte da Telha",
            "zona": "Fonte da Telha",
            "descricao": "Zona costeira com grande areal, ambiente mais tranquilo, restauração próxima e forte ligação à paisagem natural.",
            "acessivel": True,
            "estacionamento": True,
            "restauracao": True,
            "transportes": True,
            "tipo_mar": "Ondas",
            "ideal_para": ["famílias", "gastronomia", "passeio"],
            "localizacao": "Fonte da Telha",
            "imagem": "imagens/almada/fonte-da-telha.jpg"
        },
        {
            "id": 3,
            "nome": "São João da Caparica",
            "zona": "Costa da Caparica",
            "descricao": "Praia situada na zona norte da frente atlântica de Almada, próxima de acessos urbanos e bastante procurada para lazer.",
            "acessivel": True,
            "estacionamento": True,
            "restauracao": True,
            "transportes": True,
            "tipo_mar": "Ondas",
            "ideal_para": ["famílias", "passeio", "praia urbana"],
            "localizacao": "São João da Caparica",
            "imagem": "imagens/almada/sao-joao-caparica.jpg"
        },
        {
            "id": 4,
            "nome": "Cova do Vapor",
            "zona": "Trafaria / Caparica",
            "descricao": "Praia situada junto à foz do Tejo, com ambiente característico e ligação visual à entrada do rio.",
            "acessivel": False,
            "estacionamento": True,
            "restauracao": False,
            "transportes": True,
            "tipo_mar": "Misto",
            "ideal_para": ["paisagem", "passeio", "fotografia"],
            "localizacao": "Cova do Vapor",
            "imagem": "imagens/almada/cova-do-vapor.jpg"
        },
        {
            "id": 5,
            "nome": "Praia da Rainha",
            "zona": "Costa da Caparica",
            "descricao": "Praia da linha da Costa da Caparica, conhecida pelo ambiente balnear e proximidade a apoios de praia.",
            "acessivel": True,
            "estacionamento": False,
            "restauracao": True,
            "transportes": True,
            "tipo_mar": "Ondas",
            "ideal_para": ["famílias", "lazer", "restauração"],
            "localizacao": "Costa da Caparica",
            "imagem": "imagens/almada/Praia-da-Rainha.webp"
        },
        {
            "id": 6,
            "nome": "Praia da Morena",
            "zona": "Costa da Caparica",
            "descricao": "Praia procurada pelo ambiente jovem, bares de praia e ligação ao lazer de verão.",
            "acessivel": False,
            "estacionamento": True,
            "restauracao": True,
            "transportes": False,
            "tipo_mar": "Ondas",
            "ideal_para": ["bares", "lazer", "surf"],
            "localizacao": "Costa da Caparica",
            "imagem": "imagens/almada/praia-morena.jpg"
        },
        {
            "id": 7,
            "nome": "Praia da Sereia",
            "zona": "Costa da Caparica",
            "descricao": "Praia associada a bares e ambiente descontraído, bastante frequentada em época balnear.",
            "acessivel": False,
            "estacionamento": False,
            "restauracao": True,
            "transportes": False,
            "tipo_mar": "Ondas",
            "ideal_para": ["bares", "lazer", "passeio"],
            "localizacao": "Costa da Caparica",
            "imagem": "imagens/almada/praia-sereia.jpg"
        },
        {
            "id": 8,
            "nome": "Praia da Cabana do Pescador",
            "zona": "Costa da Caparica",
            "descricao": "Praia ampla, muito procurada por banhistas e visitantes que procuram uma zona de praia com apoio e espaço.",
            "acessivel": True,
            "estacionamento": False,
            "restauracao": True,
            "transportes": False,
            "tipo_mar": "Ondas",
            "ideal_para": ["famílias", "lazer", "passeio"],
            "localizacao": "Costa da Caparica",
            "imagem": "imagens/almada/praia-cabana-pescador.jpg"
        }
    ]

    return jsonify(praias)

@app.route("/api/parques")
def listar_parques():
    parques = [
        {
            "id": 1,
            "nome": "Parque da Paz",
            "zona": "Feijó",
            "descricao": "Grande parque urbano de Almada, adequado para caminhadas, descanso, contacto com a natureza e passeios em família.",
            "acessivel": True,
            "familias": True,
            "transportes": True,
            "estacionamento": True,
            "tipo": "Parque urbano",
            "ideal_para": ["famílias", "caminhada", "descanso"],
            "localizacao": "Parque da Paz, Almada",
            "imagem": "imagens/almada/parque-da-paz.jpg"
        },
        {
            "id": 2,
            "nome": "Jardim do Rio",
            "zona": "Cacilhas",
            "descricao": "Espaço junto à frente ribeirinha, com vista para Lisboa e ambiente adequado para passeios curtos e descanso.",
            "acessivel": True,
            "familias": True,
            "transportes": True,
            "estacionamento": False,
            "tipo": "Jardim ribeirinho",
            "ideal_para": ["vista", "passeio", "descanso"],
            "localizacao": "Jardim do Rio, Almada",
            "imagem": "imagens/almada/jardim-do-rio.jpg"
        },
        {
            "id": 3,
            "nome": "Jardim do Castelo",
            "zona": "Almada Velha",
            "descricao": "Jardim localizado numa zona histórica, com interesse patrimonial e vista sobre a envolvente urbana e ribeirinha.",
            "acessivel": False,
            "familias": False,
            "transportes": True,
            "estacionamento": False,
            "tipo": "Jardim histórico",
            "ideal_para": ["história", "vista", "passeio"],
            "localizacao": "Jardim do Castelo, Almada",
            "imagem": "imagens/almada/jardim-castelo.jpg"
        }
    ]

    return jsonify(parques)

@app.route("/api/pontos")
def listar_pontos():
    return listar_passear()


if __name__ == "__main__":
    app.run(debug=True, port=5001)
