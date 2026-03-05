import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 3; i++) {
            String[] list = rd.readLine().split(" ");
            int sum = 0;
            for(String num : list) {
                sum += Integer.parseInt(num);
            }
            String answer = "";
            if(sum == 3) {
                answer = "A";
            } else if(sum == 2) {
                answer = "B";
            } else if(sum == 1) {
                answer = "C";
            } else if(sum == 0) {
                answer = "D";
            } else if(sum == 4) {
                answer = "E";
            }
            System.out.println(answer);
        }
    }
} 