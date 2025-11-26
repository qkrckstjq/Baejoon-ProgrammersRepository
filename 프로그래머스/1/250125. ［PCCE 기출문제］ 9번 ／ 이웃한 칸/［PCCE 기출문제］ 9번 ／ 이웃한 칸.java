class Solution {
    public int solution(String[][] board, int h, int w) {
        int n = board.length;              // 보드 한 변의 길이
        int count = 0;                     // 같은 색 칸 개수

        // 상하좌우 방향 벡터
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};

        String curColor = board[h][w];     // 기준이 되는 색

        // 네 방향 체크
        for (int i = 0; i < 4; i++) {
            int nh = h + dh[i];
            int nw = w + dw[i];
            if (nh >= 0 && nh < n && nw >= 0 && nw < n) {
                if (curColor.equals(board[nh][nw])) {
                    count++;
                }
            }
        }

        return count;
    }
}
