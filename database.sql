-- SQL Schema for Student Records
CREATE DATABASE IF NOT EXISTS school_db;
USE school_db;

CREATE TABLE IF NOT EXISTS marks (
    roll_no INT PRIMARY KEY,
    student_name VARCHAR(100),
    physics INT,
    chemistry INT,
    maths INT,
    total_percentage DECIMAL(5,2)
);

-- Sample Data Entry
INSERT INTO marks (roll_no, student_name, physics, chemistry, maths, total_percentage)
VALUES 
(101, 'Ishanth', 92, 88, 95, 91.67),
(102, 'Aditya', 75, 80, 70, 75.00);

-- Query to find top performers
SELECT * FROM marks WHERE total_percentage > 90;
