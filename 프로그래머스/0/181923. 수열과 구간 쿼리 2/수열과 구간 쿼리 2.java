class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for(int i = 0; i < queries.length; i++) {
            int min = Integer.MAX_VALUE;
            int[] se = queries[i];
            for(int j = se[0]; j <= se[1]; j++) {
                if(arr[j] > se[2]) {
                    min = Math.min(min, arr[j]);
                }
            }
            answer[i] = min == Integer.MAX_VALUE ? -1 : min;
        }
        return answer;
    }
}