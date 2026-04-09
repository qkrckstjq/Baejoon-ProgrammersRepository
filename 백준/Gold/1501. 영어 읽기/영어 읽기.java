import java.io.*;
import java.util.*;

public class Main {

    static String normalize(String s) {
        if (s.length() <= 2) return s;

        char[] mid = s.substring(1, s.length() - 1).toCharArray();
        Arrays.sort(mid);

        return "" + s.charAt(0) + new String(mid) + s.charAt(s.length() - 1);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            String key = normalize(word);
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        int M = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (M-- > 0) {
            String[] sentence = br.readLine().split(" ");
            long result = 1;

            for (String word : sentence) {
                String key = normalize(word);
                result *= map.getOrDefault(key, 0);
            }

            sb.append(result).append("\n");
        }

        System.out.print(sb);
    }
}