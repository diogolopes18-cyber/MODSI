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
PROJETOS
(
    nome_projeto varchar(50) UNIQUE,
    status_project varchar(50)
);

CREATE TABLE IF NOT EXISTS
INFO_PROJETOS
(
    sigla_resp varchar(5) UNIQUE NOT NULL,
    departamento varchar(50),
    FOREIGN KEY (sigla_resp) REFERENCES DIRETOR (sigla)
);
