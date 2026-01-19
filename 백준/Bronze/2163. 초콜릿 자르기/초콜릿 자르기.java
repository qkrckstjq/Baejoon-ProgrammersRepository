import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        System.out.println(n * m - 1);
    }
}