class Solution {
    public String solution(String str1, String str2) {
        StringBuilder answer = new StringBuilder("");
        int i = 0;
        int j = 0;
        while(i < str1.length() || j < str2.length()) {
            if(i < str1.length()) {
                answer.append(str1.charAt(i));
            }
            
            if(j < str2.length()) {
                answer.append(str2.charAt(j));
            }
            i++;
            j++;
        }
        return answer.toString();
    }
}