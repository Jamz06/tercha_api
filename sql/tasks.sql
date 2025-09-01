-- Получить список задач по всем собакам владельца

select
	t.id, d.name, c.name, s.name
from 
	task t
	left join card c on c.id = t.card
	,
	dog d,
	task_status s
where 
	d.owner_id = :owner_id
	AND t.dog = d.id
	and s.id = t.status
	and s.task_closed = 'False';
