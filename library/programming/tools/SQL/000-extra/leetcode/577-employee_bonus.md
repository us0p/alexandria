```SQL
select
    e.name,
    b.bonus
from 
    Employee e
left join
    Bonus b
on 
    b.empId = e.empId
where
    b.bonus is null
or
    b.bonus < 1000;
```
- Uses `left join` to join the whole table at the left.
- Uses `where` to include also unmatched rows.