class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long ans = 0L;
        long d = 0, p = 0;

        for (int i = n - 1; i >= 0; i--) {
            d += deliveries[i];
            p += pickups[i];

            while (d > 0 || p > 0) {
                d -= cap;
                p -= cap;
                ans += (long)(i + 1) * 2;
            }
        }
        return ans;
    }
}