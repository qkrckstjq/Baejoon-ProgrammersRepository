class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer = new StringBuilder("");
        for(int i = (my_string.length() - n); i < my_string.length(); i++) {
            answer.append(my_string.charAt(i));
        }
        return answer.toString();
    }
}