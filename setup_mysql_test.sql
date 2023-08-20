CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbhb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbhb_test_db' TO 'hbnb_dev'@'localhost';
GRANT SELECT on 'perfomance_schema' TO 'hbnb_dev'@'localhost';