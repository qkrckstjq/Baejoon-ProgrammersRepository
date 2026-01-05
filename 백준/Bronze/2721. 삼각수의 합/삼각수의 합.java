import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        for(int i = 0; i < n; i++) {
            long input = Long.parseLong(rd.readLine());
            System.out.println(input * (input + 1) * (input + 2) * (input + 3) / 8);
        }
    }
}