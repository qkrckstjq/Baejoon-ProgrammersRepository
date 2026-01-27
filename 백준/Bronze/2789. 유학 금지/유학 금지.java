import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        boolean[] banned = new boolean[26];
        String ban = "CAMBRIDGE";
        for (int i = 0; i < ban.length(); i++) {
            banned[ban.charAt(i) - 'A'] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!banned[c - 'A']) sb.append(c);
        }

        System.out.print(sb.toString());
    }
}
