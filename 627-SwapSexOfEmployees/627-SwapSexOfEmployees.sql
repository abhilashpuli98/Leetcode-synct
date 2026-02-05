-- Last updated: 2/5/2026, 7:41:46 AM
# Write your MySQL query statement below
update salary
set sex =  case when sex="f" then "m"
when sex = "m" then "f"
end;