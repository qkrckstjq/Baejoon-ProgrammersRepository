class Solution {
    public long solution(int r1, int r2) {
        return countLE(r2) - countLT(r1); // r1 ≤ d ≤ r2
    }

    // 반지름 r 이하(≤)의 격자점 개수
    private static long countLE(long r) {
        long r2 = r * r, y = r, sum = 0;
        for (long x = 1; x <= r; x++) {
            long x2 = x * x;
            while (y > 0 && x2 + y * y > r2) y--;
            sum += y;
        }
        return 1 + 4 * sum + 4 * r;
    }

    // 반지름 r 미만(<)의 격자점 개수
    private static long countLT(long r) {
        if (r <= 0) return 0;
        long r2 = r * r, y = r - 1, sum = 0;
        for (long x = 1; x <= r - 1; x++) {
            long x2 = x * x;
            while (y > 0 && x2 + y * y >= r2) y--; // 경계 제외
            sum += y;
        }
        return 1 + 4 * sum + 4 * (r - 1);
    }
}