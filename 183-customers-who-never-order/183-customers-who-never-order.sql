# Write your MySQL query statement below
SELECT c.name as 'Customers'
FROM Customers c
WHERE c.id not in (
    SELECT customerId FROM Orders
);