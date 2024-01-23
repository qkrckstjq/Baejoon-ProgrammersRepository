import java.util.Stack;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        
        while(!stack.isEmpty()) {
            int cur = stack.pop();
            visited[cur] = 1;
            for(int i = 0; i < n; i++) {
                if(computers[cur][i] == 1 && visited[i] == 0) {
                    stack.push(i);
                }
            }
            if(stack.isEmpty()) {
                answer++;
                for(int i = 0; i < n; i++) {
                    if(visited[i] == 0) {
                        stack.push(i);
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}