class Solution {
    public int solution(int num, int k) {
        return Integer.toString(num).indexOf(Integer.toString(k)) < 0 ? -1 : Integer.toString(num).indexOf(Integer.toString(k)) + 1;
    }
}