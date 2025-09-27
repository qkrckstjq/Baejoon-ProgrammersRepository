class Solution {
    public String solution(String rny_string) {
        String[] temp = rny_string.split("");
        for(int i = 0; i < temp.length; i++) {
            String str = temp[i];
            if(str.equals("m")) temp[i] = "rn";
        }
        return String.join("", temp);
    }
}