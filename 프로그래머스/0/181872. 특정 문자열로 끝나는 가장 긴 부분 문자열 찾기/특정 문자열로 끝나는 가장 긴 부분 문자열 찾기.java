class Solution {
    public String solution(String myString, String pat) {
        StringBuilder answer = new StringBuilder("");
        boolean find = false;
        int idx = 0;
        for(int i = myString.length() - 1; i >= 0; i--) {
            if(pat.length() > i + 1) break;
            if(compare(myString, i, pat)) {
                idx = i + 1;
                find = true;
                break;
            }
        }
        for(int i = 0; i < idx; i++) {
            answer.append(myString.charAt(i));
        }         
        return answer.toString();
    }
    
    public boolean compare(String myString, int end, String pat) {
        int start = end - pat.length() + 1;
        if (start < 0) return false;                
        for (int k = 0; k < pat.length(); k++) {
            if (pat.charAt(k) != myString.charAt(start + k)) return false;
        }
        return true;
    }
}