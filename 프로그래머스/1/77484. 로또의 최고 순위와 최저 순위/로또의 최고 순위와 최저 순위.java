
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int best = 0;
        int worst = 0;
        int empty = 0;
        
        for(int lotto : lottos) {
            if(lotto == 0) {
                empty++;
            }
            for(int winNumber : win_nums) {
                if(lotto == winNumber) {
                    best++;
                    worst++;
                }
            }
        }
        best+=empty;
        answer[0] = caseSelector(best);
        answer[1] = caseSelector(worst);
        return answer;        
    }
    public int caseSelector (int number) {
        if(number < 2) {
            return 6;
        }
        if(number == 2) {
            return 5;
        } else if (number == 3) {
            return 4;
        } else if (number == 4) {
            return 3;
        } else if (number == 5) {
            return 2;
        } else {
            return 1;
        }
    }
}