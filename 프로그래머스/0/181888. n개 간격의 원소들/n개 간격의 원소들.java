class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length % n == 0 ? num_list.length / n : (num_list.length / n) + 1;
        int[] answer = new int[len];
        int idx = 0;
        for(int i = 0; i < num_list.length; i++) {
            answer[idx++] = num_list[i];
            i += (n - 1);
        }
        return answer;
    }
}