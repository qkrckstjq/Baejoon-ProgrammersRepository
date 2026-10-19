# Write your MySQL query statement below
with r as (
    select * from (
        select
        *,
        FIRST_VALUE(product_name) over(partition by store_id order by price) as cheapest_product,
        FIRST_VALUE(product_name) over(partition by store_id order by price desc) as most_exp_product,
        FIRST_VALUE(quantity) over(partition by store_id order by price) /
        FIRST_VALUE(quantity) over(partition by store_id order by price desc) as imbalance_ratio
        from inventory i
    ) a
    group by a.store_id
    having count(*) >= 3
)
select s.store_id, s.store_name, s.location, r.most_exp_product, r.cheapest_product, round(r.imbalance_ratio, 2) as imbalance_ratio from r
left join stores s
on r.store_id = s.store_id
where r.imbalance_ratio > 1
order by r.imbalance_ratio desc, s.store_name asc
