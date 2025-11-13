class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for(int i = 0; i < quiz.length; i++) {
            String[] math = quiz[i].split(" ");
            int num1 = Integer.parseInt(math[0]);
            int num2 = Integer.parseInt(math[2]);
            int result = Integer.parseInt(math[4]);
            // System.out.printf("%s\n", math[1]);
            answer[i] = (math[1].equals("-") ? num1 - num2 : num1 + num2) == result ? "O" : "X";
        }
        return answer;
    }
}