import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        for(int i = 0; i < t; i++) {
            String[] input = rd.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            System.out.println(input[1].substring(0, n - 1) + input[1].substring(n, input[1].length()));
        }
    }
}