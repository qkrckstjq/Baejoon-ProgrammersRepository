import java.util.*;
class Solution {
    public String[] solution(String[][] tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        for(String[] info : tickets) {
            String src = info[0];
            String dst = info[1];
            graph.computeIfAbsent(src, a -> new ArrayList<>()).add(dst);
        }
        for(String key : graph.keySet()) {
            Collections.sort(graph.get(key));
        }
        
        Deque<String> queue = new ArrayDeque<>();
        List<String> answer = new ArrayList<>();
        queue.addLast("ICN");
        while(!queue.isEmpty()) {
            String curSrc = queue.removeFirst();
            
        }
        
        return null;
    }
}