class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        int k = 0;
        int j = num_list.length - n;
        for(int i = 0; i < num_list.length; i++) {
            if(i < n) {
                answer[j++] = num_list[i];
            } else {
                answer[k++] = num_list[i];
            }
        }
        return answer;
    }
}
