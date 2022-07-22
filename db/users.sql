DROP DATABASE IF EXISTS ss_users;
CREATE DATABASE ss_users;
USE ss_users;

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id     INTEGER         AUTO_INCREMENT,
    email       VARCHAR(63)     NOT NULL,
    username    VARCHAR(63)     NOT NULL,
    password    VARCHAR(63)     NOT NULL,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

INSERT INTO users(email, username, password) VALUES
    ("fakeemail@site.com", "FakeUser72", "puppies"),
    ("cactusspikes@succ.com", "SucculentLover23", "spikey");
