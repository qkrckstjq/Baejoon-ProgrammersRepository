import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] x = {a, b, c, d};
        Arrays.sort(x);

        if (x[0] == x[3]) {                    // 4개 모두 같음
            return 1111 * x[0];
        }
        if (x[0] == x[2]) {                    // (3,1) - 앞 세 개
            int p = x[0], q = x[3];
            int t = 10 * p + q;
            return t * t;
        }
        if (x[1] == x[3]) {                    // (3,1) - 뒤 세 개
            int p = x[1], q = x[0];
            int t = 10 * p + q;
            return t * t;
        }
        if (x[0] == x[1] && x[2] == x[3]) {    // (2,2)
            return (x[0] + x[2]) * Math.abs(x[0] - x[2]);
        }
        if (x[0] == x[1]) {                    // (2,1,1)
            return x[2] * x[3];
        }
        if (x[1] == x[2]) {                    // (2,1,1)
            return x[0] * x[3];
        }
        if (x[2] == x[3]) {                    // (2,1,1)
            return x[0] * x[1];
        }
        return x[0];                           // 모두 다름
    }
}
