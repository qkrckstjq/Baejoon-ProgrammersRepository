class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int[] list = new int[n + 1];
        
        for(int i : section) {
            list[i] = 1;
        }
        
        for(int i = 1; i < list.length; i++) {
            if(list[i] == 1) {
                answer += 1;
                for(int j = i; j < (i + m < list.length ? i + m : list.length); j++) {
                    list[j] = 0;
                }
            }
        }
        
        return answer;
    }
}