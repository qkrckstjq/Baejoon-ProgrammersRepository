class Solution {
    public String solution(String X, String Y) {
        int[] cntX = new int[10];
        int[] cntY = new int[10];

        for (int i = 0; i < X.length(); i++) {
            cntX[X.charAt(i) - '0']++;
        }
        for (int i = 0; i < Y.length(); i++) {
            cntY[Y.charAt(i) - '0']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            int c = Math.min(cntX[d], cntY[d]);  // 짝지을 수 있는 개수
            for (int i = 0; i < c; i++) {
                sb.append((char) ('0' + d));
            }
        }

        if (sb.length() == 0) return "-1";   // 공통 숫자 없음
        if (sb.charAt(0) == '0') return "0"; // 전부 0인 경우
        return sb.toString();
    }
}
