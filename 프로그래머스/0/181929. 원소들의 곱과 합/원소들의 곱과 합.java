class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int square = 1;
        for(int a : num_list) {
            sum += a;
            square *= a;
        }
            
        return square < sum * sum ? 1 : 0;
    }
}