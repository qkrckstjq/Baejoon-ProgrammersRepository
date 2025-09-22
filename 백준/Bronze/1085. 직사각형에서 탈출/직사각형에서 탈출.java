import java.util.*;
import java.io.*;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int yx = Math.min(input[0], input[1]);
        int yx2 = Math.min(input[2] - input[0], input[3] - input[1]);
        int answer = Math.min(yx, yx2);
        writer.write(Integer.toString(answer));
        writer.flush();
    }
}