import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] list;
        int a;
        int b;
        while (true) {
            list = rd.readLine().split(" ");
            a = Integer.parseInt(list[0]);
            b = Integer.parseInt(list[1]);
            if(a == 0 && b == 0) return;
            System.out.println(a > b ? "Yes" : "No");
        }
    }
        
}