import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "almada.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # ── Tabelas ──

    c.execute("""
        CREATE TABLE IF NOT EXISTS passear (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            categoria TEXT,
            descricao TEXT,
            tags TEXT,
            locais TEXT,
            como_chegar TEXT,
            acessivel INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS praias (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            zona TEXT,
            descricao TEXT,
            acessivel INTEGER,
            estacionamento INTEGER,
            restauracao INTEGER,
            transportes INTEGER,
            tipo_mar TEXT,
            ideal_para TEXT,
            localizacao TEXT,
            imagem TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS parques (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            zona TEXT,
            descricao TEXT,
            acessivel INTEGER,
            familias INTEGER,
            transportes INTEGER,
            estacionamento INTEGER,
            tipo TEXT,
            ideal_para TEXT,
            localizacao TEXT,
            imagem TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS comer (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT,
            tipo TEXT,
            zona TEXT,
            localizacao TEXT,
            descricao TEXT,
            tags TEXT,
            locais TEXT,
            imagem TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS cultura (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT,
            tipo TEXT,
            zona TEXT,
            localizacao TEXT,
            descricao TEXT,
            tags TEXT,
            locais TEXT,
            imagem TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS miradouros (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            zona TEXT,
            localizacao TEXT,
            descricao TEXT,
            acessivel INTEGER,
            transportes INTEGER,
            estacionamento INTEGER,
            tags TEXT,
            ideal_para TEXT,
            imagem TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS historicos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            zona TEXT,
            localizacao TEXT,
            tipo TEXT,
            descricao TEXT,
            acessivel INTEGER,
            transportes INTEGER,
            tags TEXT,
            ideal_para TEXT,
            imagem TEXT
        )
    """)

    # ── Dados ──

    # Passear
    passear = [
        (1, "Praias", "praias", "Praias atlânticas do concelho de Almada, com destaque para a Costa da Caparica e Fonte da Telha.",
         json.dumps(["Atlântico", "Lazer"]),
         json.dumps(["Costa da Caparica", "Fonte da Telha", "São João da Caparica", "Cova do Vapor"]),
         "Consultar transportes e acessos rodoviários na secção Transportes.", 1),
        (2, "Parques e jardins", "parques", "Espaços verdes adequados para passeios calmos, descanso e contacto com a natureza.",
         json.dumps(["Acessível", "Descanso"]),
         json.dumps(["Parque da Paz", "Jardim do Rio", "Jardim do Castelo"]),
         "Consultar transportes públicos próximos e acessos pedonais.", 1),
        (3, "Miradouros", "miradouros", "Locais com vista panorâmica sobre Lisboa, o rio Tejo e a frente ribeirinha de Almada.",
         json.dumps(["Vista sobre Lisboa"]),
         json.dumps(["Cristo Rei", "Boca do Vento", "Almada Velha"]),
         "Verificar acessos, transportes e existência de zonas inclinadas.", 0),
        (4, "Locais históricos", "historico", "Espaços com valor histórico, religioso e cultural ligados à identidade de Almada.",
         json.dumps(["Património", "História"]),
         json.dumps(["Castelo de Almada", "Casa da Cerca", "Convento dos Capuchos"]),
         "Confirmar acessibilidade e transportes disponíveis antes da visita.", 0),
    ]
    c.executemany("INSERT OR REPLACE INTO passear VALUES (?,?,?,?,?,?,?,?)", passear)

    # Praias
    praias = [
        (1, "Costa da Caparica", "Costa da Caparica",
         "Extensa frente atlântica com areais longos, forte procura balnear, apoios de praia, restauração e condições para surf.",
         1, 1, 1, 1, "Ondas", json.dumps(["famílias", "surf", "passeio"]),
         "Costa da Caparica", "imagens/almada/costa-caparica.jpg"),
        (2, "Fonte da Telha", "Fonte da Telha",
         "Zona costeira com grande areal, ambiente mais tranquilo, restauração próxima e forte ligação à paisagem natural.",
         1, 1, 1, 1, "Ondas", json.dumps(["famílias", "gastronomia", "passeio"]),
         "Fonte da Telha", "imagens/almada/fonte-da-telha.jpg"),
        (3, "São João da Caparica", "Costa da Caparica",
         "Praia situada na zona norte da frente atlântica de Almada, próxima de acessos urbanos e bastante procurada para lazer.",
         1, 1, 1, 1, "Ondas", json.dumps(["famílias", "passeio", "praia urbana"]),
         "São João da Caparica", "imagens/almada/sao-joao-caparica.jpg"),
        (4, "Cova do Vapor", "Trafaria / Caparica",
         "Praia situada junto à foz do Tejo, com ambiente característico e ligação visual à entrada do rio.",
         0, 1, 0, 1, "Misto", json.dumps(["paisagem", "passeio", "fotografia"]),
         "Cova do Vapor", "imagens/almada/cova-do-vapor.jpg"),
        (5, "Praia da Rainha", "Costa da Caparica",
         "Praia da linha da Costa da Caparica, conhecida pelo ambiente balnear e proximidade a apoios de praia.",
         1, 0, 1, 1, "Ondas", json.dumps(["famílias", "lazer", "restauração"]),
         "Costa da Caparica", "imagens/almada/Praia-da-Rainha.webp"),
        (6, "Praia da Morena", "Costa da Caparica",
         "Praia procurada pelo ambiente jovem, bares de praia e ligação ao lazer de verão.",
         0, 1, 1, 0, "Ondas", json.dumps(["bares", "lazer", "surf"]),
         "Costa da Caparica", "imagens/almada/praia-morena.jpg"),
        (7, "Praia da Sereia", "Costa da Caparica",
         "Praia associada a bares e ambiente descontraído, bastante frequentada em época balnear.",
         0, 0, 1, 0, "Ondas", json.dumps(["bares", "lazer", "passeio"]),
         "Costa da Caparica", "imagens/almada/praia-sereia.jpg"),
        (8, "Praia da Cabana do Pescador", "Costa da Caparica",
         "Praia ampla, muito procurada por banhistas e visitantes que procuram uma zona de praia com apoio e espaço.",
         1, 0, 1, 0, "Ondas", json.dumps(["famílias", "lazer", "passeio"]),
         "Costa da Caparica", "imagens/almada/praia-cabana-pescador.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO praias VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", praias)

    # Parques
    parques = [
        (1, "Parque da Paz", "Feijó",
         "Grande parque urbano de Almada, adequado para caminhadas, descanso, contacto com a natureza e passeios em família.",
         1, 1, 1, 1, "Parque urbano", json.dumps(["famílias", "caminhada", "descanso"]),
         "Parque da Paz, Almada", "imagens/almada/parque-da-paz.jpg"),
        (2, "Jardim do Rio", "Cacilhas",
         "Espaço junto à frente ribeirinha, com vista para Lisboa e ambiente adequado para passeios curtos e descanso.",
         1, 1, 1, 0, "Jardim ribeirinho", json.dumps(["vista", "passeio", "descanso"]),
         "Jardim do Rio, Almada", "imagens/almada/jardim-do-rio.jpg"),
        (3, "Jardim do Castelo", "Almada Velha",
         "Jardim localizado numa zona histórica, com interesse patrimonial e vista sobre a envolvente urbana e ribeirinha.",
         0, 0, 1, 0, "Jardim histórico", json.dumps(["história", "vista", "passeio"]),
         "Jardim do Castelo, Almada", "imagens/almada/jardim-castelo.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO parques VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", parques)

    # Comer
    comer = [
        (1, "Restaurantes de peixe de Cacilhas", "peixe", "Restaurante de peixe", "Cacilhas", "Cacilhas, Almada",
         "Zona ribeirinha conhecida por restaurantes de peixe fresco com vista para o Tejo e Lisboa. Destaque para o camarão, linguado e outros frutos do mar típicos da margem sul.",
         json.dumps(["Peixe fresco", "Vista para o Tejo"]),
         json.dumps(["Cais do Ginjal", "Rua Cândido dos Reis", "Cacilhas"]),
         "imagens/almada/cacilhas-restaurantes.jpg"),
        (2, "Restaurantes de peixe da Costa da Caparica", "peixe", "Restaurante de peixe", "Costa da Caparica", "Costa da Caparica, Almada",
         "Restaurantes junto à praia atlântica com peixe e marisco frescos, ideais após um dia de praia.",
         json.dumps(["Peixe fresco", "Praia"]),
         json.dumps(["Costa da Caparica", "Fonte da Telha"]),
         "imagens/almada/caparica-restaurantes.jpg"),
        (3, "Restaurantes tradicionais de Almada Velha", "tradicional", "Restaurante tradicional", "Almada Velha", "Almada Velha, Almada",
         "Cozinha portuguesa com pratos regionais, bacalhau e sopas tradicionais, em ambiente familiar e histórico.",
         json.dumps(["Comida portuguesa", "Ambiente histórico"]),
         json.dumps(["Almada Velha", "Cova da Piedade"]),
         "imagens/almada/almada-velha-restaurantes.jpg"),
        (4, "Cafés e esplanadas de Cacilhas", "bar", "Café e esplanada", "Cacilhas", "Cacilhas, Almada",
         "Esplanadas com vista para o rio Tejo e Lisboa, ideais para uma pausa com café ou petisco junto ao ferry.",
         json.dumps(["Esplanada", "Vista para Lisboa"]),
         json.dumps(["Largo Alfredo Dinis", "Boca do Vento"]),
         "imagens/almada/cacilhas-cafes.jpg"),
        (5, "Bares de praia da Costa da Caparica", "bar", "Bar de praia", "Costa da Caparica", "Costa da Caparica, Almada",
         "Bares de praia com ambiente descontraído, bebidas frescas e petiscos, junto ao areal atlântico.",
         json.dumps(["Praia", "Ambiente jovem"]),
         json.dumps(["Costa da Caparica", "Praia da Morena", "Fonte da Telha"]),
         "imagens/almada/caparica-bares.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO comer VALUES (?,?,?,?,?,?,?,?,?,?)", comer)

    # Cultura
    cultura = [
        (1, "Casa da Cerca", "arte", "Centro de Arte Contemporânea", "Almada", "Rua Casa da Cerca, Almada",
         "Centro de Arte Contemporânea situado num edifício histórico com jardim botânico e vista panorâmica sobre o Tejo e Lisboa. Alberga exposições de artistas nacionais e internacionais.",
         json.dumps(["Arte contemporânea", "Vista para o Tejo"]),
         json.dumps(["Casa da Cerca", "Jardim Botânico O Chão das Artes"]),
         "imagens/almada/casa-da-cerca.jpg"),
        (2, "Teatro Municipal Joaquim Benite", "teatro", "Teatro", "Almada", "Praça de Portugal, Almada",
         "Principal sala de espetáculos de Almada, com programação regular de teatro, dança e música. Sede do afamado Festival Internacional de Teatro de Almada.",
         json.dumps(["Teatro", "Festival"]),
         json.dumps(["Teatro Municipal Joaquim Benite"]),
         "imagens/almada/teatro-municipal.jpg"),
        (3, "Fórum Municipal Romeu Correia", "teatro", "Espaço cultural multiusos", "Almada", "Almada",
         "Espaço cultural com programação diversificada que inclui teatro, música, cinema e eventos municipais.",
         json.dumps(["Eventos", "Cultura local"]),
         json.dumps(["Fórum Municipal Romeu Correia"]),
         "imagens/almada/forum-romeu-correia.jpg"),
        (4, "Museu Naval de Almada", "patrimonio", "Museu", "Cacilhas", "Cacilhas, Almada",
         "Museu dedicado à história naval portuguesa, com peças, embarcações e documentos ligados à tradição marítima da margem sul do Tejo.",
         json.dumps(["História", "Marítimo"]),
         json.dumps(["Cacilhas"]),
         "imagens/almada/museu-naval.jpg"),
        (5, "Almada Velha", "patrimonio", "Zona histórica", "Almada Velha", "Almada Velha, Almada",
         "Núcleo histórico de Almada com ruas medievais, miradouros, igrejas e o antigo castelo. Zona de grande valor patrimonial e identitário do concelho.",
         json.dumps(["Património", "Medieval"]),
         json.dumps(["Castelo de Almada", "Igreja de São João Baptista", "Boca do Vento"]),
         "imagens/almada/almada-velha.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO cultura VALUES (?,?,?,?,?,?,?,?,?,?)", cultura)

    # Miradouros
    miradouros = [
        (1, "Cristo Rei", "Alto do Pragal", "Alto do Pragal, Almada",
         "Monumento icónico com vista de 360° sobre Lisboa, o Tejo e toda a área metropolitana. Inclui elevador panorâmico e plataforma de observação a 82 metros de altura.",
         1, 1, 1,
         json.dumps(["Vista 360°", "Religioso", "Monumento"]),
         json.dumps(["fotografia", "visita cultural", "família"]),
         "imagens/almada/cristo-rei.jpg"),
        (2, "Boca do Vento", "Cacilhas", "Cacilhas, Almada",
         "Miradouro com elevador público sobre o Tejo, com vista direta para Lisboa e a Ponte 25 de Abril. Um dos locais mais fotogénicos e acessíveis da margem sul.",
         1, 1, 0,
         json.dumps(["Vista para Lisboa", "Ribeirinho"]),
         json.dumps(["fotografia", "passeio", "casal"]),
         "imagens/almada/boca-do-vento.jpg"),
        (3, "Miradouro de Almada Velha", "Almada Velha", "Almada Velha, Almada",
         "Vista sobre o Tejo a partir do núcleo histórico de Almada, com enquadramento único entre as ruínas do castelo medieval e a frente ribeirinha.",
         0, 1, 0,
         json.dumps(["Vista histórica", "Medieval"]),
         json.dumps(["fotografia", "história", "passeio"]),
         "imagens/almada/miradouro-almada-velha.jpg"),
        (4, "Miradouro da Costa da Caparica", "Costa da Caparica", "Costa da Caparica, Almada",
         "Vista sobre o oceano Atlântico e a extensa linha costeira da Caparica. Ideal para observar o pôr-do-sol sobre o mar.",
         1, 1, 1,
         json.dumps(["Vista para o Atlântico", "Pôr-do-sol"]),
         json.dumps(["fotografia", "relaxamento", "família"]),
         "imagens/almada/miradouro-caparica.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO miradouros VALUES (?,?,?,?,?,?,?,?,?,?,?)", miradouros)

    # Historicos
    historicos = [
        (1, "Castelo de Almada", "Almada Velha", "Almada Velha, Almada", "Castelo medieval",
         "Ruínas do castelo medieval de Almada, com origem mourisca e reconstrução posterior. Está integrado no núcleo histórico e oferece vista sobre o Tejo.",
         0, 1,
         json.dumps(["Medieval", "Arqueologia", "Ruínas"]),
         json.dumps(["história", "fotografia", "arqueologia"]),
         "imagens/almada/castelo-almada.jpg"),
        (2, "Casa da Cerca", "Almada", "Rua Casa da Cerca, Almada", "Edifício histórico / Centro de arte",
         "Antiga quinta histórica do século XVII, hoje reconvertida em centro de arte contemporânea. Inclui jardim botânico e vista panorâmica sobre o Tejo.",
         1, 1,
         json.dumps(["Século XVII", "Arte", "Jardim histórico"]),
         json.dumps(["arte", "história", "família"]),
         "imagens/almada/casa-da-cerca.jpg"),
        (3, "Convento dos Capuchos", "Costa da Caparica", "Caparica, Almada", "Convento",
         "Convento franciscano do século XVI inserido numa paisagem natural de grande valor. Um dos exemplos mais bem preservados da arquitectura religiosa na margem sul.",
         0, 0,
         json.dumps(["Século XVI", "Religioso", "Franciscano"]),
         json.dumps(["história", "religião", "fotografia"]),
         "imagens/almada/convento-capuchos.jpg"),
        (4, "Igreja de Nossa Senhora do Cabo", "Almada Velha", "Almada Velha, Almada", "Igreja",
         "Igreja com grande valor histórico e religioso, integrada no núcleo antigo de Almada. Destaca-se pela arquitectura e pelo enquadramento junto às muralhas.",
         0, 1,
         json.dumps(["Religioso", "Património"]),
         json.dumps(["história", "religião", "arquitetura"]),
         "imagens/almada/igreja-nossa-senhora-cabo.jpg"),
        (5, "Museu Naval de Almada", "Cacilhas", "Cacilhas, Almada", "Museu",
         "Museu dedicado à história naval portuguesa e à tradição marítima da margem sul do Tejo, com embarcações, instrumentos e documentos históricos.",
         1, 1,
         json.dumps(["Marítimo", "Museu", "História"]),
         json.dumps(["história", "família", "educação"]),
         "imagens/almada/museu-naval.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO historicos VALUES (?,?,?,?,?,?,?,?,?,?,?)", historicos)

    conn.commit()
    conn.close()
    print(f"Base de dados criada em: {DB_PATH}")


if __name__ == "__main__":
    init_db()
