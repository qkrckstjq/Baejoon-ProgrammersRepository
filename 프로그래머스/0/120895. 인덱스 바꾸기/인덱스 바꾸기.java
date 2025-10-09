class Solution {
    public String solution(String my_string, int num1, int num2) {
        StringBuilder answer = new StringBuilder(my_string);
        char c1 = answer.charAt(num1);
        char c2 = answer.charAt(num2);
        answer.setCharAt(num1, c2);
        answer.setCharAt(num2, c1);
        return answer.toString();
    }
}