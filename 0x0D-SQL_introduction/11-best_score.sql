-- list all the records of the second table with score above 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
