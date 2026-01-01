import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int s = Integer.parseInt(rd.readLine());
        int[] hms = new int[]{Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2])};
        
        hms[2] += s;
        s = hms[2] / 60;
        hms[2] %= 60;
        
        hms[1] += s;
        s = hms[1] / 60;
        hms[1] %= 60;
        
        hms[0] += s;
        hms[0] %= 24;
        
        System.out.printf("%d %d %d", hms[0], hms[1], hms[2]);
    }
}