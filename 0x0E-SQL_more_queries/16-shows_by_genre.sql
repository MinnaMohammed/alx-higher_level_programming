-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, COALESCE(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;
