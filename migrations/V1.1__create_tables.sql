BEGIN;

CREATE TABLE users (
    id SERIAL NOT NULL,
    name VARCHAR NOT NULL
);

INSERT INTO users (name) values ("nikhil");

COMMIT;