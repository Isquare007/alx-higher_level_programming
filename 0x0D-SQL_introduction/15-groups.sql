-- display records with the same score in the table second_table

SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
GROUP BY score DESC
