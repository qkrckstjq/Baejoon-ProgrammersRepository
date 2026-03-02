import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int houseCnt, chickenCnt;
    static int[] hx, hy, cx, cy;
    static int[][] dist;
    static int[] sel;
    static int best = Integer.MAX_VALUE;

    static void dfs(int start, int chosen) {
        if (chosen == M) {
            int total = 0;
            for (int i = 0; i < houseCnt; i++) {
                int minD = Integer.MAX_VALUE;
                for (int j = 0; j < M; j++) {
                    int d = dist[i][sel[j]];
                    if (d < minD) minD = d;
                }
                total += minD;
                if (total >= best) return;
            }
            if (total < best) best = total;
            return;
        }

        if (chickenCnt - start < M - chosen) return;

        for (int i = start; i < chickenCnt; i++) {
            sel[chosen] = i;
            dfs(i + 1, chosen + 1);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int maxCells = N * N;
        hx = new int[maxCells];
        hy = new int[maxCells];
        cx = new int[maxCells];
        cy = new int[maxCells];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int v = Integer.parseInt(st.nextToken());
                if (v == 1) {
                    hx[houseCnt] = i;
                    hy[houseCnt] = j;
                    houseCnt++;
                } else if (v == 2) {
                    cx[chickenCnt] = i;
                    cy[chickenCnt] = j;
                    chickenCnt++;
                }
            }
        }

        dist = new int[houseCnt][chickenCnt];
        for (int i = 0; i < houseCnt; i++) {
            for (int j = 0; j < chickenCnt; j++) {
                dist[i][j] = Math.abs(hx[i] - cx[j]) + Math.abs(hy[i] - cy[j]);
            }
        }

        sel = new int[M];
        dfs(0, 0);

        System.out.print(best);
    }
}