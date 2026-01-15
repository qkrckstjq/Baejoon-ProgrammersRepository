import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        int answer = 0;
        int temp = 1;
        String[] inputList = rd.readLine().split(" ");
        for(String input : inputList) {
            if(input.equals("1")) {
                answer += temp;
                temp += 1;
            } else {
                temp = 1;
            }
        }
        System.out.println(answer);
    }
}