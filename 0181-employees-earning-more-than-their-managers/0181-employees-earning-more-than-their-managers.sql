# Write your MySQL query statement below
SELECT
  emp_1.name AS 'Employee'
FROM 
  Employee AS emp_1,
  Employee AS emp_2
WHERE 
  emp_1.managerId = emp_2.id
      AND emp_1.salary > emp_2.Salary;

