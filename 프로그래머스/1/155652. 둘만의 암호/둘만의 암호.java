class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            for(int j = 0; j < index; j++) {
                c = (char) (c + 1);
                if(c > 'z') c = (char) ('a' - 1 + (c - 'z'));
                if(skip.contains(Character.toString(c))) j -= 1;
            }
            answer.append(Character.toString(c));
        }
        return answer.toString();
    }
}