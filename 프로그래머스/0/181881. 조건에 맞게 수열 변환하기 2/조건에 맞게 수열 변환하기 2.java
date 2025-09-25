class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        boolean change = false;
        while(!change) {
            change = true;
            for(int i = 0; i < arr.length; i++) {
                int num = arr[i];
                if(num >= 50 && num % 2 == 0) {
                    arr[i] = num / 2;
                    change = false;
                } else if(num < 50 && num % 2 != 0) {
                    arr[i] = num * 2 + 1;
                    change = false;
                } else {
                    arr[i] = num;
                }
            }
            if(!change) {
                answer += 1;
            }
        }
        return answer;
    }
}