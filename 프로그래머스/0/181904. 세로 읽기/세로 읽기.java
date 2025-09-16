class Solution {
    public String solution(String my_string, int m, int c) {
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < my_string.length(); i++) {
            for(int j = 0; j < m; j++) {
                if(j + 1 == c) {
                    answer.append(my_string.charAt(i + j));
                }
            }
            i += m - 1;
        }
        return answer.toString();
    }
}