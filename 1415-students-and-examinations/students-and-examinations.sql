# Write your MySQL query statement below
select S.student_id as student_id, S.student_name as student_name,S.subject_name as subject_name, ifnull(count(e.subject_name),0) as attended_exams from
(select s1.student_id,s1.student_name,s2.subject_name from Students as s1 cross join Subjects as s2) as S  
left join Examinations as e on S.student_id = e.student_id and S.subject_name = e.subject_name
group by S.student_id,S.subject_name 
order by S.student_id,S.subject_name