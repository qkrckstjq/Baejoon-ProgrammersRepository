class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 1;
        if(is_prefix.length() > my_string.length()) {
            return 0;
        }
        int j = 0;
        for(int i = 0; i < is_prefix.length(); i++) {
            if(my_string.charAt(j++) != is_prefix.charAt(i)) {
                answer = 0;
                break;
            }
        }
        return answer;
    }
}