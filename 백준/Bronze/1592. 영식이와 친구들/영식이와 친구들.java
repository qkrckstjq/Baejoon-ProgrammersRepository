import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int L = Integer.parseInt(input[2]);
        
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 1; i <= N; i++) {
            map.put(i, 0);
        }
        int curNode = 1;
        int answer = 0;
        while(true) {
            int curNM = map.get(curNode);
            curNM += 1;
            if(curNM >= M) break;
            answer += 1;
            map.put(curNode, curNM);

            int nextNode = curNode;
            if(curNM % 2 != 0) {
                nextNode += L;
                curNode = nextNode > N ? nextNode - N : nextNode;
            } else {
                nextNode -= L;
                curNode = nextNode < 1 ? nextNode + N : nextNode;
            }
        }
        System.out.println(answer);
    }
} 