class Solution {
    public int solution(String number) {
        int rem = 0;
        for (int i = 0; i < number.length(); i++) {
            rem = (rem + (number.charAt(i) - '0')) % 9;
        }
        return rem; // 0..8 (예: "0"이면 0)
    }
}