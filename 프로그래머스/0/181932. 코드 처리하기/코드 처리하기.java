class Solution {
    public String solution(String code) {
        StringBuilder answer = new StringBuilder("");
        char mode = '0';
        for(int i = 0; i < code.length(); i++) {
            char curCode = code.charAt(i);
            
            if(mode == '0' && curCode == '1') {
                mode = '1';
            } else if(mode == '1' && curCode == '1') {
                mode = '0';
            } else {
                if((mode == '0' && i % 2 == 0) || (mode == '1' && i % 2 != 0)) {
                    answer.append(curCode); 
                } 
            }
            // System.out.printf("mode : %c, i : %d, curCode : %c\n", mode, i, curCode);
        }
        return answer.length() == 0 ? "EMPTY" : answer.toString();
    }
}