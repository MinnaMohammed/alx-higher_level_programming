--  A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;
