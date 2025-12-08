import java.io.*;
import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new HashMap<>();
        String line;
        while((line = rd.readLine()) != null) {
            for(int i = 0; i < line.length(); i++) {
                char target = line.charAt(i);
                String alp = Character.toString(target);
                if(97 <= target && target <= 122) {
                    map.put(alp, map.getOrDefault(alp, 0) + 1);
                }
            }
        }
        List<String> list = map.keySet().stream()
            .sorted(Comparator.comparing((String s) -> map.get(s) * -1).thenComparing(s -> s))
            .collect(Collectors.toList());
        StringBuilder answer = new StringBuilder("");
        int t = -1;
        for(int i = 0; i < list.size(); i++) {
            if(t < 0) t = map.get(list.get(i));
            if(t > map.get(list.get(i))) break;
            answer.append(list.get(i));
        }
        System.out.println(answer.toString());
    }
}