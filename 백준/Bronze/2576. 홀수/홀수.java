import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        
        String input;
        int answer = 0;
        int minOdd = 101;
        while((input = rd.readLine()) != null) {
            int inputNum = Integer.parseInt(input);
            if(inputNum % 2 != 0) {
                answer += inputNum;
                minOdd = Math.min(minOdd, inputNum);
            }
        }
        if(minOdd == 101) {
            System.out.println(-1);
        } else {
            System.out.printf("%d\n%d", answer, minOdd);
        }
    }
}