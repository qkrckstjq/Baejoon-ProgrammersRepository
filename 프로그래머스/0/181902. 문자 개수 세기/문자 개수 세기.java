class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        
        for(int i = 0; i < my_string.length(); i++) {
            int index = my_string.charAt(i);
            if(97 <= index) {
                answer[index - 97 + 26] += 1;
            } else {
                answer[index - 65] += 1;
            }
        }
        
        return answer;
    }
}