import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(rd.readLine());
        while(0 < T--) {
            String temp = rd.readLine();
            String[] sb = rd.readLine().split(" ");
            List<Integer> s = Arrays.stream(rd.readLine().split(" "))
                .map(Integer::parseInt)
                .sorted()
                .collect(Collectors.toList());
            List<Integer> b = Arrays.stream(rd.readLine().split(" "))
                .map(Integer::parseInt)
                .sorted()
                .collect(Collectors.toList());
            
            while(!s.isEmpty() && !b.isEmpty()) {
                int lastS = s.get(s.size() - 1);
                int lastB = b.get(b.size() - 1);
                
                if(lastS >= lastB) {
                    b.remove(b.size() - 1);
                } else {
                    s.remove(s.size() - 1);
                }
            }
            if(s.isEmpty()) {
                System.out.println("B");
            } else {
                System.out.println("S");
            }
        }
    }
}