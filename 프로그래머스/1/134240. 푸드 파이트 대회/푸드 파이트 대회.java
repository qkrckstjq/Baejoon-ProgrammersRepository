class Solution {
    public String solution(int[] food) {
        String answer = "";
        for(int i = 1; i < food.length; i++) {
            int max = (food[i] % 2 == 0) ? food[i]/2 : (food[i]-1)/2;
            for(int j = 0; j < max; j++) {
                answer+=Integer.toString(i);
            }
        }
        answer+='0';
        for(int i = answer.length()-2; i >= 0; i--) {
            answer+=answer.charAt(i);
        }
        return answer;
    }
}