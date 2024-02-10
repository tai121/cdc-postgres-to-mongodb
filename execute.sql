INSERT INTO movies (id, title, year, director, rating) VALUES (1, 'The Shawshank Redemption', 1994, 'Frank Darabont', 9.3);
INSERT INTO movies (id, title, year, director, rating) VALUES (2, 'The Godfather', 1972, 'Francis Ford Coppola', 9.2);
INSERT INTO movies (id, title, year, director, rating) VALUES (3, 'The Godfather: Part II', 1974, 'Francis Ford Coppola', 9.0);
INSERT INTO movies (id, title, year, director, rating) VALUES (4, 'The Dark Knight', 2008, 'Christopher Nolan', 9.0);
INSERT INTO movies (id, title, year, director, rating) VALUES (5, 'Interstellar', 2014, 'Christopher Nolan', 10);
UPDATE movies SET rating = 8 WHERE id=5;
DELETE FROM movies WHERE id = 4;