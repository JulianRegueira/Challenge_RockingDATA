-- =========================
-- CAPA PROCESSED
-- =========================

-- Tabla de plataformas
CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

-- Tabla de títulos (películas/series)
CREATE TABLE titles (
    title_id SERIAL PRIMARY KEY,
    show_id VARCHAR(50) UNIQUE,
    title VARCHAR(255),
    type VARCHAR(50),
    release_year INT,
    rating VARCHAR(50),
    duration_minutes INT,
    date_added DATE,
    description TEXT,
    platform_id INT REFERENCES platforms(platform_id)
);

-- Tabla de directores
CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

-- Tabla de actores
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

-- Relación N:M entre títulos y actores
CREATE TABLE title_actors (
    title_id INT REFERENCES titles(title_id),
    actor_id INT REFERENCES actors(actor_id),
    PRIMARY KEY (title_id, actor_id)
);

-- Relación 1:N entre títulos y directores
CREATE TABLE title_directors (
    title_id INT REFERENCES titles(title_id),
    director_id INT REFERENCES directors(director_id),
    PRIMARY KEY (title_id, director_id)
);

-- =========================
-- ÍNDICES
-- =========================
CREATE INDEX idx_titles_year ON titles(release_year);
CREATE INDEX idx_titles_platform ON titles(platform_id);
CREATE INDEX idx_actors_name ON actors(name);
CREATE INDEX idx_directors_name ON directors(name);
