import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        Set<String> visit = new HashSet<>();
        int N = Integer.parseInt(rd.readLine());
        String[] input = rd.readLine().split(" ");
        int answer = 0;
        for(String v : input) {
            if(visit.contains(v)) {
                answer+=1;
            } else {
                 visit.add(v);   
            }
        }
        System.out.println(answer);
    }
}