class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        for(int i = 0; i < arr.length; i++) {
            answer[i] = arr[i];
        }
        
        for(int i = 0; i < queries.length; i++) {
            int[] se = queries[i];
            for(int j = se[0]; j <= se[1]; j++) {
                if(j % se[2] == 0) {
                    answer[j] += 1;
                }
            }
        }
        return answer;
    }
}