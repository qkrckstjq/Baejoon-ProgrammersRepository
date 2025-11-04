class Solution {
    public int solution(int[] nums) {
        boolean[] primeArr = new boolean[1000001];
        
        for(int i = 2; i < (int) Math.sqrt(100001); i++) {
            if(!primeArr[i]) {
                for(int j = i + i; j < 100001; j += i) {
                    primeArr[j] = true;
                }
            }
        }
        
        primeArr[5] = false;
        primeArr[7] = false;
        
        // for(int i = 1; i < 100; i++) {
        //     System.out.printf("%d : %s\n", i, primeArr[i]);
        // }
        
        int answer = 0;
        for(int i = 0; i < nums.length; i++) {
            int numI = nums[i];
            for(int j = i + 1; j < nums.length; j++) {
                int numJ = nums[j];
                for(int k = j + 1; k < nums.length; k++) {
                    int numK = nums[k];
                    int temp = numI + numJ + numK;
                    if(!primeArr[temp]) {
                        // System.out.printf("%d %d %d\n", numI, numJ, numK);
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }
}