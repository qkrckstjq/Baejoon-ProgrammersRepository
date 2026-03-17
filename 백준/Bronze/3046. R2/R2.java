import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int r1 = Integer.parseInt(input[0]);
        int s = Integer.parseInt(input[1]);
        System.out.println(s * 2 - r1);
    }
}