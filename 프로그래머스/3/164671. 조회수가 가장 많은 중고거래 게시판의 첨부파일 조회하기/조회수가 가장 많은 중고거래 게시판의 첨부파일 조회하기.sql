-- 코드를 입력하세요
SELECT
CONCAT("/home/grep/src/", ub.BOARD_ID, "/", uf.FILE_ID, uf.FILE_NAME, uf.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD ub
left join USED_GOODS_FILE uf
on ub.BOARD_ID = uf.BOARD_ID
where (select MAX(VIEWS) from USED_GOODS_BOARD) = ub.VIEWS