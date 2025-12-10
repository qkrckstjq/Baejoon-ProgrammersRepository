import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        for(int i = 0; i < n; i++) {
            String[] input = rd.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int m = getMinor(a, b);
            System.out.printf("%d %d\n", a * b / m, m);
        }
    }
    
    public static int getMinor(int a, int b) {
        int l = Math.max(a, b);
        int s = Math.min(a, b);
        while(s != 0) {
            int n = l % s;
            l = s;
            s = n;
        }
        return l;
    }
}