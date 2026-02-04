import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        Integer[] input = Arrays.stream(rd.readLine().split(" "))
            .map(Integer::parseInt)
            .sorted(Comparator.comparing(i -> i))
            .toArray(Integer[]::new);
        System.out.println(input[0] * input[2]);
    }
}