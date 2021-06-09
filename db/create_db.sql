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
    nome_projeto varchar(50) UNIQUE PRIMARY KEY,
    status_project varchar(50),
    student_id int UNIQUE NOT NULL,
    sigla_orientador varchar(5) UNIQUE NOT NULL, 
    FOREIGN KEY (student_id) REFERENCES ALUNOS_MODSI (mec_aluno),
    FOREIGN KEY (sigla_orientador) REFERENCES ORIENTADOR (sigla)
);

CREATE TABLE IF NOT EXISTS
ORIENTADOR_SUGGESTIONS
(
    nome_projeto varchar(50) UNIQUE NOT NULL,
    id_orientador varchar(5) UNIQUE NOT NULL,
    description_project TEXT NOT NULL,
    FOREIGN KEY (id_orientador) REFERENCES ORIENTADOR (sigla)
);

CREATE TABLE IF NOT EXISTS
GRADES
(
    nota int,
    student int UNIQUE NOT NULL,
    project varchar(50) UNIQUE,
    FOREIGN KEY (student) REFERENCES ALUNOS_MODSI (mec_aluno),
    FOREIGN KEY (project) REFERENCES PROJETOS (nome_projeto)
);

