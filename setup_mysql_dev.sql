-- Create setup script for MYSQL development server
-- Create necessary databases and users 

-- create hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user hbnb_dev if not exist with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
