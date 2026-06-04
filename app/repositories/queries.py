from database import engine
from database.engine import Session
from sqlalchemy import text
from random import randint

# Tenho que ver a criação do banco pra fazer alguns ajustes, na espera.
# Aluno tambem tem que ter a matricula, mas tenho que ver como ta no banco
def database_populate_students():
    # DADOS
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
        for nome, email, cpf in zip( # Uma query diferente para cada aluno com seus diferentes dados
            student_names,
            student_email,
            student_cpf
        ):
            session.execute( # Executa a query
                text("""
                    INSERT INTO aluno(nome, cpf, email)
                    VALUES (:nome, :cpf, :email)
                """),
                {
                    "nome": nome,
                    "cpf": cpf,
                    "email": email
                }
            )

        session.commit() # Commita no banco de dados


# Tenho que ver a criação do banco pra fazer alguns ajustes, na espera.
def database_populate_disciplines():
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


# Tenho que ver a criação do banco pra fazer alguns ajustes, na espera.
def database_populate_courses():
    courses = ["Ciência da Computação", "Física", "Engenharia Química"]
    conclusion = [4, 5, 5] # Em anos

    with Session(engine) as session:
        for course, c in zip(courses, conclusion):
            session.execute(
                text(
                    """
                    INSERT INTO curso(nome, conclusao)
                    VALUES (:nome, :conclusao)
                """
                ),
                {
                    "nome": course,
                    "conclusao": c
                }
            )
        
        session.commit()


def select_5(): # Crie um SQL que retorne os alunos matriculados em Ciencia da Computacao...
    pass


def select_6(): # Crie um SQL que retorne os alunos matriculados em cada disciplina...
    pass
