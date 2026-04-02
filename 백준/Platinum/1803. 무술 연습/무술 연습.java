import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ');

            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }

            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int m = fs.nextInt();
        int n = fs.nextInt();
        int N = m + n;

        int[] out = new int[N];
        int[] indeg = new int[N];

        for (int i = 0; i < m; i++) {
            int b = fs.nextInt() - 1;
            out[i] = m + b;
            indeg[m + b]++;
        }

        for (int i = 0; i < n; i++) {
            int a = fs.nextInt() - 1;
            out[m + i] = a;
            indeg[a]++;
        }

        int[] remainIndeg = indeg.clone();
        int[] bowIn = new int[N];
        int[] state = new int[N];
        Arrays.fill(state, -1);

        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            if (remainIndeg[i] == 0) q.add(i);
        }

        while (!q.isEmpty()) {
            int v = q.poll();
            state[v] = bowIn[v] > 0 ? 0 : 1;

            int to = out[v];
            if (state[v] == 1) bowIn[to]++;
            remainIndeg[to]--;

            if (remainIndeg[to] == 0) q.add(to);
        }

        boolean[] visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            if (remainIndeg[i] > 0 && !visited[i]) {
                int cur = i;
                int len = 0;
                while (!visited[cur]) {
                    visited[cur] = true;
                    len++;
                    cur = out[cur];
                }

                int[] cycle = new int[len];
                cur = i;
                for (int k = 0; k < len; k++) {
                    cycle[k] = cur;
                    cur = out[cur];
                }

                int startForced = -1;
                for (int k = 0; k < len; k++) {
                    if (bowIn[cycle[k]] > 0) {
                        startForced = k;
                        break;
                    }
                }

                if (startForced == -1) {
                    state[cycle[0]] = 1;
                    for (int k = 1; k < len; k++) {
                        state[cycle[k]] = 1 - state[cycle[k - 1]];
                    }
                } else {
                    state[cycle[startForced]] = 0;
                    for (int step = 1; step < len; step++) {
                        int prev = cycle[(startForced + step - 1) % len];
                        int v = cycle[(startForced + step) % len];
                        if (bowIn[v] > 0) {
                            state[v] = 0;
                        } else {
                            state[v] = 1 - state[prev];
                        }
                    }
                }
            }
        }

        StringBuilder sbA = new StringBuilder();
        StringBuilder sbB = new StringBuilder();

        for (int i = 0; i < m; i++) sbA.append(state[i]);
        for (int i = 0; i < n; i++) sbB.append(state[m + i]);

        StringBuilder ans = new StringBuilder();
        ans.append(sbA).append('\n').append(sbB).append('\n');
        System.out.print(ans);
    }
}