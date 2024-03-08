CREATE TABLE IF NOT EXISTS bandas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    ano_formacao INT,
    integrantes INT,
    cidade_origem VARCHAR(100)
);

INSERT INTO bandas (nome, genero, ano_formacao, integrantes, cidade_origem) VALUES
('Coldplay', 'Pop/Rock', 1996, 4, 'Londres'),
('Queen', 'Rock', 1970, 4, 'Londres'),
('The Beatles', 'Rock', 1960, 4, 'Liverpool'),
('U2', 'Rock', 1976, 4, 'Dublin'),
('AC/DC', 'Rock', 1973, 5, 'Sydney');

CREATE TABLE IF NOT EXISTS musicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    duracao TIME,
    banda_id INT,
    FOREIGN KEY (banda_id) REFERENCES bandas(id)
);

INSERT INTO musicas (titulo, duracao, banda_id)
VALUES 
    ('Yellow', '00:04:29', 1),
    ('Fix You', '00:04:55', 1),
    ('The Scientist', '00:05:09', 1),
    ('Clocks', '00:05:07', 1),
    ('Paradise', '00:04:21', 1),
    ('Bohemian Rhapsody', '00:05:55', 2),
    ('We Will Rock You', '00:02:02', 2),
    ('Another One Bites the Dust', '00:03:35', 2),
    ('Under Pressure', '00:04:05', 2),
    ('Somebody to Love', '00:04:56', 2),
    ('Hey Jude', '00:07:11', 3),
    ('Let It Be', '00:03:50', 3),
    ('Yesterday', '00:02:05', 3),
    ('Come Together', '00:04:20', 3),
    ('Help!', '00:02:18', 3),
    ('With or Without You', '00:04:56', 4),
    ('One', '00:04:36', 4),
    ('Beautiful Day', '00:04:08', 4),
    ('Sunday Bloody Sunday', '00:04:42', 4),
    ('Where the Streets Have No Name', '00:05:38', 4),
    ('Back in Black', '00:04:15', 5),
    ('Highway to Hell', '00:03:29', 5),
    ('Thunderstruck', '00:04:53', 5),
    ('You Shook Me All Night Long', '00:03:30', 5),
    ('T.N.T.', '00:03:34', 5);