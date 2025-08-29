import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        Set<String> dict = new HashSet<>(Arrays.asList("aya","ye","woo","ma"));

        for (String b : babbling) {
            String prev = "";
            StringBuilder target = new StringBuilder();
            boolean ok = true;

            for (int i = 0; i < b.length(); i++) {
                target.append(b.charAt(i));
                int L = target.length();

                if (L == 2 || L == 3) {
                    String sTarget = target.toString();
                    if (dict.contains(sTarget) && !sTarget.equals(prev)) {
                        prev = sTarget;
                        target.setLength(0); 
                    } else if (L == 3) {        
                        ok = false;
                        break;
                    }
                } else if (L > 3) {
                    ok = false;
                    break;
                }
            }

            if (ok && target.length() == 0) {
                answer++;
            }
        }
        return answer;
    }
}