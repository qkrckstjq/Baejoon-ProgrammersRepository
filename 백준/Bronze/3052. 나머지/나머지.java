import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < 10; i++) {
            Integer num = Integer.parseInt(rd.readLine());
            if(!set.contains(num % 42)) set.add(num % 42);
        }
        System.out.println(set.size());
    }
}