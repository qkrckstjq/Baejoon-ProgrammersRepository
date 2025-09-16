class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuilder answer = new StringBuilder(my_string);
        int j = e;
        for(int i = s; i <= (e + s) / 2; i++) {
            char temp = answer.charAt(i);
            answer.setCharAt(i, answer.charAt(j));
            answer.setCharAt(j--, temp);
        }
        return answer.toString();
    }
}