class Solution {

    public int solution(int[][] signals) {

        int n = signals.length;

        int[] cycle = new int[n];
        int[] yellowStart = new int[n];
        int[] yellowEnd = new int[n];

        int lcmValue = 1;

        for (int i = 0; i < n; i++) {

            int g = signals[i][0];
            int y = signals[i][1];
            int r = signals[i][2];

            cycle[i] = g + y + r;

            yellowStart[i] = g;
            yellowEnd[i] = g + y - 1;

            lcmValue = lcm(lcmValue, cycle[i]);
        }

        for (int t = 1; t <= lcmValue; t++) {

            boolean allYellow = true;

            for (int i = 0; i < n; i++) {

                int pos = (t - 1) % cycle[i];

                if (pos < yellowStart[i] || pos > yellowEnd[i]) {
                    allYellow = false;
                    break;
                }
            }

            if (allYellow) {
                return t;
            }
        }

        return -1;
    }

    private int gcd(int a, int b) {

        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }

    private int lcm(int a, int b) {
        return a / gcd(a, b) * b;
    }
}