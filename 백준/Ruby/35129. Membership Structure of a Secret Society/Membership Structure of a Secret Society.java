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

        String next() throws IOException {
            int c;
            do {
                c = read();
                if (c == -1) return null;
            } while (c <= ' ');
            StringBuilder sb = new StringBuilder();
            while (c > ' ') {
                sb.append((char) c);
                c = read();
            }
            return sb.toString();
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
                if (c == -1) return Integer.MIN_VALUE;
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

    static class DSU {
        int[] p, sz;
        DSU(int n) {
            p = new int[n + 1];
            sz = new int[n + 1];
            for (int i = 0; i <= n; i++) {
                p[i] = i;
                sz[i] = 1;
            }
        }
        int find(int x) {
            while (p[x] != x) {
                p[x] = p[p[x]];
                x = p[x];
            }
            return x;
        }
        void union(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) { int t = a; a = b; b = t; }
            p[b] = a;
            sz[a] += sz[b];
        }
    }

    static boolean addAll(BitSet target, BitSet source) {
        BitSet diff = (BitSet) source.clone();
        diff.andNot(target);
        if (diff.isEmpty()) return false;
        target.or(diff);
        return true;
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        String ts = fs.next();
        if (ts == null) return;
        int t = Integer.parseInt(ts);
        StringBuilder out = new StringBuilder();

        for (int tc = 0; tc < t; tc++) {
            int n = fs.nextInt();
            int maxId = 3 * n;

            boolean[] active = new boolean[maxId + 1];

            int[] recA = new int[n];
            int[] recB = new int[n];
            int recCnt = 0;

            int[] nrecA = new int[n];
            int[] nrecB = new int[n];
            int nrecCnt = 0;

            int[] lhs = new int[n];
            int[] op1 = new int[n];
            int[] op2 = new int[n];
            int interCnt = 0;

            int[] leftCnt = new int[maxId + 1];
            int[] rightCnt = new int[maxId + 1];

            for (int i = 0; i < n; i++) {
                String type = fs.next();
                if (type.equals("recommend")) {
                    int a = fs.nextInt();
                    int b = fs.nextInt();
                    recA[recCnt] = a;
                    recB[recCnt] = b;
                    recCnt++;
                    active[a] = true;
                    active[b] = true;
                } else if (type.equals("not-recommend")) {
                    int a = fs.nextInt();
                    int b = fs.nextInt();
                    nrecA[nrecCnt] = a;
                    nrecB[nrecCnt] = b;
                    nrecCnt++;
                    active[a] = true;
                    active[b] = true;
                } else {
                    int a = fs.nextInt();
                    int b = fs.nextInt();
                    int c = fs.nextInt();
                    lhs[interCnt] = a;
                    op1[interCnt] = b;
                    op2[interCnt] = c;
                    interCnt++;

                    active[a] = true;
                    active[b] = true;
                    active[c] = true;
                    leftCnt[a]++;
                    rightCnt[b]++;
                    rightCnt[c]++;
                }
            }

            int[] activeList = new int[maxId];
            int activeN = 0;
            for (int i = 1; i <= maxId; i++) {
                if (active[i]) activeList[activeN++] = i;
            }

            int[][] leftAdj = new int[maxId + 1][];
            int[][] rightAdj = new int[maxId + 1][];
            int[] leftPos = new int[maxId + 1];
            int[] rightPos = new int[maxId + 1];
            for (int i = 1; i <= maxId; i++) {
                if (leftCnt[i] > 0) leftAdj[i] = new int[leftCnt[i]];
                if (rightCnt[i] > 0) rightAdj[i] = new int[rightCnt[i]];
            }
            for (int idx = 0; idx < interCnt; idx++) {
                int a = lhs[idx], b = op1[idx], c = op2[idx];
                leftAdj[a][leftPos[a]++] = idx;
                rightAdj[b][rightPos[b]++] = idx;
                rightAdj[c][rightPos[c]++] = idx;
            }

            BitSet[] mem = new BitSet[maxId + 1];
            int[] vis = new int[maxId + 1];
            int stamp = 0;
            int[] q = new int[maxId + 5];

            for (int ii = 0; ii < activeN; ii++) {
                int start = activeList[ii];
                stamp++;
                BitSet bs = new BitSet(maxId + 1);
                int head = 0, tail = 0;

                vis[start] = stamp;
                bs.set(start);
                q[tail++] = start;

                while (head < tail) {
                    int cur = q[head++];

                    int[] la = leftAdj[cur];
                    if (la != null) {
                        for (int p : la) {
                            int y = op1[p], z = op2[p];
                            if (vis[y] != stamp) {
                                vis[y] = stamp;
                                bs.set(y);
                                q[tail++] = y;
                            }
                            if (vis[z] != stamp) {
                                vis[z] = stamp;
                                bs.set(z);
                                q[tail++] = z;
                            }
                        }
                    }

                    int[] ra = rightAdj[cur];
                    if (ra != null) {
                        for (int p : ra) {
                            int x = lhs[p];
                            int y = op1[p], z = op2[p];
                            int other = (cur == y ? z : y);
                            if (vis[other] == stamp && vis[x] != stamp) {
                                vis[x] = stamp;
                                bs.set(x);
                                q[tail++] = x;
                            }
                        }
                    }
                }
                mem[start] = bs;
            }

            DSU dsu = new DSU(maxId);
            for (int ii = 0; ii < activeN; ii++) {
                int i = activeList[ii];
                BitSet bs = mem[i];
                for (int j = bs.nextSetBit(i + 1); j >= 0; j = bs.nextSetBit(j + 1)) {
                    if (active[j]) {
                        BitSet bj = mem[j];
                        if (bj != null && bj.get(i)) dsu.union(i, j);
                    }
                }
            }

            int[] repToIdx = new int[maxId + 1];
            Arrays.fill(repToIdx, -1);
            int[] idToIdx = new int[maxId + 1];
            Arrays.fill(idToIdx, -1);

            int k = 0;
            for (int ii = 0; ii < activeN; ii++) {
                int id = activeList[ii];
                int r = dsu.find(id);
                if (repToIdx[r] == -1) repToIdx[r] = k++;
                idToIdx[id] = repToIdx[r];
            }

            int[] L = new int[interCnt];
            int[] Y = new int[interCnt];
            int[] Z = new int[interCnt];
            int[] leftCnt2 = new int[k];
            int[] rightCnt2 = new int[k];

            for (int idx = 0; idx < interCnt; idx++) {
                int a = idToIdx[lhs[idx]];
                int b = idToIdx[op1[idx]];
                int c = idToIdx[op2[idx]];
                L[idx] = a; Y[idx] = b; Z[idx] = c;
                leftCnt2[a]++;
                rightCnt2[b]++;
                rightCnt2[c]++;
            }

            int[][] leftAdj2 = new int[k][];
            int[][] rightAdj2 = new int[k][];
            int[] leftPos2 = new int[k];
            int[] rightPos2 = new int[k];

            for (int i = 0; i < k; i++) {
                if (leftCnt2[i] > 0) leftAdj2[i] = new int[leftCnt2[i]];
                if (rightCnt2[i] > 0) rightAdj2[i] = new int[rightCnt2[i]];
            }
            for (int idx = 0; idx < interCnt; idx++) {
                int a = L[idx], b = Y[idx], c = Z[idx];
                leftAdj2[a][leftPos2[a]++] = idx;
                rightAdj2[b][rightPos2[b]++] = idx;
                rightAdj2[c][rightPos2[c]++] = idx;
            }

            BitSet[] inSet = new BitSet[k];
            for (int i = 0; i < k; i++) inSet[i] = new BitSet(k);

            ArrayDeque<Integer> dq = new ArrayDeque<>();
            boolean[] inq = new boolean[k];

            for (int i = 0; i < recCnt; i++) {
                int a = idToIdx[recA[i]];
                int b = idToIdx[recB[i]];
                if (!inSet[b].get(a)) {
                    inSet[b].set(a);
                    if (!inq[b]) {
                        inq[b] = true;
                        dq.add(b);
                    }
                }
            }

            while (!dq.isEmpty()) {
                int v = dq.poll();
                inq[v] = false;

                int[] la = leftAdj2[v];
                if (la != null) {
                    for (int idx : la) {
                        int y = Y[idx], z = Z[idx];
                        if (addAll(inSet[y], inSet[v]) && !inq[y]) {
                            inq[y] = true;
                            dq.add(y);
                        }
                        if (addAll(inSet[z], inSet[v]) && !inq[z]) {
                            inq[z] = true;
                            dq.add(z);
                        }
                    }
                }

                int[] ra = rightAdj2[v];
                if (ra != null) {
                    for (int idx : ra) {
                        int x = L[idx], y = Y[idx], z = Z[idx];
                        BitSet cand = (BitSet) inSet[y].clone();
                        cand.and(inSet[z]);
                        cand.andNot(inSet[x]);
                        if (!cand.isEmpty()) {
                            inSet[x].or(cand);
                            if (!inq[x]) {
                                inq[x] = true;
                                dq.add(x);
                            }
                        }
                    }
                }
            }

            boolean ok = true;

            for (int i = 0; i < nrecCnt && ok; i++) {
                int a = idToIdx[nrecA[i]];
                int b = idToIdx[nrecB[i]];
                if (inSet[b].get(a)) ok = false;
            }

            if (ok) {
                BitSet[] outSet = new BitSet[k];
                int[] indeg = new int[k];

                for (int v = 0; v < k; v++) {
                    BitSet inc = inSet[v];
                    indeg[v] = inc.cardinality();
                    for (int u = inc.nextSetBit(0); u >= 0; u = inc.nextSetBit(u + 1)) {
                        if (outSet[u] == null) outSet[u] = new BitSet(k);
                        outSet[u].set(v);
                    }
                }

                ArrayDeque<Integer> topo = new ArrayDeque<>();
                for (int v = 0; v < k; v++) if (indeg[v] == 0) topo.add(v);

                int processed = 0;
                while (!topo.isEmpty()) {
                    int u = topo.poll();
                    processed++;
                    BitSet nb = outSet[u];
                    if (nb == null) continue;
                    for (int v = nb.nextSetBit(0); v >= 0; v = nb.nextSetBit(v + 1)) {
                        indeg[v]--;
                        if (indeg[v] == 0) topo.add(v);
                    }
                }
                if (processed != k) ok = false;
            }

            out.append(ok ? "yes\n" : "no\n");
        }

        System.out.print(out);
    }
}