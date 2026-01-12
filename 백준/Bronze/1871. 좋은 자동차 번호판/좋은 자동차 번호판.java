import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        
        for(int i = 0; i < t; i++) {
            String[] input = rd.readLine().split("-");
            int a = toNum(input[0]);
            int b = Integer.parseInt(input[1]);
            System.out.println(Math.abs(a - b) <= 100 ? "nice" : "not nice");    
        }
    }
    
    public static int toNum(String str) {
        int answer = 0;
        int n = 2;
        for(int i = 0; i < str.length(); i++) {
            answer += Math.pow(26, n--) * (((int) str.charAt(i)) - 65);
        }
        return answer;
    }
}