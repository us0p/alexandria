```SQL
-- Using Subquery
select
    email Email
from
    (
        select 
            email, 
            count(*) c 
        from 
            Person p 
        group by 
            email
    )
where
    c > 1;

-- Using Having
select
    email Email
from
    Person p
group by
    email
having
    count(email) > 1;

-- Using CTE with Window function
with dpe as (
    select
        email,
        count(*) over (partition by email)
    from
        Person p
)
select
    distinct email Email
from
    dpe
where count >1;

```