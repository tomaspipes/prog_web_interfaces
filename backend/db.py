import sqlite3
import json
import os


DB_PATH = os.path.join(os.path.dirname(__file__), "almada.db")


def get_db():
    """Abre uma ligação à base de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def query_db(query, args=(), one=False):
    """Executa uma query e devolve os resultados como lista de dicts."""
    conn = get_db()
    cur = conn.execute(query, args)
    rows = cur.fetchall()
    conn.close()

    result = [dict(row) for row in rows]

    # Desserializar campos JSON (tags, locais, ideal_para)
    for row in result:
        for key in ("tags", "locais", "ideal_para"):
            if key in row and isinstance(row[key], str):
                try:
                    row[key] = json.loads(row[key])
                except (json.JSONDecodeError, TypeError):
                    pass

        # Converter campos booleanos (SQLite armazena como 0/1)
        for key in ("acessivel", "estacionamento", "restauracao",
                     "transportes", "familias"):
            if key in row and row[key] is not None:
                row[key] = bool(row[key])

    if one:
        return result[0] if result else None
    return result
