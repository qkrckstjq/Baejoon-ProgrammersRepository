import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        
        if(a + b == c) {
            System.out.printf("%d+%d=%d", a, b, c);
        } else if(b + c == a) {
            System.out.printf("%d=%d+%d", a, b, c);
        } else if(a - b == c) {
            System.out.printf("%d-%d=%d", a, b, c);
        } else if(a == b - c) {
            System.out.printf("%d=%d-%d", a, b, c);
        } else if(a * b == c) {
            System.out.printf("%d*%d=%d", a, b, c);
        } else if(a == b * c) {
            System.out.printf("%d=%d*%d", a, b, c);
        } else if(a / b == c) {
            System.out.printf("%d/%d=%d", a, b, c);
        } else {
            System.out.printf("%d=%d/%d", a, b, c);
        }
    }
}