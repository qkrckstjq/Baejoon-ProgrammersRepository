class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for(int q = i; q <= j; q++) {
            String str = String.valueOf(q);
            for(int c = 0; c < str.length(); c++) {
                if(str.charAt(c) - '0' == k) answer += 1;
            }
        }
        return answer;
    }
}