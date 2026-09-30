# Write your MySQL query statement below
with a as (
    -- select *, count(d.lead_id) as unique_leads, count(d.partner_id) as unique_partners from DailySales d
    -- group by d.date_id, d.make_name, d.lead_id

    -- union all

    select d.date_id, d.make_name, count(distinct d.lead_id) as unique_leads, count(distinct d.partner_id) as unique_partners from DailySales d
    group by d.date_id, d.make_name
)
select * from a
-- where a.make_name = 'toyota'
-- select a.date_id, a.make_name, max(a.unique_leads), max(a.unique_partners) from a
-- group by a.date_id, a.make_name

