class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int i = 0, j = 0, k = 0;
        
        while(true) {
            if(k == goal.length) {
                return "Yes";
            }
            
            
            if(i < cards1.length && goal[k].equals(cards1[i])) {
                i++;
                k++;
            } else if (j < cards2.length && goal[k].equals(cards2[j])) {
                j++;
                k++;
            } else {
                return "No";
            }
        }
    }
}