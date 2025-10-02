class Solution {
    public String solution(String myString) {
        StringBuilder answer = new StringBuilder(myString);
        for(int i = 0; i < answer.length(); i++) {
            if(answer.charAt(i) < 'l' - 0) answer.setCharAt(i, 'l');
        }
        return answer.toString();
    }
}