-- List of all cities that are in database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
  FROM cities
       INNER JOIN states
       ON cities.state_id = states.id
 ORDER BY cities.id;
