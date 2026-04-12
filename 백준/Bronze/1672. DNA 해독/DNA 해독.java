import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        Map<Character, Map<Character, Character>> protocol = new HashMap<>();
        protocol.put('A', Map.of('A', 'A', 'G', 'C', 'C', 'A', 'T', 'G'));
        protocol.put('G', Map.of('A', 'C', 'G', 'G', 'C', 'T', 'T', 'A'));
        protocol.put('C', Map.of('A', 'A', 'G', 'T', 'C', 'C', 'T', 'G'));
        protocol.put('T', Map.of('A', 'G', 'G', 'A', 'C', 'G', 'T', 'T'));
        
        
        int n = Integer.parseInt(rd.readLine());
        String input = rd.readLine();
        
        char i = input.charAt(n - 1);
        for(int j = n - 2; j >= 0; j--) {
            i = protocol.get(input.charAt(j)).get(i);
        }
        System.out.println(i);
    }
}