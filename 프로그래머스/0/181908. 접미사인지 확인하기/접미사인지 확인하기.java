class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 1;
        int j = 0;
        if(is_suffix.length() > my_string.length()) {
            return 0;
        }
        for(int i = (my_string.length() - is_suffix.length()); i < my_string.length(); i++) {
            if(my_string.charAt(i) != is_suffix.charAt(j++)) {
                answer = 0;
                break;
            }
        }
        return answer;
    }
}