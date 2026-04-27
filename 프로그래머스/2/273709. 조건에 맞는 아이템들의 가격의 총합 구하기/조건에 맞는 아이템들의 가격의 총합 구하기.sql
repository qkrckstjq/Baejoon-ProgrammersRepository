-- 코드를 작성해주세요
select SUM(ii.PRICE) as TOTAL_PRICE from ITEM_INFO ii
where ii.RARITY = "LEGEND"