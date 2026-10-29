"""
personagens.py - Funções da tabela PERSONAGENS.

Colunas: id, nome, nivel, jogador_id, classe_id

jogador_id e classe_id são CHAVES ESTRANGEIRAS: guardam o id de um
jogador e de uma classe. Para mostrar o APELIDO do jogador e o NOME da
classe, juntamos as tabelas com JOIN.

As consultas (buscar_por_id, buscar_por_nome e listar) devolvem
as colunas nesta ordem, que é a ordem que o main.py mostra na tela:
    (id, nome, nivel, apelido do jogador, nome da classe)
"""

# Parte comum das consultas.
CONSULTA = """
    SELECT personagens.id, personagens.nome, personagens.nivel,
           jogadores.apelido, classes.nome
    FROM personagens
    JOIN jogadores ON jogadores.id = personagens.jogador_id
    JOIN classes ON classes.id = personagens.classe_id
"""


def incluir(conn, nome, nivel, jogador_id, classe_id):
    """Insere um personagem e devolve o id gerado."""
    cursor = conn.execute(
        "INSERT INTO personagens (nome, nivel, jogador_id, classe_id) "
        "VALUES (?, ?, ?, ?)",
        (nome, nivel, jogador_id, classe_id))
    conn.commit()
    return cursor.lastrowid


def buscar_por_id(conn, id):
    """Devolve UMA linha, ou None."""
    cursor = conn.execute(CONSULTA + " WHERE personagens.id = ?", (id,))
    return cursor.fetchone()


def buscar_por_nome(conn, nome):
    """Devolve uma LISTA com os personagens cujo nome contém o texto."""
    cursor = conn.execute(
        CONSULTA + " WHERE personagens.nome LIKE ? ORDER BY personagens.nome",
        ("%" + nome + "%",))
    return cursor.fetchall()


def listar(conn):
    """Devolve uma LISTA com todos os personagens."""
    cursor = conn.execute(CONSULTA + " ORDER BY personagens.id")
    return cursor.fetchall()
