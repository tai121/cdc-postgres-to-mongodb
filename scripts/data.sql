
CREATE TABLE IF NOT EXISTS movies (
    id bigint PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INTEGER NOT NULL,
    director VARCHAR(255) NOT NULL,
    rating DECIMAL NOT NULL
);

