-- Last updated: 2/5/2026, 7:43:06 AM
# Write your MySQL query statement below
select email from Person group by email having count(email)>1;