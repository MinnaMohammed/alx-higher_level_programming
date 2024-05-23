-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT
    tv_shows.title,
    (SELECT GROUP_CONCAT(tv_genres.name SEPARATOR ', ')
     FROM tv_genres
     JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
     WHERE tv_show_genres.show_id = tv_shows.id) AS genres
FROM
    tv_shows
ORDER BY
    tv_shows.title ASC;

