CREATE OR REPLACE FUNCTION processed.top5_movies_by_year(p_year INT)
RETURNS TABLE (
    title_id INT,
    title VARCHAR(255),
    duration_minutes INT,
    release_year INT
) AS $$
BEGIN
    RETURN QUERY
    SELECT t.title_id, t.title, t.duration_minutes, t.release_year
    FROM processed.titles t
    WHERE t.release_year = p_year
      AND t.type = 'Movie'
      AND t.duration_minutes IS NOT NULL
    ORDER BY t.duration_minutes DESC
    LIMIT 5;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM processed.top5_movies_by_year(2021);
/*
TITLE_ID, TITLE, DURATION_MINUTES, RELEASED_YEAR
718	"Headspace: Unwind Your Mind"	273	2021
688	"Jagame Thandhiram"	159	2021
1231	"Aelay"	151	2021
854	"Army of the Dead"	148	2021
80	"Tughlaq Durbar (Telugu)"	145	2021
