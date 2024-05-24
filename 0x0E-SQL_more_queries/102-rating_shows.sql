-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, IFNULL(SUM(tv_show_ratings.rate), 0) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
ORDER BY rating_sum DESC;
