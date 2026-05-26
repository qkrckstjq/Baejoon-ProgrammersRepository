class Solution {
    public int solution(int n) {
        if(n <= 3) {
            return n;
        }
        int[] arr = new int[n + 1];
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 3;
        int answer = 0;
        for(int i = 4; i <= n; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1000000007;
        }
        
        return arr[n];
    }
}

// 1 2 3 4
// 1 2 3 5 