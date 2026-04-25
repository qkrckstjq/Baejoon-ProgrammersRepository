-- 코드를 작성해주세요
select ii.ITEM_ID, ii.ITEM_NAME, ii.RARITY from ITEM_TREE it
left join ITEM_INFO ii
on it.ITEM_ID = ii.ITEM_ID
where PARENT_ITEM_ID in 
    (select ii.ITEM_ID from ITEM_INFO ii where ii.RARITY = "RARE")
order by ii.ITEM_ID desc
