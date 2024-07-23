# Write your MySQL query statement below
select machine_id, round(abs(timestamp_sum - (2 * timestamp))/processing_time,3) as processing_time
from 

(select machine_id, sum(timestamp) as timestamp_sum,timestamp,processing_time from

(select  machine_id, sum(timestamp) as timestamp, count(machine_id) as processing_time
from Activity group by machine_id, activity_type) as result
group by machine_id) as ans 