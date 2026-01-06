import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception{
       BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
       String input = rd.readLine();
       int sumA = Arrays.stream(rd.readLine().split(" "))
           .mapToInt(Integer::parseInt)
           .reduce(0, (result, a) -> result + a);
       int sumB = Arrays.stream(rd.readLine().split(" "))
           .mapToInt(Integer::parseInt)
           .reduce(0, (result, a) -> result + a);
       System.out.println(sumA - sumB);
    }
}