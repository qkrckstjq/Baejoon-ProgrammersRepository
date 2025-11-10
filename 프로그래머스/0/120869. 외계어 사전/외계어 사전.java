import java.util.*;

class Solution {
    public int solution(String[] spell, String[] dic) {
        int[] base = new int[26];
        for (String s : spell) base[s.charAt(0) - 'a']++;  // spell은 한 글자 문자열들

        for (String w : dic) {
            if (w.length() != spell.length) continue;

            int[] cnt = Arrays.copyOf(base, 26);
            boolean ok = true;
            for (int i = 0; i < w.length(); i++) {
                int idx = w.charAt(i) - 'a';
                if (--cnt[idx] < 0) { ok = false; break; }
            }
            if (ok) return 1;
        }
        return 2;
    }
}
