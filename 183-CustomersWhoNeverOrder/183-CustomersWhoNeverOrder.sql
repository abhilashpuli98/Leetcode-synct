-- Last updated: 2/5/2026, 7:43:03 AM
# Write your MySQL query statement below
select name as Customers  from Customers where id not in(select customerId from Orders);
