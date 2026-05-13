import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> l1 = new HashMap<>();
        Map<String, List<Integer>> l2 = new HashMap<>();
        for(int i = 0; i < genres.length; i++) {
            String g = genres[i];
            int p = plays[i];
            List<Integer> ex = l2.getOrDefault(g, new ArrayList<>());
            ex.add(i);
            
            l1.put(g, l1.getOrDefault(g, 0) + p);
            l2.put(g, ex);
        }
        l2.keySet().stream()
            .forEach(k -> l2.get(k).sort(Comparator.comparing((Integer i) -> plays[i]).reversed()));
        

        List<String> list = l1.keySet().stream()
            .sorted(Comparator.comparing(s -> l1.get(s)).reversed())
            .collect(Collectors.toList());
        
        
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < list.size(); i++) {
            String g = list.get(i);
            List<Integer> nums = l2.get(g);
            for(int j = 0; j < Math.min(2, nums.size()); j++) {
                answer.add(nums.get(j));
            }
        }
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}