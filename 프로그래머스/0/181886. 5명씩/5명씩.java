class Solution {
    public String[] solution(String[] names) {
        int len = names.length % 5 == 0 ? names.length / 5 : names.length / 5 + 1;
        String[] answer = new String[len];
        int j = 0;
        for(int i = 0; i < names.length; i++) {
            answer[j++] = names[i];
            i += 4;
        }
        return answer;
    }
}