-- Create setup script for MYSQL test server
-- Create necessary databases and users 

-- create hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user hbnb_dev if not exist with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privileges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
