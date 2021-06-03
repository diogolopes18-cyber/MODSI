CREATE TABLE IF NOT EXISTS
ALUNOS_MODSI
(
    mec_aluno int PRIMARY KEY UNIQUE NOT NULL,
    pass varchar(255) NOT NULL,
    email varchar(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS
DIRETOR
(
    sigla varchar(5) PRIMARY KEY UNIQUE NOT NULL,
    pass varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS
ORIENTADOR
(
    sigla varchar(5) PRIMARY KEY UNIQUE NOT NULL,
    pass varchar(50) NOT NULL,
    email varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS
PROJETOS
(
    nome_projeto varchar(50) UNIQUE,
    status_project varchar(50),
    student_id int UNIQUE NOT NULL,
    sigla_orientador varchar(5) UNIQUE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES ALUNOS_MODSI (mec_aluno),
    FOREIGN KEY (sigla_orientador) REFERENCES ORIENTADOR (sigla)
);
