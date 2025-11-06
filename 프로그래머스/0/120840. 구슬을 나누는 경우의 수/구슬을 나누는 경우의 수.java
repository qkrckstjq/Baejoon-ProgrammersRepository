class Solution {
    public int solution(int balls, int share) {
        if (share < 0 || share > balls) return 0;
        int k = Math.min(share, balls - share);
        long res = 1;
        for (int i = 1; i <= k; i++) {
            res = res * (balls - k + i) / i;
        }
        return (int) res;
    }
}
