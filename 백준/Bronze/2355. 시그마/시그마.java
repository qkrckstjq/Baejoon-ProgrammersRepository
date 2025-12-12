import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        long i = Long.parseLong(input[0]);
        long j = Long.parseLong(input[1]);
        long a = Math.min(i, j);
        long b = Math.max(i, j);
        long answer = (b - a + 1) * (a + b) / 2;
        System.out.println(answer);
    }
}