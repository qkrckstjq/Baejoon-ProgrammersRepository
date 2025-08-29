class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        for(int i = 0; i < targets.length; i++) {
            for(int j = 0; j < targets[i].length(); j++) {
                char w = targets[i].charAt(j);
                int minC = Integer.MAX_VALUE;
                
                for(String key : keymap) {
                    for(int k = 0; k < key.length(); k++) {
                        if(k >= minC) {
                            break;
                        }
                        if(key.charAt(k) == w) {
                            minC = Math.min(minC, k + 1);
                        }
                    }
                }
                
                if(minC == Integer.MAX_VALUE) {
                    answer[i] = -1;
                    break;
                }
                
                answer[i] += minC;
                
            }   
        }
        return answer;
    }
}