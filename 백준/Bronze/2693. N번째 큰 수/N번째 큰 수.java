import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        
        for(int i = 0; i < n; i++) {
            String[] input = rd.readLine().split(" ");
            int[] numList = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
            Arrays.sort(numList);
            System.out.println(numList[7]);
        }
    }
}