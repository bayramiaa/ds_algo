SELECT g.name, 
       AVG(gc.genre_count) avg_genres, 
       MAX(gc.genre_count) max_genres
FROM genres g
INNER JOIN (
    SELECT movie_id, 
           genre_id, 
           COUNT(genre_id) over (partition BY movie_id) genre_count
    FROM genres_movies
    )
AS gc ON g.id = gc.genre_id
GROUP BY g.name
ORDER BY avg_genres DESC;
