class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for(int i = 0; i < queries.length; i++) {
            int[] se = queries[i];
            for(int j = se[0]; j <= se[1]; j++) {
                arr[j] += 1;
            }
        }
        return arr;
    }
}