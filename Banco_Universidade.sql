-- ============================================================
-- BANCO DE DADOS: Banco_Universidade
-- ============================================================

CREATE DATABASE Banco_Universidade;

USE Banco_Universidade;

-- ============================================================
-- TABELA CURSO
-- ============================================================

CREATE TABLE Curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- ============================================================
-- TABELA ALUNO
-- Cada aluno pertence a um curso
-- ============================================================

CREATE TABLE Aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    email VARCHAR(100),
    id_curso INT NOT NULL,

    FOREIGN KEY (id_curso) REFERENCES Curso(id_curso)
);

-- ============================================================
-- TABELA DISCIPLINA
-- ============================================================

CREATE TABLE Disciplina (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

-- ============================================================
-- TABELA MATRICULA
-- Liga Aluno com Disciplina
-- Guarda o ano e semestre da matrícula
-- ============================================================

CREATE TABLE Matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_disciplina INT NOT NULL,
    ano INT NOT NULL,
    semestre INT NOT NULL,

    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id_disciplina)
);

-- ============================================================
-- POPULAR O BANCO COM CURSOS
-- ============================================================

INSERT INTO Curso (nome) VALUES
('Ciencia da Computacao'),
('Fisica'),
('Engenharia Quimica');

-- ============================================================
-- POPULAR O BANCO COM DISCIPLINAS
-- ============================================================

INSERT INTO Disciplina (nome, carga_horaria) VALUES
('Calculo 1', 80),
('Fisica 1', 80),
('Quimica 1', 80),
('Algebra Linear', 80),
('Bioquimica', 80),
('Banco de Dados', 80);

-- ============================================================
-- POPULAR O BANCO COM 10 ALUNOS
-- ============================================================

INSERT INTO Aluno (nome, cpf, email, id_curso) VALUES
('Ana Silva', '111.111.111-11', 'ana@email.com', 1),
('Bruno Santos', '222.222.222-22', 'bruno@email.com', 1),
('Carla Oliveira', '333.333.333-33', 'carla@email.com', 1),
('Joao Pereira', '000.000.000-00', 'joao@email.com', 1),
('Daniel Souza', '444.444.444-44', 'daniel@email.com', 2),
('Eduarda Lima', '555.555.555-55', 'eduarda@email.com', 2),
('Felipe Costa', '666.666.666-66', 'felipe@email.com', 2),
('Gabriela Rocha', '777.777.777-77', 'gabriela@email.com', 3),
('Henrique Alves', '888.888.888-88', 'henrique@email.com', 3),
('Isabela Martins', '999.999.999-99', 'isabela@email.com', 3);

-- ============================================================
-- POPULAR O BANCO COM MATRÍCULAS
-- Semestre atual: 2026 / 1
-- Semestre passado: 2025 / 2
-- ============================================================

INSERT INTO Matricula (id_aluno, id_disciplina, ano, semestre) VALUES
-- Semestre atual: 2026/1

-- Ciencia da Computacao
(1, 1, 2026, 1), -- Ana em Calculo 1
(1, 6, 2026, 1), -- Ana em Banco de Dados
(2, 1, 2026, 1), -- Bruno em Calculo 1
(2, 4, 2026, 1), -- Bruno em Algebra Linear
(3, 6, 2026, 1), -- Carla em Banco de Dados
(3, 4, 2026, 1), -- Carla em Algebra Linear
(4, 1, 2026, 1), -- Joao em Calculo 1
(4, 6, 2026, 1), -- Joao em Banco de Dados

-- Fisica
(5, 2, 2026, 1), -- Daniel em Fisica 1
(5, 4, 2026, 1), -- Daniel em Algebra Linear
(6, 2, 2026, 1), -- Eduarda em Fisica 1
(7, 4, 2026, 1), -- Felipe em Algebra Linear

-- Engenharia Quimica
(8, 3, 2026, 1), -- Gabriela em Quimica 1
(8, 5, 2026, 1), -- Gabriela em Bioquimica
(9, 3, 2026, 1), -- Henrique em Quimica 1
(10, 5, 2026, 1), -- Isabela em Bioquimica

-- Semestre passado: 2025/2

-- Ciencia da Computacao
(1, 4, 2025, 2), -- Ana em Algebra Linear
(2, 6, 2025, 2), -- Bruno em Banco de Dados
(3, 1, 2025, 2), -- Carla em Calculo 1
(4, 1, 2025, 2), -- Joao em Calculo 1

-- Fisica
(5, 2, 2025, 2), -- Daniel em Fisica 1
(6, 4, 2025, 2), -- Eduarda em Algebra Linear
(7, 2, 2025, 2), -- Felipe em Fisica 1

-- Engenharia Quimica
(8, 3, 2025, 2), -- Gabriela em Quimica 1
(9, 5, 2025, 2), -- Henrique em Bioquimica
(10, 3, 2025, 2); -- Isabela em Quimica 1

-- ============================================================
-- CONSULTA:
-- Retorna os alunos matriculados em:
-- Ciencia da Computacao, Fisica e Engenharia Quimica
-- ============================================================

SELECT 
    a.id_aluno,
    a.nome AS aluno,
    c.nome AS curso
FROM Aluno a
INNER JOIN Curso c 
    ON a.id_curso = c.id_curso
WHERE c.nome IN (
    'Ciencia da Computacao',
    'Fisica',
    'Engenharia Quimica'
)
ORDER BY 
    c.nome,
    a.nome;

-- ============================================================
-- CONSULTA:
-- Retorna os alunos matriculados em cada disciplina
-- no semestre atual e no semestre passado
-- ============================================================

SELECT 
    CASE
        WHEN m.ano = 2026 AND m.semestre = 1 THEN 'Semestre atual'
        WHEN m.ano = 2025 AND m.semestre = 2 THEN 'Semestre passado'
    END AS periodo,

    d.nome AS disciplina,
    a.nome AS aluno,
    c.nome AS curso,
    m.ano,
    m.semestre

FROM Matricula m
INNER JOIN Aluno a 
    ON m.id_aluno = a.id_aluno
INNER JOIN Curso c 
    ON a.id_curso = c.id_curso
INNER JOIN Disciplina d 
    ON m.id_disciplina = d.id_disciplina

WHERE 
    (m.ano = 2026 AND m.semestre = 1)
    OR
    (m.ano = 2025 AND m.semestre = 2)

ORDER BY 
    m.ano DESC,
    m.semestre DESC,
    d.nome,
    a.nome;
