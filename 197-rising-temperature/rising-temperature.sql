# Write your MySQL query statement below
select d.id as ID
from Weather as w left join Weather as d
on DATE_ADD(w.recordDate, INTERVAL 1 DAY) = d.recordDate
where w.temperature < d.temperature;