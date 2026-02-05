-- Last updated: 2/5/2026, 7:41:09 AM
# Write your MySQL query statement below
select player_id,MIN(event_date) as first_login from Activity group by player_id;
