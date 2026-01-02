import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int avg = 0;
        Map<Integer, Integer> arr = new HashMap<>();
        
        for(int i = 0; i < 10; i++) {
            int input = Integer.parseInt(rd.readLine());
            avg += input;
            arr.put(input, arr.getOrDefault(input, 0) + 1);
        }
        
        int maxKey = arr.keySet().stream().reduce((best, k) -> arr.get(k) > arr.get(best) ? k : best).orElseThrow();;
        
        System.out.printf("%d\n%d", avg / 10, maxKey);
    }
}