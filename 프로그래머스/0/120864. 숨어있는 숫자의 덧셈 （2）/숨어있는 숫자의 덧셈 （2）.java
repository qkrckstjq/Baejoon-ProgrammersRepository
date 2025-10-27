class Solution {
    public int solution(String my_string) {
        int answer = 0;
        StringBuilder num = new StringBuilder("");
        for(int i = 0; i < my_string.length(); i++) {
            if(0 <= my_string.charAt(i) - '0' && my_string.charAt(i) - '0' <= 9) {
                num.append(my_string.charAt(i));
            } else if(num.length() > 0){
                answer += Integer.parseInt(num.toString());
                num = new StringBuilder("");
            }
        }
        if (num.length() > 0) answer += Integer.parseInt(num.toString());
        return answer;
    }
}