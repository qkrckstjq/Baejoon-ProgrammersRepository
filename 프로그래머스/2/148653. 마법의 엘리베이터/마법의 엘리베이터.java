class Solution {
    public int answer = Integer.MAX_VALUE;
    public int solution(int storey) {
        back(storey, String.valueOf(storey).length() - 1, 0);
        return answer;
    }
    
    public void back(int storey, int digit, int num) {
        // System.out.println(storey);
        // System.out.println(digit);
        // System.out.println(num);
        // System.out.println();
        
        if(storey == 0) {
            answer = Math.min(num, answer);
            return;
        }
        
        if(num > answer || digit < 0 || storey < 0) {
            return;
        }
    
        StringBuilder temp = new StringBuilder(String.valueOf(storey));
        int curNum = temp.charAt(digit) - '0';
        int plus = (10 - curNum);
        int minus = curNum;
        
        int plusNum = storey + (int) (Math.pow(10, temp.length() - 1 - digit) * plus);
        int minusNum = storey - (int) (Math.pow(10, temp.length() - 1 - digit) * minus);

        back(plusNum, digit - (String.valueOf(plusNum).length() <= temp.length() ? 1 : 0), num + plus);
        back(minusNum, digit - 1, num + minus);
    }
}