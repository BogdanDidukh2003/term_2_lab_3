CREATE DATABASE circus_show_db;

USE circus_show_db;

CREATE TABLE performance
(
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT NOT NULL,
    musicians_number INT NOT NULL,
    avg_ticket_price INT NOT NULL,
    PRIMARY KEY (id) 
);