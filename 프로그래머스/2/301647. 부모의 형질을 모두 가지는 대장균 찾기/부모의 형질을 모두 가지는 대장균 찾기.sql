-- 코드를 작성해주세요

select ed1.ID, ed1.GENOTYPE, (select ed.GENOTYPE from ECOLI_DATA ed
  where ed1.PARENT_ID = ed.ID) as PARENT_GENOTYPE from ECOLI_DATA ed1
where 
ed1.PARENT_ID is not null and 
(ed1.GENOTYPE & 
 (select ed.GENOTYPE from ECOLI_DATA ed
  where ed1.PARENT_ID = ed.ID)) = (select ed.GENOTYPE from ECOLI_DATA ed
  where ed1.PARENT_ID = ed.ID)
order by ed1.ID asc