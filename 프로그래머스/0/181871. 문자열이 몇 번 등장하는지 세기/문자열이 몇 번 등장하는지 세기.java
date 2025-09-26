class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        for(int i = 0; i < myString.length(); i++) {
            if(myString.length() - i < pat.length()) {
                break;
            }
            answer += compare(myString, i, pat) ? 1 : 0;
        }
        return answer;
    }
    
    public boolean compare(String myString, int idx, String pat) {
        for(int i = idx; i < idx + pat.length(); i++) {
            if(myString.charAt(i) != pat.charAt(i - idx)) {
                return false;
            }
        }
        return true;
    }
}