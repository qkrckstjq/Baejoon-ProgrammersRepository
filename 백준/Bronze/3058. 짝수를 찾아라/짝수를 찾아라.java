import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < t; i++) {
            int minEven = Integer.MAX_VALUE;
            int result = 0;
            String[] input = rd.readLine().split(" ");
            for(int j = 0; j < 7; j++) {
                int num = Integer.parseInt(input[j]);
                if(num % 2 == 0) {
                    result += num;
                    minEven = Math.min(minEven, num);
                }
            }
            answer.append(result + " " + minEven).append("\n");
        }
        System.out.println(answer.toString());
    }
}