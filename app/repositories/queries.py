from database import engine
from database.engine import Session
from sqlalchemy import text
from random import randint

def database_populate_students():
    """
    Popula a tabela Aluno com dados fictícios.

    Para cada aluno são gerados:
    - Nome
    - E-mail
    - CPF
    - Curso aleatório (id_curso entre 1 e 3)

    Os registros são inseridos na tabela Aluno e confirmados
    através de commit ao final da operação.
    """

    student_names = ["José", "Diego", "Alexandre", "Gustavo", "Yohan", "Leticia", "Daniel",
                    "Vitória", "Ingrid", "Ana Beatriz", "Wellington", "Miguel", "Bittar",
                    "Gabriel"]
    student_email = [f"{name.lower().replace(' ', '')}@gmail.com" for name in student_names]
    student_cpf = [
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
    "10101010101",
    "12121212121",
    "13131313131",
    "14141414141",
    "15151515151"
    ]

    with Session(engine) as session:
        for nome, email, cpf in zip(
            student_names,
            student_email,
            student_cpf
        ):
            session.execute(
                text("""
                    INSERT INTO Aluno(
                        nome,
                        cpf,
                        email,
                        id_curso
                    )
                    VALUES(
                        :nome,
                        :cpf,
                        :email,
                        :id_curso
                    )
                """),
                {
                    "nome": nome,
                    "cpf": cpf,
                    "email": email,
                    "id_curso": randint(1, 3)
                }
            )
        session.commit()



def database_populate_disciplines():
    """
    Popula a tabela Disciplina com disciplinas pré-definidas.

    Para cada disciplina é gerada uma carga horária aleatória
    entre 10 e 90 horas.

    Os registros são inseridos na tabela Disciplina e
    persistidos no banco através de commit.
    """

    disciplines = ["Calculo 1", "Física 1", "Quimica 1", "Algebra Linear", "Bioquimica", "Banco de Dados"]
    course_load = [randint(10, 90) for _ in range(len(disciplines))]

    with Session(engine) as session:
        for discipline, load in zip(disciplines, course_load):
            session.execute(
                text(
                    """
                    INSERT INTO disciplina(nome, carga_horaria)
                    VALUES (:nome, :carga_horaria)
                """
                ),
                {
                    "nome": discipline,
                    "carga_horaria": load
                }
            )
        
        session.commit()



def database_populate_courses():
    """
    Popula a tabela Curso com uma lista de cursos.

    Os cursos são inseridos individualmente na tabela Curso
    utilizando comandos SQL parametrizados.

    Após a inserção de todos os registros é realizado commit.
    """

    courses = [
        "Ciência da Computação",
        "Física",
        "Engenharia Química",
        "Filosofia",
        "Letras Japones",
        "Dança"
    ]

    with Session(engine) as session:
        for course in courses:
            session.execute(
                text("""
                    INSERT INTO Curso(nome)
                    VALUES (:nome)
                """),
                {
                    "nome": course
                }
            )
        session.commit()


def database_populate_enrollments():
    """
    Popula a tabela Matricula com matrículas fictícias.

    Cada aluno recebe uma matrícula em uma disciplina
    escolhida aleatoriamente.

    As matrículas são registradas para o ano de 2026
    e semestre 1.

    Após a inserção dos registros é realizado commit.
    """

    with Session(engine) as session:
        for aluno in range(1, 15):
            session.execute(
                text("""
                    INSERT INTO Matricula(
                        id_aluno,
                        id_disciplina,
                        ano,
                        semestre
                    )
                    VALUES(
                        :id_aluno,
                        :id_disciplina,
                        :ano,
                        :semestre
                    )
                """),
                {
                    "id_aluno": aluno,
                    "id_disciplina": randint(1, 6),
                    "ano": 2026,
                    "semestre": 1
                }
            )
        session.commit()


def select_5():
    """
    Retorna os alunos matriculados nos cursos:

    - Ciência da Computação
    - Física
    - Engenharia Química

    A consulta utiliza JOIN entre as tabelas Aluno e Curso
    para recuperar o nome do aluno e o respectivo curso.

    Returns:
        list: Lista contendo os registros retornados pela consulta.
    """

    with Session(engine) as session:
        result = session.execute(
            text("""
                SELECT
                    a.id_aluno,
                    a.nome AS aluno,
                    c.nome AS curso
                FROM Aluno a
                INNER JOIN Curso c
                    ON a.id_curso = c.id_curso
                WHERE c.nome IN (
                    'Ciência da Computação',
                    'Física',
                    'Engenharia Química'
                )
                ORDER BY
                    c.nome,
                    a.nome;
            """)
        )
        
        return result.fetchall()


def select_6():
    """
    Retorna os alunos matriculados em cada disciplina
    no semestre atual e no semestre anterior.

    A consulta utiliza JOIN entre as tabelas:
    - Matricula
    - Aluno
    - Disciplina

    São considerados os períodos:
    - 2026/1 (semestre atual)
    - 2025/2 (semestre anterior)

    Returns:
        list: Lista contendo os registros retornados pela consulta.
    """

    with Session(engine) as session:
        result = session.execute(
            text("""
                SELECT
                    d.nome AS disciplina,
                    a.nome AS aluno,
                    m.ano,
                    m.semestre
                FROM Matricula m
                INNER JOIN Aluno a
                    ON m.id_aluno = a.id_aluno
                INNER JOIN Disciplina d
                    ON m.id_disciplina = d.id_disciplina
                WHERE
                    (m.ano = 2026 AND m.semestre = 1)
                    OR
                    (m.ano = 2025 AND m.semestre = 2)
                ORDER BY
                    d.nome,
                    a.nome
            """)
        )

        return result.fetchall()


def main():
    database_populate_courses()
    database_populate_students()
    database_populate_disciplines()
    database_populate_enrollments()

    alunos_cursos = select_5()
    matriculas = select_6()

    print("\n=== SELECT 5 ===")
    for linha in alunos_cursos:
        print(linha)

    print("\n=== SELECT 6 ===")
    for linha in matriculas:
        print(linha)


if __name__ == '__main__':
    main()
