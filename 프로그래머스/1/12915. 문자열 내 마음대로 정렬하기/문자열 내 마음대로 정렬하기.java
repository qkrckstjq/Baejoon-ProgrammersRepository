import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                char c1 = s1.charAt(n);
                char c2 = s2.charAt(n);
                if (c1 == c2) {
                    return s1.compareTo(s2); // 인덱스 n의 문자가 같다면 사전순으로 정렬
                } else {
                    return c1 - c2; // 인덱스 n의 문자를 기준으로 오름차순 정렬
                }
            }
        });
        return strings;
    }
}