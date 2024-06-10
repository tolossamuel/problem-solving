# Write your MySQL query statement below
select v.customer_id, count(v.customer_id) as count_no_trans
from Transactions as t
right join Visits as v
on t.visit_id = v.visit_id where t.transaction_id IS NULL
GROUP BY v.customer_id;
;