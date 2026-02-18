import java.io.*;
import java.util.*;

public class Main {
    static int N, F;
    static int[] w;
    static int[] ans;
    static boolean[] used;
    static boolean found = false;

    static int[] binomRow(int n) {
        int[] row = new int[n + 1];
        row[0] = 1;
        for (int i = 1; i <= n; i++) {
            row[i] = 1;
            for (int j = i - 1; j >= 1; j--) row[j] += row[j - 1];
        }
        return row;
    }

    static int boundAdd(int idx, boolean min) {
        ArrayList<Integer> nums = new ArrayList<>();
        for (int x = 1; x <= N; x++) if (!used[x]) nums.add(x);

        int m = nums.size();
        int[] weights = new int[m];
        for (int i = 0; i < m; i++) weights[i] = w[idx + i];

        Collections.sort(nums);
        Arrays.sort(weights);
        for (int i = 0, j = m - 1; i < j; i++, j--) {
            int t = weights[i];
            weights[i] = weights[j];
            weights[j] = t;
        }

        int add = 0;
        if (min) {
            for (int i = 0; i < m; i++) add += nums.get(i) * weights[i];
        } else {
            for (int i = 0; i < m; i++) add += nums.get(m - 1 - i) * weights[i];
        }
        return add;
    }

    static void dfs(int idx, int sum) {
        if (found) return;

        if (idx == N) {
            if (sum == F) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < N; i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(ans[i]);
                }
                System.out.print(sb);
                found = true;
            }
            return;
        }

        int minAdd = boundAdd(idx, true);
        int maxAdd = boundAdd(idx, false);
        if (F < sum + minAdd || F > sum + maxAdd) return;

        for (int x = 1; x <= N; x++) {
            if (used[x]) continue;
            used[x] = true;
            ans[idx] = x;
            dfs(idx + 1, sum + x * w[idx]);
            used[x] = false;
            if (found) return;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        F = Integer.parseInt(st.nextToken());

        int[] row = binomRow(N - 1);
        w = new int[N];
        for (int i = 0; i < N; i++) w[i] = row[i];

        ans = new int[N];
        used = new boolean[N + 1];

        dfs(0, 0);
    }
}