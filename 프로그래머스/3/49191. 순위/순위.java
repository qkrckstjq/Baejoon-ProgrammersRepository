import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        Map<Integer, List<Integer>> graphA = new HashMap<>();
        Map<Integer, List<Integer>> graphB = new HashMap<>();
        for(int[] ab : results) {
            int a = ab[0];
            int b = ab[1];
            List<Integer> aL = graphA.getOrDefault(a, new ArrayList<>());
            List<Integer> bL = graphB.getOrDefault(b, new ArrayList<>());
            aL.add(b);
            bL.add(a);
            graphA.put(a, aL);
            graphB.put(b, bL);
        }
        
        for(int i = 1; i <= n; i++) {
            int a = dfs(graphA, i);
            int b = dfs(graphB, i);
            // System.out.println(i);   
            // System.out.println(a);
            // System.out.println(b);
            // System.out.println('\n');
            if(a + b  == n - 1) {
                answer += 1;
            }
        }
        return answer;
    }
    
    private int dfs(Map<Integer, List<Integer>> graph, int start) {
        int result = -1;
        Set<Integer> visit = new HashSet<>();
        List<Integer> stack = new ArrayList<>();
        stack.add(start);
        while(!stack.isEmpty()) {
            Integer curNode = stack.remove(stack.size() - 1);
            if(visit.contains(curNode)) {
                continue;
            }
            visit.add(curNode);
            result += 1;
            for(Integer nextNode : graph.getOrDefault(curNode, new ArrayList<>())) {
                if(!visit.contains(nextNode)) {
                    stack.add(nextNode);
                }
            }
        }
        return result;
    }
}