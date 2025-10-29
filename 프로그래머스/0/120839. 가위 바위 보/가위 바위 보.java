class Solution {
    public String solution(String rsp) {
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < rsp.length(); i++) {
            char cur = rsp.charAt(i);
            answer.append(cur == '2' ? '0' : cur == '0' ? '5' : '2');
        }
        return answer.toString();
    }
}