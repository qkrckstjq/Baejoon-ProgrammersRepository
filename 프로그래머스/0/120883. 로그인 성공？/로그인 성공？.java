class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for(String[] ip : db) {
            if(ip[0].equals(id_pw[0])) {
                if(ip[1].equals(id_pw[1])) return "login";
                return "wrong pw";
            }
        }
        return "fail";
    }
}