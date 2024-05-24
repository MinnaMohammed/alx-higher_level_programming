-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rating) AS rating_sum
FROM tv_show_ratings
GROUP BY title
ORDER BY rating_sum DESC;
