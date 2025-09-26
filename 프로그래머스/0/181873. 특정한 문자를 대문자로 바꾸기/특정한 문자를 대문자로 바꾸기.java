class Solution {
    public String solution(String my_string, String alp) {
        StringBuilder answer = new StringBuilder(my_string);
        for(int i = 0; i < my_string.length(); i++) {
            String cur = String.valueOf(my_string.charAt(i));
            if(cur.equals(alp)) {
                answer.setCharAt(i, cur.toUpperCase().charAt(0));
            }
        }
        return answer.toString();
    }
}