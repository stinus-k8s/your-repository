-- init.sql
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT IGNORE INTO employees (name) VALUES ('test'), ('Bob'), ('Charlie');

