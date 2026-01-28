import java.io.*;
import java.util.*;

class Main {
    static class Node {
        int v;   // 누적 비용
        int cur; // 현재 위치

        Node(int v, int cur) {
            this.v = v;
            this.cur = cur;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] nd = rd.readLine().split(" ");
        int n = Integer.parseInt(nd[0]);
        int end = Integer.parseInt(nd[1]);

        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();

        while (0 < n--) {
            String[] input = rd.readLine().split(" ");
            int src = Integer.parseInt(input[0]);
            int dst = Integer.parseInt(input[1]);
            int w = Integer.parseInt(input[2]);

            // [수정] 도착이 end 넘어가거나 역방향/의미없는 지름길은 걸러도 되고(필수는 아님), 특히 dst>end는 무조건 무시
            if (dst > end) continue;              // ★ 수정
            if (src > end) continue;              // ★ 수정
            if (dst <= src) continue;             // ★ 수정 (역방향/정지 이동 배제)

            Map<Integer, Integer> prev = graph.getOrDefault(src, new HashMap<>());
            int prevNum = prev.getOrDefault(dst, Integer.MAX_VALUE); // ★ 수정 (기본값)
            prev.put(dst, Math.min(prevNum, w));
            graph.put(src, prev);
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.v, b.v));

        // [수정] visit 대신 dist로 다익스트라 정석 처리
        int[] dist = new int[end + 1];                          // ★ 수정
        Arrays.fill(dist, Integer.MAX_VALUE);                   // ★ 수정
        dist[0] = 0;                                            // ★ 수정
        pq.add(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int node = curNode.cur;
            int cost = curNode.v;

            // [수정] 더 좋은 값이 이미 있으면 스킵
            if (cost != dist[node]) continue;                   // ★ 수정

            if (node == end) {
                System.out.println(cost);
                return;
            }

            // [수정] 일반 도로: node -> node+1 비용 1 (이게 핵심)
            if (node + 1 <= end && dist[node + 1] > cost + 1) {  // ★ 수정
                dist[node + 1] = cost + 1;                      // ★ 수정
                pq.add(new Node(dist[node + 1], node + 1));      // ★ 수정
            }

            Map<Integer, Integer> nextGraph = graph.getOrDefault(node, Collections.emptyMap());
            for (Map.Entry<Integer, Integer> e : nextGraph.entrySet()) { // ★ 수정(엔트리로 순회)
                int nextNode = e.getKey();
                int w = e.getValue();
                if (dist[nextNode] > cost + w) {                 // ★ 수정
                    dist[nextNode] = cost + w;                   // ★ 수정
                    pq.add(new Node(dist[nextNode], nextNode));  // ★ 수정
                }
            }
        }
    }
}
