# Self joins
Any given table can be easily referenced multiple times using different aliases.
```SQL
-- Returns only people that live in SP and have the same name as people who live in PA
SELECT paulista.name
FROM person paulista
JOIN person sulista ON paulista.name = sulista.name AND sulista.state = 'PA'
WHERE paulista.state = 'SP';
```