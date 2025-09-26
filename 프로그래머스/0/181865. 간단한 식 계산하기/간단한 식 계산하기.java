class Solution {
    public int solution(String binomial) {
        String[] answer = binomial.trim().split(" ");
        int a = Integer.parseInt(answer[0]);
        String eval = answer[1];
        int b = Integer.parseInt(answer[2]);
        
        if(eval.equals("+")) {
            return a + b;
        } else if(eval.equals("-")) {
            return a - b;
        } else {
            return a * b;
        }
    }
}