class Solution {
    public int[] solution(int[] arr) {
        int start = -1;
        int end = -1;
        for(int i = 0; i < arr.length; i++) {
            if(start == -1 && arr[i] == 2) {
                start = i;
                end = i;
            } else if (arr[i] == 2){
                end = i;
            }
        }
        if(start == -1) {
            int[] result = {-1};
            return result;
        }
        int[] answer = new int[end - start + 1];
        int j = 0;
        for(int i = start; i <= end; i++) {
            answer[j++] = arr[i];
        }
        return answer;
    }
}