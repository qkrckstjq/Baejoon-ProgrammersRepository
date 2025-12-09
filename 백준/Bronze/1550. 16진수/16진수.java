import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();
        int answer = 0;
        
        for(int i = 0; i < input.length(); i++) {
            char target = input.charAt(i);
            int num = ((int)'A' <= (int)target && (int)target <= (int)'F') ? (int) target - 55 : target - '0';
            answer += (Math.pow(16, input.length() - 1 - i)) * (num);
        }
        System.out.println(answer);
    }
}