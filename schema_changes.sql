-- CREATE DATABASE IF NOT EXISTS test;
-- CREATE DATABASE IF NOT EXISTS test2;

USE prog8850_db;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



