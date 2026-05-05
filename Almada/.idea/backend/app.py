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
            "titulo": "Restaurantes de peixe",
            "descricao": "Zonas conhecidas por peixe fresco e cozinha tradicional, com destaque para Cacilhas e a frente ribeirinha.",
            "tags": ["Peixe fresco"],
            "locais": ["Cacilhas", "Ginjal", "Costa da Caparica"]
        },
        {
            "id": 2,
            "titulo": "Restaurantes tradicionais",
            "descricao": "Espaços com cozinha portuguesa, pratos regionais e ambientes familiares.",
            "tags": ["Comida portuguesa"],
            "locais": ["Almada Velha", "Cova da Piedade", "Costa da Caparica"]
        },
        {
            "id": 3,
            "titulo": "Cafés, esplanadas e bares",
            "descricao": "Espaços de convívio junto ao rio, à praia e a zonas históricas.",
            "tags": ["Convívio"],
            "locais": ["Cacilhas", "Boca do Vento", "Costa da Caparica", "Fonte da Telha"]
        }
    ]

    return jsonify(comer)


@app.route("/api/cultura")
def listar_cultura():
    cultura = [
        {
            "id": 1,
            "titulo": "Casa da Cerca",
            "descricao": "Centro de Arte Contemporânea situado num edifício histórico com vista sobre Lisboa e o Tejo.",
            "tags": ["Arte contemporânea"],
            "locais": ["Casa da Cerca", "Jardim Botânico O Chão das Artes"]
        },
        {
            "id": 2,
            "titulo": "Teatro e eventos",
            "descricao": "Oferta cultural ligada a teatro, programação municipal e eventos locais.",
            "tags": ["Cultura local"],
            "locais": ["Teatro Municipal Joaquim Benite", "Fórum Municipal Romeu Correia"]
        },
        {
            "id": 3,
            "titulo": "Património e museus",
            "descricao": "Espaços ligados à memória, à história local e à identidade do concelho.",
            "tags": ["História"],
            "locais": ["Castelo de Almada", "Museu Naval", "Almada Velha"]
        }
    ]

    return jsonify(cultura)


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
    app.run(debug=True)