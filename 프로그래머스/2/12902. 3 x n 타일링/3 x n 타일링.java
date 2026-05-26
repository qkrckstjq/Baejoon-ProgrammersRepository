class Solution {
    public int solution(int n) {
        long MOD = 1000000007L;

if (n % 2 == 1) return 0;

long[] dp = new long[n + 1];

dp[0] = 1;
dp[2] = 3;

for (int i = 4; i <= n; i += 2) {
    dp[i] = (4L * dp[i - 2] - dp[i - 4] + MOD) % MOD;
}

return (int) dp[n];
    }
}

// 1 2 3 4
// 0 3 0 11