class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < parts.length; i++) {
            String my_str = my_strings[i];
            for(int j = parts[i][0]; j <= parts[i][1]; j++) {
                answer.append(my_str.charAt(j));
            }
        }
        return answer.toString();
    }
}