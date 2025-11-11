class Solution {
    public int solution(String s) {
        int answer = 0;
        char x = s.charAt(0);
        int left = 0, right = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == x) left++;
            else right++;

            if (left == right) {
                answer++;
                left = 0; right = 0;
                if (i + 1 < s.length()) x = s.charAt(i + 1);
            }
        }

        if (left != right) answer++;
        return answer;
    }
}
