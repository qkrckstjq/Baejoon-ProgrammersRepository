class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder answer = new StringBuilder(my_string);
        for(int[] se : queries) {
            int start = se[0];
            int end = se[1];
            int idx = end;
            for(int j = start; j < (start + end) / 2 + 1; j++) {
                char temp = answer.charAt(j);
                answer.setCharAt(j, answer.charAt(idx));
                answer.setCharAt(idx--, temp);
            } 
        }
        return answer.toString();
    }
}