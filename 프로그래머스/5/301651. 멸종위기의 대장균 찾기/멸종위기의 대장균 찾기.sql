# -- 코드를 작성해주세요

with RECURSIVE generations as (
    select
    ID,
    PARENT_ID,
    GENOTYPE,
    1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select
    e.ID,
    e.PARENT_ID,
    e.GENOTYPE,
    (g.GENERATION + 1) as GENERATION
    from ECOLI_DATA e
    join generations g
    on e.PARENT_ID = g.ID
    # join generations g
    # on (p.GENOTYPE & e.GENOTYPE) = e.GENOTYPE
)
select count(*) as COUNT, g.GENERATION from generations g
left join (
    select g1.ID from generations g1
    join generations g2
    on (g1.ID = g2.PARENT_ID)
    # where (
    #     select count(*) from generations g
    #     where g.GENERATION = (g1.GENERATION + 1)
    # ) = 0 or (
    #     select count(*) from generations g
    #     where g.ID = (g1.PARENT_ID)
    # ) = 0
    # order by g1.GENERATION asc
    ) h_c
on g.ID = h_c.ID
where h_c.ID is null
group by g.GENERATION
order by g.GENERATION







# select * from (select * from ECOLI_DATA p
# where p.PARENT_ID is null) p
# left join (select * from ECOLI_DATA where PARENT_ID is not null) c
# on (p.GENOTYPE & c.GENOTYPE) != c.GENOTYPE

# select * from ECOLI_DATA