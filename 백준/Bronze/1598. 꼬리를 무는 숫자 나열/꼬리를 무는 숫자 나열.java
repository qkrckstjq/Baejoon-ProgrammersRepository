import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int a = Integer.parseInt(input[0]) - 1;
        int b = Integer.parseInt(input[1]) - 1;
        
        int y1 = a / 4;
        int x1 = a % 4;
        
        int y2 = b / 4;
        int x2 = b % 4;
        
        System.out.println(Math.abs(y1 - y2) + Math.abs(x1 - x2));
    }
}