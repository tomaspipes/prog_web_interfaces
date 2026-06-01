import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS pontos_interesse")
cursor.execute("DROP TABLE IF EXISTS categorias")

cursor.execute("""
               CREATE TABLE categorias (
                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                           nome TEXT NOT NULL
               )
               """)

cursor.execute("""
               CREATE TABLE pontos_interesse (
                                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                 nome TEXT NOT NULL,
                                                 descricao TEXT NOT NULL,
                                                 localizacao TEXT NOT NULL,
                                                 imagem TEXT,
                                                 categoria_id INTEGER NOT NULL,
                                                 FOREIGN KEY (categoria_id) REFERENCES categorias(id)
               )
               """)

categorias = [
    ("Património Religioso",),
    ("Castelos e Fortificações",),
    ("Quintas e Palácios",)
]

cursor.executemany("INSERT INTO categorias (nome) VALUES (?)", categorias)

pontos = [
    ("Santuário Nacional de Cristo Rei", "Monumento religioso e miradouro emblemático sobre Lisboa e o Tejo.", "Almada", "imagens/santuario_nacional_de_cristo_rei_(almada).webp", 1),
    ("Convento dos Capuchos", "Antigo convento com valor histórico e ligação à paisagem natural de Almada.", "Almada", "imagens/convento_dos_capuchos_(almada).webp", 1),
    ("Convento de São Paulo", "Edifício religioso histórico situado em Almada.", "Almada", "imagens/convento_de_sao_paulo_(almada).webp", 1),
    ("Monte da Cruz", "Local associado ao património religioso e paisagístico da Charneca de Caparica.", "Charneca de Caparica", "imagens/monte_da_cruz_(charneca_de_caparica).webp", 1),

    ("Castelo de Almada", "Estrutura histórica ligada à defesa e observação do estuário do Tejo.", "Almada", "imagens/castelo_de_almada.webp", 2),
    ("Forte de Nossa Senhora da Saúde da Trafaria", "Fortificação histórica situada na Trafaria.", "Trafaria", "imagens/forte_de_nossa_senhora_da_saude_da_trafaria.webp", 2),
    ("Forte de Almada", "Estrutura defensiva associada à proteção da margem sul do Tejo.", "Almada", "imagens/forte_de_almada.webp", 2),
    ("Zona ribeirinha da Trafaria", "Área com valor histórico e relação direta com a defesa e circulação no Tejo.", "Trafaria", "imagens/trafaria.webp", 2),

    ("Palácio da Cerca", "Espaço histórico e cultural com jardins e vista sobre Lisboa.", "Almada", "imagens/palacio_da_cerca_(almada).webp", 3),
    ("Solar dos Zagallos", "Antiga quinta senhorial com valor patrimonial e cultural.", "Sobreda", "imagens/solar_dos_zagallos_(sobreda).webp", 3),
    ("Quinta da Fidalga", "Quinta histórica situada no Seixal, associada ao património local.", "Seixal", "imagens/quinta_da_fidalga_(seixal).webp", 3),
    ("Frente ribeirinha do Seixal", "Espaço urbano e paisagístico ligado ao rio e à história local.", "Seixal", "imagens/frente_ribeirinha_seixal.webp", 3)
]

cursor.executemany("""
                   INSERT INTO pontos_interesse (nome, descricao, localizacao, imagem, categoria_id)
                   VALUES (?, ?, ?, ?, ?)
                   """, pontos)

conn.commit()
conn.close()

print("Base de dados criada com sucesso.")