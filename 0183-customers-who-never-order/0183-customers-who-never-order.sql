# Write your MySQL query statement below
SELECT
   Customers.name as 'Customers'
FROM 
   Customers
     LEFT OUTER JOIN 
   Orders
     ON Customers.id = Orders.customerId
WHERE 
   Orders.id is Null;
   

    