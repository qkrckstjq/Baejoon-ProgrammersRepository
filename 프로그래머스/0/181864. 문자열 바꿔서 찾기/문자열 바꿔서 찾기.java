class Solution {
    public int solution(String myString, String pat) {
        StringBuilder str = new StringBuilder(myString);
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(c == 'A') str.setCharAt(i, 'B');
            else if(c == 'B') str.setCharAt(i, 'A');
        }
        return str.toString().contains(pat) ? 1 : 0;
    }
}