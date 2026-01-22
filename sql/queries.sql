-- Considerando únicamente la plataforma de Netflix, ¿qué actor aparece más veces?

SELECT
    a.name AS actor,
    COUNT(*) AS apariciones
FROM processed.titles t
JOIN processed.platforms p 
    ON t.platform_id = p.platform_id
JOIN processed.title_actors ta 
    ON t.title_id = ta.title_id
JOIN processed.actors a
    ON ta.actor_id = a.actor_id
WHERE p.name = 'Netflix'
GROUP BY a.name
ORDER BY apariciones DESC
LIMIT 1;

-- RESPUESTA: "Anupam Kher"	44 veces

-- Top 10 de actores participantes considerando ambas plataformas en el 
año actual. Se aprecia flexibilidad.
SELECT
    a.name AS actor, 
    COUNT(*) AS apariciones
FROM processed.titles t
JOIN processed.title_actors ta 
    ON t.title_id = ta.title_id
JOIN processed.actors a 
    ON ta.actor_id = a.actor_id
WHERE t.release_year BETWEEN 2020 AND 2021
GROUP BY a.name
ORDER BY apariciones DESC
LIMIT 10;

/*
RESPUESTA:
"Jim Cummings"	23
"Fortune Feimster"	15
"Jeff Bennett"	14
"Tony Hale"	14
"David Spade"	13
"London Hughes"	12
"Walt Disney"	12
"Raven-Symoné"	11
"Grey Griffin"	10
"Dave Goelz"	9 
