CREATE DATABASE IF NOT EXISTS cine_db;
USE cine_db;

CREATE TABLE IF NOT EXISTS directores (
    id_director INT AUTO_INCREMENT PRIMARY KEY,
    director VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias (
    identificador INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS peliculas (
    identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    id_director INT NOT NULL,
    duracion INT NOT NULL,
    id_categoria INT NOT NULL,
    sinopsis TEXT NOT NULL,
    CONSTRAINT fk_peliculas_director
        FOREIGN KEY (id_director) REFERENCES directores (id_director),
    CONSTRAINT fk_peliculas_categoria
        FOREIGN KEY (id_categoria) REFERENCES categorias (identificador)
);
