class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int len = common.length - 1;
        int last = common[len];
        int second = common[len - 1];
        int third = common[len - 2];
        
        int f_dif = last - second;
        int s_dif = second - third;
        
        if(f_dif == s_dif) {
            return last + f_dif;
        } else {
            return last * (last / second); 
        }
        
        // return answer;
    }
}