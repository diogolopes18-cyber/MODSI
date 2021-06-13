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
    student_id int NOT NULL,
    sigla_orientador varchar(5) NOT NULL,
    make_public boolean, 
    FOREIGN KEY (student_id) REFERENCES ALUNOS_MODSI (mec_aluno),
    FOREIGN KEY (sigla_orientador) REFERENCES ORIENTADOR (sigla)
);

CREATE TABLE IF NOT EXISTS
ORIENTADOR_SUGGESTIONS
(
    nome_projeto varchar(50) UNIQUE NOT NULL,
    id_orientador varchar(5) NOT NULL,
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

--#####INSERT RANDOM VALUES FOR TESTING PURPOSES####--
INSERT INTO ALUNOS_MODSI (mec_aluno, pass, email) VALUES (1180900, 'test123', '1180900@isep.ipp.pt') ON CONFLICT DO NOTHING;

INSERT INTO ORIENTADOR (sigla, pass, email) VALUES ('crc', 'Yolo123%', 'crc@isep.ipp.pt') ON CONFLICT DO NOTHING;
INSERT INTO ORIENTADOR (sigla, pass, email) VALUES ('mjs', 'hello123', 'mjs@isep.ipp.pt') ON CONFLICT DO NOTHING;

INSERT INTO PROJETOS (nome_projeto, status_project, student_id, sigla_orientador) 
    VALUES ('A new approach to real time systems', 'to_approve', 1180900, 'crc') 
    ON CONFLICT DO NOTHING;

INSERT INTO ORIENTADOR_SUGGESTIONS (nome_projeto, id_orientador, description_project) 
    VALUES ('Robotic arm', 'crc', 'Develop a robotic arm with 6 DOF using a STM32 microcontroller')
    ON CONFLICT DO NOTHING;