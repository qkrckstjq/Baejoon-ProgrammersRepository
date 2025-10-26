class Solution {
    public int solution(int n) {
        int[] board = new int[101];
        int num = 1;
        for(int i = 1; i <= 100; i++) {
            while(num % 3 == 0 || Integer.toString(num).contains("3")) num++;
            board[i] = num;
            num += 1;
        }
        // for(int q : board) System.out.println(q);
        return board[n];
    }
}