CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)

INSERT INTO users (username, email) VALUES
    ('noah amoo', 'noah@amoo.com'),
    ('jon smith', 'jon@smith.com'),
    ('bob jones', 'bob@jones.com');

INSERT INTO users (username, email)
VALUES (
    'username:character varying',
    'email:character@varying'
  );SELECT * FROM users