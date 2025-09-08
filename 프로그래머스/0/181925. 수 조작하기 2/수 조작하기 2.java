class Solution {
    public String solution(int[] numLog) {
        StringBuilder answer = new StringBuilder("");
        int prev = numLog[0];
        for(int i = 1; i < numLog.length; i++) {
            int move = prev - numLog[i];
            if(move == -1) {
                answer.append("w");
            } else if(move == 1) {
                answer.append("s");
            } else if(move == -10) {
                answer.append("d");
            } else if(move == 10) {
                answer.append("a");
            }
            prev = numLog[i];
        }
        return answer.toString();
    }
}