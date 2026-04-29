-- 코드를 작성해주세요
select ii.ITEM_ID, ii.ITEM_NAME, ii.RARITY from ITEM_INFO ii
left join ITEM_TREE it
on ii.ITEM_ID = it.PARENT_ITEM_ID
where it.PARENT_ITEM_ID is NULL
order by ii.ITEM_ID desc