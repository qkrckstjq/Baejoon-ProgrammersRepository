import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        while(n-- > 0) {
            String[] input = rd.readLine().split(" ");
            Double num = Double.parseDouble(input[0]);
            String a = input[1];
            if(a.equals("kg")) {
                System.out.printf("%.4f %s\n", num * 2.2046, "lb");
            } else if(a.equals("lb")) {
                System.out.printf("%.4f %s\n", num * 0.4536, "kg");
            } else if(a.equals("l")) {
                System.out.printf("%.4f %s\n", num * 0.2642, "g");
            } else {
                System.out.printf("%.4f %s\n", num * 3.7854, "l");
            }
        }
    }
}