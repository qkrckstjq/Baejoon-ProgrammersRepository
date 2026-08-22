# Write your MySQL query statement below
select p.firstName, p.LastName, a.city, a.state from Person p
left join (select personId, city, state from Address) a
on p.personId = a.personId