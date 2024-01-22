
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int same = 0;
        int empty = 0;
        
        for(int lotto : lottos) {
            if(lotto == 0) {
                empty++;
            }
            for(int winNumber : win_nums) {
                if(lotto == winNumber) {
                    same++;
                }
            }
        }
        answer[0] = same+empty == 0 ? 6 : 7 - (same+empty);
        answer[1] = same == 0 ? 6 : 7 - same;
        return answer;        
    }
}