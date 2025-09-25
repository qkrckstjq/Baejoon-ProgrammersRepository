class Solution {
    public String solution(String myString) {
        StringBuilder answer = new StringBuilder(myString);
        for(int i = 0; i < answer.length(); i++) {
            char c = answer.charAt(i);
            if(c == 'a') {
                c -= 32;
            } else if (65 <= c && c <= 90 && c != 'A'){
                c += 32;
            }
            answer.setCharAt(i, c);
        }
        return answer.toString();
    }
}