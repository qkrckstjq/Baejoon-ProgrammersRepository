class Solution {

    public int solution(String word) {
        int[] weight = {781, 156, 31, 6, 1};
        char[] vowels = {'A', 'E', 'I', 'O', 'U'};

        int answer = 0;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            for (int j = 0; j < 5; j++) {
                if (c == vowels[j]) {
                    answer += j * weight[i] + 1;
                    break;
                }
            }
        }

        return answer;
    }
}