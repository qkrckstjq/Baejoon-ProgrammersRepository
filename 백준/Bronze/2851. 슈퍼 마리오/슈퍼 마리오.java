import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        String input;
        while((input = rd.readLine()) != null) {
            int num = Integer.parseInt(input);
            int next = answer + num;
            if(Math.abs(100 - next) > Math.abs(100 - answer)) {
                System.out.println(answer);
                return;
            } else if(Math.abs(100 - next) == Math.abs(100 - answer)) {
                System.out.println(Math.max(next, answer));
                return;
            }
            answer = next;
        }
        System.out.println(answer);
    }
}