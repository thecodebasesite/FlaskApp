CREATE DATABASE thecodebase;

show tables;

USE thecodebase;

CREATE TABLE users (
    uid INT(11) AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(20), 
    password VARCHAR(100), 
    email VARCHAR(50), 
    settings VARCHAR(32500), 
    tracking VARCHAR(32500), 
    rank INT(3)
);



CREATE TABLE visits (
    visit_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    time DATETIME,
    remote_addr VARCHAR(45),
    endpoint VARCHAR(50),
    FOREIGN KEY (uid) REFERENCES users(uid)
);

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'thecodebase'@'localhost' IDENTIFIED BY 'kikkeli97';

SET PASSWORD FOR 'username'@'localhost' = PASSWORD('password');

CREATE TABLE Score (
    score_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    time DATETIME,
    score INT,
    FOREIGN KEY (uid) REFERENCES users(uid)
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'thecodebase'
AND table_name = 'users';

