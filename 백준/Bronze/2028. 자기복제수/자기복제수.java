import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(rd.readLine());
        for(int i = 0; i < T; i++) {
            StringBuilder target = new StringBuilder(rd.readLine());
            StringBuilder p = new StringBuilder(Integer.toString((int) Math.pow(Integer.parseInt(target.toString()), 2)));
            String rTarget = target.reverse().toString();
            String rSq = p.reverse().toString();
            
            // System.out.println();
            // System.out.println(rTarget);
            // System.out.println(p.toString());
            // System.out.println();
            
            if(rSq.startsWith(rTarget)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}