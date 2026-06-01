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
         "Costa da Caparica", "imagens/passear/praias/costa-caparica.jpg"),
        (2, "Fonte da Telha", "Fonte da Telha",
         "Zona costeira com grande areal, ambiente mais tranquilo, restauração próxima e forte ligação à paisagem natural.",
         1, 1, 1, 1, "Ondas", json.dumps(["famílias", "gastronomia", "passeio"]),
         "Fonte da Telha", "imagens/passear/praias/fonte-da-telha.jpg"),
        (3, "São João da Caparica", "Costa da Caparica",
         "Praia situada na zona norte da frente atlântica de Almada, próxima de acessos urbanos e bastante procurada para lazer.",
         1, 1, 1, 1, "Ondas", json.dumps(["famílias", "passeio", "praia urbana"]),
         "São João da Caparica", "imagens/passear/praias/sao-joao-caparica.jpg"),
        (4, "Cova do Vapor", "Trafaria / Caparica",
         "Praia situada junto à foz do Tejo, com ambiente característico e ligação visual à entrada do rio.",
         0, 1, 0, 1, "Misto", json.dumps(["paisagem", "passeio", "fotografia"]),
         "Cova do Vapor", "imagens/passear/praias/cova-do-vapor.jpg"),
        (5, "Praia da Rainha", "Costa da Caparica",
         "Praia da linha da Costa da Caparica, conhecida pelo ambiente balnear e proximidade a apoios de praia.",
         1, 0, 1, 1, "Ondas", json.dumps(["famílias", "lazer", "restauração"]),
         "Costa da Caparica", "imagens/passear/praias/Praia-da-Rainha.webp"),
        (6, "Praia da Morena", "Costa da Caparica",
         "Praia procurada pelo ambiente jovem, bares de praia e ligação ao lazer de verão.",
         0, 1, 1, 0, "Ondas", json.dumps(["bares", "lazer", "surf"]),
         "Costa da Caparica", "imagens/passear/praias/praia-morena.jpg"),
        (7, "Praia da Sereia", "Costa da Caparica",
         "Praia associada a bares e ambiente descontraído, bastante frequentada em época balnear.",
         0, 0, 1, 0, "Ondas", json.dumps(["bares", "lazer", "passeio"]),
         "Costa da Caparica", "imagens/passear/praias/praia-sereia.jpg"),
        (8, "Praia da Cabana do Pescador", "Costa da Caparica",
         "Praia ampla, muito procurada por banhistas e visitantes que procuram uma zona de praia com apoio e espaço.",
         1, 0, 1, 0, "Ondas", json.dumps(["famílias", "lazer", "passeio"]),
         "Costa da Caparica", "imagens/passear/praias/praia-cabana-pescador.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO praias VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", praias)

    # Parques
    parques = [
        (1, "Parque da Paz", "Feijó",
         "Grande parque urbano de Almada, adequado para caminhadas, descanso, contacto com a natureza e passeios em família.",
         1, 1, 1, 1, "Parque urbano", json.dumps(["famílias", "caminhada", "descanso"]),
         "Parque da Paz, Almada", "imagens/passear/parques/parque-da-paz.jpg"),
        (2, "Jardim do Rio", "Cacilhas",
         "Espaço junto à frente ribeirinha, com vista para Lisboa e ambiente adequado para passeios curtos e descanso.",
         1, 1, 1, 0, "Jardim ribeirinho", json.dumps(["vista", "passeio", "descanso"]),
         "Jardim do Rio, Almada", "imagens/passear/parques/jardim-do-rio.jpg"),
        (3, "Jardim do Castelo", "Almada Velha",
         "Jardim localizado numa zona histórica, com interesse patrimonial e vista sobre a envolvente urbana e ribeirinha.",
         0, 0, 1, 0, "Jardim histórico", json.dumps(["história", "vista", "passeio"]),
         "Jardim do Castelo, Almada", "imagens/passear/parques/jardim-castelo.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO parques VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", parques)

    # Comer
    comer = [
        (1, "Escondidinho de Cacilhas", "peixe", "Restaurante de peixe", "Cacilhas", "Rua Cândido dos Reis, Cacilhas",
         "Restaurante de referência em Cacilhas, especializado em peixe fresco e marisco. Vista sobre o Tejo e Lisboa, ambiente familiar e cozinha ribeirinha de qualidade.",
         json.dumps(["Peixe fresco", "Vista para o Tejo", "Marisco"]),
         json.dumps(["Cais do Ginjal", "Rua Cândido dos Reis", "Cacilhas"]),
         "imagens/comer/peixe/cacilhas-restaurantes.jpg"),
        (2, "The Ocean", "peixe", "Restaurante de peixe", "Costa da Caparica", "Costa da Caparica, Almada",
         "Restaurante junto à frente atlântica da Costa da Caparica, com peixe e marisco frescos. Ambiente descontraído com terraço e vista para o oceano.",
         json.dumps(["Peixe fresco", "Oceano", "Terraço"]),
         json.dumps(["Costa da Caparica", "Fonte da Telha"]),
         "imagens/comer/bares/the-ocean.jpg"),
        (3, "Sebastião", "tradicional", "Restaurante tradicional", "Almada Velha", "Almada Velha, Almada",
         "Restaurante tradicional português no coração de Almada Velha. Conhecido pelo bacalhau, pelos petiscos e por um ambiente acolhedor numa zona histórica do concelho.",
         json.dumps(["Comida portuguesa", "Bacalhau", "Ambiente histórico"]),
         json.dumps(["Almada Velha", "Cova da Piedade"]),
         "imagens/comer/tradicionais/sebastiao.jpg"),
        (4, "Casa das Artes", "bar", "Café e esplanada", "Cacilhas", "Cacilhas, Almada",
         "Espaço cultural e de restauração em Cacilhas, com esplanada com vista para o Tejo e Lisboa. Ideal para um café, petisco ou brunch junto ao cais do ferry.",
         json.dumps(["Esplanada", "Vista para Lisboa", "Brunch"]),
         json.dumps(["Cacilhas", "Boca do Vento"]),
         "imagens/comer/bares/cacilhas-cafes.jpg"),
        (5, "Waikiki", "bar", "Bar de praia", "Costa da Caparica", "Costa da Caparica, Almada",
         "Bar de praia icónico da Costa da Caparica, com música, caipirinhas e ambiente jovem mesmo no areal. Um dos pontos de encontro mais animados do verão na Caparica.",
         json.dumps(["Praia", "Ambiente jovem", "Música"]),
         json.dumps(["Costa da Caparica", "Praia da Morena"]),
         "imagens/comer/bares/waikiki.jpg"),
        (6, "Restaurante Ponto Final", "peixe", "Restaurante de peixe", "Cacilhas", "Rua do Ginjal, Cacilhas",
         "Um dos restaurantes mais emblemáticos de Cacilhas, situado à beira-rio com vista privilegiada para Lisboa. Famoso pelo peixe grelhado e marisco fresco, servidos em ambiente descontraído.",
         json.dumps(["Peixe grelhado", "Vista para Lisboa", "Beira-rio"]),
         json.dumps(["Cais de Cacilhas", "Elevador da Boca do Vento"]),
         "imagens/comer/peixe/ponto-final.jpg"),
        (7, "Restaurante O Farol", "peixe", "Restaurante de peixe", "Costa da Caparica", "Avenida General Humberto Delgado, Costa da Caparica",
         "Restaurante de referência na Costa da Caparica, especializado em peixe fresco e caldeirada. Ambiente familiar com esplanada e vista para o mar.",
         json.dumps(["Peixe fresco", "Caldeirada", "Esplanada"]),
         json.dumps(["Praia de São João", "Centro da Caparica"]),
         "imagens/comer/peixe/restaurante-farol.jpg"),
        (8, "Cervejaria Portugália de Almada", "peixe", "Restaurante de peixe", "Almada", "Forum Almada, Almada",
         "Cervejaria clássica portuguesa com vasta oferta de marisco, peixe e petiscos. Localizada no Forum Almada, combina a tradição com a conveniência.",
         json.dumps(["Marisco", "Cervejaria", "Petiscos"]),
         json.dumps(["Forum Almada", "Pragal"]),
         "imagens/comer/peixe/cervejaria-almada.jpg"),
        (9, "Tasca do Chico", "tradicional", "Restaurante tradicional", "Cacilhas", "Largo Alfredo Dinis, Cacilhas",
         "Tasca típica portuguesa com petiscos tradicionais, enchidos e pratos caseiros. Ambiente acolhedor e autêntico, ideal para quem procura sabores genuínos.",
         json.dumps(["Comida portuguesa", "Petiscos", "Ambiente típico"]),
         json.dumps(["Cais de Cacilhas", "Rua do Ginjal"]),
         "imagens/comer/tradicionais/tasca-chico.jpg"),
        (10, "Restaurante Solar dos Presuntos de Almada", "tradicional", "Restaurante tradicional", "Almada", "Centro de Almada",
         "Restaurante de cozinha tradicional portuguesa com destaque para pratos de carne, bacalhau e cozido à portuguesa. Porções generosas e preços acessíveis.",
         json.dumps(["Carne", "Bacalhau", "Cozido"]),
         json.dumps(["Jardim do Castelo", "Castelo de Almada"]),
         "imagens/comer/tradicionais/solar-presuntos.jpg"),
        (11, "O Trigueirinho", "tradicional", "Restaurante tradicional", "Trafaria", "Trafaria, Almada",
         "Restaurante tradicional na Trafaria, conhecido pela cozinha caseira e ambiente familiar. Especialidades incluem arroz de marisco e feijoada de choco.",
         json.dumps(["Comida caseira", "Arroz de marisco", "Familiar"]),
         json.dumps(["Porto de Trafaria", "Praia da Trafaria"]),
         "imagens/comer/tradicionais/trigueirinho.jpg"),
        (12, "Quiosque da Boca do Vento", "bar", "Café e esplanada", "Almada", "Miradouro Boca do Vento, Almada",
         "Quiosque com esplanada no miradouro Boca do Vento, oferecendo bebidas, snacks e gelados com vista panorâmica para Lisboa e o Tejo.",
         json.dumps(["Esplanada", "Vista panorâmica", "Gelados"]),
         json.dumps(["Elevador da Boca do Vento", "Casa da Cerca"]),
         "imagens/comer/bares/quiosque-boca-vento.jpg"),
        (13, "Bar da Praia da Sereia", "bar", "Bar de praia", "Costa da Caparica", "Praia da Sereia, Costa da Caparica",
         "Bar de praia com ambiente descontraído, cocktails, música ao vivo aos fins de semana e petiscos. Ponto de encontro popular entre surfistas.",
         json.dumps(["Cocktails", "Música ao vivo", "Surf"]),
         json.dumps(["Praia da Sereia", "Praia da Morena"]),
         "imagens/comer/bares/bar-sereia.jpg"),
        (14, "Café Central de Almada", "bar", "Café e esplanada", "Almada Velha", "Praça da Liberdade, Almada",
         "Café histórico no coração de Almada Velha, com esplanada na praça principal. Serve pastelaria tradicional, tostas e cafés de especialidade.",
         json.dumps(["Pastelaria", "Café", "Centro histórico"]),
         json.dumps(["Castelo de Almada", "Igreja de Santiago"]),
         "imagens/comer/bares/cafe-central.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO comer VALUES (?,?,?,?,?,?,?,?,?,?)", comer)

    # Cultura
    cultura = [
        (1, "Casa da Cerca", "arte", "Centro de Arte Contemporânea", "Almada", "Rua Casa da Cerca, Almada",
         "Centro de Arte Contemporânea situado num edifício histórico com jardim botânico e vista panorâmica sobre o Tejo e Lisboa. Alberga exposições de artistas nacionais e internacionais.",
         json.dumps(["Arte contemporânea", "Vista para o Tejo"]),
         json.dumps(["Casa da Cerca", "Jardim Botânico O Chão das Artes"]),
         "imagens/cultura/arte/casa-da-cerca.webp"),
        (2, "Teatro Municipal Joaquim Benite", "teatro", "Teatro", "Almada", "Praça de Portugal, Almada",
         "Principal sala de espetáculos de Almada, com programação regular de teatro, dança e música. Sede do afamado Festival Internacional de Teatro de Almada.",
         json.dumps(["Teatro", "Festival"]),
         json.dumps(["Teatro Municipal Joaquim Benite"]),
         "imagens/cultura/teatro/teatro-municipal-almada.jpg"),
        (3, "Fórum Municipal Romeu Correia", "teatro", "Espaço cultural multiusos", "Almada", "Almada",
         "Espaço cultural com programação diversificada que inclui teatro, música, cinema e eventos municipais.",
         json.dumps(["Eventos", "Cultura local"]),
         json.dumps(["Fórum Municipal Romeu Correia"]),
         "imagens/cultura/teatro/forum-romeu-correia.jpg"),
        (4, "Museu Naval de Almada", "patrimonio", "Museu", "Cacilhas", "Cacilhas, Almada",
         "Museu dedicado à história naval portuguesa, com peças, embarcações e documentos ligados à tradição marítima da margem sul do Tejo.",
         json.dumps(["História", "Marítimo"]),
         json.dumps(["Cacilhas"]),
         "imagens/cultura/patrimonio/museu-naval.jpg"),
        (5, "Almada Velha", "patrimonio", "Zona histórica", "Almada Velha", "Almada Velha, Almada",
         "Núcleo histórico de Almada com ruas medievais, miradouros, igrejas e o antigo castelo. Zona de grande valor patrimonial e identitário do concelho.",
         json.dumps(["Património", "Medieval"]),
         json.dumps(["Castelo de Almada", "Igreja de São João Baptista", "Boca do Vento"]),
         "imagens/cultura/patrimonio/almada-velha.jpg"),
        (6, "Galeria Municipal de Arte", "arte", "Galeria de arte", "Almada", "Centro de Almada",
         "Galeria de arte moderna e contemporânea com exposições rotativas de artistas nacionais e internacionais. Espaço dedicado à promoção da arte visual.",
         json.dumps(["Arte moderna", "Exposições", "Galeria"]),
         json.dumps(["Centro Cultural de Almada"]),
         "imagens/cultura/arte/galeria-municipal.jpg"),
        (7, "Atelier-Museu Júlio Pomar", "arte", "Museu", "Cacilhas", "Cacilhas, Almada",
         "Espaço dedicado à obra do pintor Júlio Pomar, um dos mais importantes artistas portugueses do século XX. Acervo permanente com pinturas, desenhos e esculturas.",
         json.dumps(["Arte contemporânea", "Pintura", "Escultura"]),
         json.dumps(["Cais de Cacilhas", "Rua do Ginjal"]),
         "imagens/cultura/arte/atelier-pomar.jpg"),
        (8, "Centro Cultural de Almada", "teatro", "Espaço cultural", "Almada", "Almada Centro",
         "Espaço polivalente que acolhe espetáculos de teatro, dança, música e cinema. Programação regular ao longo do ano com artistas nacionais.",
         json.dumps(["Espetáculos", "Dança", "Música"]),
         json.dumps(["Praça da Liberdade", "Jardim do Castelo"]),
         "imagens/cultura/teatro/centro-cultural.jpg"),
        (9, "Festival de Almada", "teatro", "Festival", "Almada", "Vários locais em Almada",
         "O Festival Internacional de Teatro de Almada é um dos mais prestigiados festivais de artes performativas em Portugal, realizado anualmente em julho.",
         json.dumps(["Festival", "Teatro internacional", "Julho"]),
         json.dumps(["Teatro Municipal", "Fórum Romeu Correia"]),
         "imagens/cultura/teatro/festival-almada.jpg"),
        (10, "Fragata D. Fernando II e Glória", "patrimonio", "Navio-museu", "Cacilhas", "Cais de Cacilhas",
         "Navio-museu atracado em Cacilhas, a última fragata de vela da Marinha Portuguesa. Construída em 1843, é uma peça única do património marítimo nacional.",
         json.dumps(["Navio-museu", "Marítimo", "Século XIX"]),
         json.dumps(["Cais de Cacilhas", "Museu Naval"]),
         "imagens/cultura/patrimonio/fragata-fernando.jpg"),
        (11, "Convento dos Capuchos", "patrimonio", "Convento", "Costa da Caparica", "Monte de Caparica",
         "Convento franciscano do século XVI com igreja e claustro. Recentemente restaurado, oferece visitas guiadas e eventos culturais em ambiente histórico.",
         json.dumps(["Convento", "Século XVI", "Restaurado"]),
         json.dumps(["Monte de Caparica", "Costa da Caparica"]),
         "imagens/cultura/patrimonio/convento-capuchos-cultura.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO cultura VALUES (?,?,?,?,?,?,?,?,?,?)", cultura)

    # Miradouros
    miradouros = [
        (1, "Cristo Rei", "Alto do Pragal", "Alto do Pragal, Almada",
         "Monumento icónico com vista de 360° sobre Lisboa, o Tejo e toda a área metropolitana. Inclui elevador panorâmico e plataforma de observação a 82 metros de altura.",
         1, 1, 1,
         json.dumps(["Vista 360°", "Religioso", "Monumento"]),
         json.dumps(["fotografia", "visita cultural", "família"]),
         "imagens/passear/miradouros/cristo-rei.jpg"),
        (2, "Boca do Vento", "Cacilhas", "Cacilhas, Almada",
         "Miradouro com elevador público sobre o Tejo, com vista direta para Lisboa e a Ponte 25 de Abril. Um dos locais mais fotogénicos e acessíveis da margem sul.",
         1, 1, 0,
         json.dumps(["Vista para Lisboa", "Ribeirinho"]),
         json.dumps(["fotografia", "passeio", "casal"]),
         "imagens/passear/miradouros/boca-do-vento.jpg"),
        (3, "Miradouro de Almada Velha", "Almada Velha", "Almada Velha, Almada",
         "Vista sobre o Tejo a partir do núcleo histórico de Almada, com enquadramento único entre as ruínas do castelo medieval e a frente ribeirinha.",
         0, 1, 0,
         json.dumps(["Vista histórica", "Medieval"]),
         json.dumps(["fotografia", "história", "passeio"]),
         "imagens/passear/miradouros/miradouro-almada-velha.jpg"),
        (4, "Miradouro da Costa da Caparica", "Costa da Caparica", "Costa da Caparica, Almada",
         "Vista sobre o oceano Atlântico e a extensa linha costeira da Caparica. Ideal para observar o pôr-do-sol sobre o mar.",
         1, 1, 1,
         json.dumps(["Vista para o Atlântico", "Pôr-do-sol"]),
         json.dumps(["fotografia", "relaxamento", "família"]),
         "imagens/passear/miradouros/miradouro-caparica.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO miradouros VALUES (?,?,?,?,?,?,?,?,?,?,?)", miradouros)

    # Historicos
    historicos = [
        (1, "Castelo de Almada", "Almada Velha", "Almada Velha, Almada", "Castelo medieval",
         "Ruínas do castelo medieval de Almada, com origem mourisca e reconstrução posterior. Está integrado no núcleo histórico e oferece vista sobre o Tejo.",
         0, 1,
         json.dumps(["Medieval", "Arqueologia", "Ruínas"]),
         json.dumps(["história", "fotografia", "arqueologia"]),
         "imagens/passear/historicos/castelo_de_almada.webp"),
        (2, "Casa da Cerca", "Almada", "Rua Casa da Cerca, Almada", "Edifício histórico / Centro de arte",
         "Antiga quinta histórica do século XVII, hoje reconvertida em centro de arte contemporânea. Inclui jardim botânico e vista panorâmica sobre o Tejo.",
         1, 1,
         json.dumps(["Século XVII", "Arte", "Jardim histórico"]),
         json.dumps(["arte", "história", "família"]),
         "imagens/passear/historicos/casa-da-cerca.webp"),
        (3, "Convento dos Capuchos", "Costa da Caparica", "Caparica, Almada", "Convento",
         "Convento franciscano do século XVI inserido numa paisagem natural de grande valor. Um dos exemplos mais bem preservados da arquitectura religiosa na margem sul.",
         0, 0,
         json.dumps(["Século XVI", "Religioso", "Franciscano"]),
         json.dumps(["história", "religião", "fotografia"]),
         "imagens/passear/historicos/convento_dos_capuchos_(almada).webp"),
        (4, "Igreja de Nossa Senhora do Cabo", "Almada Velha", "Almada Velha, Almada", "Igreja",
         "Igreja com grande valor histórico e religioso, integrada no núcleo antigo de Almada. Destaca-se pela arquitectura e pelo enquadramento junto às muralhas.",
         0, 1,
         json.dumps(["Religioso", "Património"]),
         json.dumps(["história", "religião", "arquitetura"]),
         "imagens/passear/historicos/igreja-nossa-senhora-cabo.jpg"),
        (5, "Museu Naval de Almada", "Cacilhas", "Cacilhas, Almada", "Museu",
         "Museu dedicado à história naval portuguesa e à tradição marítima da margem sul do Tejo, com embarcações, instrumentos e documentos históricos.",
         1, 1,
         json.dumps(["Marítimo", "Museu", "História"]),
         json.dumps(["história", "família", "educação"]),
         "imagens/passear/historicos/museu-naval.jpg"),
    ]
    c.executemany("INSERT OR REPLACE INTO historicos VALUES (?,?,?,?,?,?,?,?,?,?,?)", historicos)

    conn.commit()
    conn.close()
    print(f"Base de dados criada em: {DB_PATH}")


if __name__ == "__main__":
    init_db()
