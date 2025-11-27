import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] weight = new long[10];     // A~J 각각의 자릿값 가중치 합
        boolean[] leading = new boolean[10]; // 맨 앞에 나온 적 있는지(0 배정 금지)

        // 입력 처리 + 가중치 계산
        for (int i = 0; i < N; i++) {
            String s = br.readLine();     // 공백 없이 들어오므로 trim 불필요
            int firstIdx = s.charAt(0) - 'A';
            leading[firstIdx] = true;

            long p = 1L;
            for (int j = s.length() - 1; j >= 0; j--) {
                int idx = s.charAt(j) - 'A';
                weight[idx] += p;
                p *= 10L;
            }
        }

        // A~J 전부 한 번 이상 등장했는지 체크
        boolean allUsed = true;
        for (int i = 0; i < 10; i++) {
            if (weight[i] == 0L) {   // 한 번도 안 나온 알파벳 존재
                allUsed = false;
                break;
            }
        }

        // 전부 사용된 경우: 0을 줄 알파벳 하나 골라서 그 가중치를 0으로 만든다
        if (allUsed) {
            long min = Long.MAX_VALUE;
            int zeroIdx = -1;

            // 맨 앞에 나온 적 없는 알파벳 중에서 가중치가 가장 작은 애를 고른다
            for (int i = 0; i < 10; i++) {
                if (!leading[i] && weight[i] < min) {
                    min = weight[i];
                    zeroIdx = i;
                }
            }
            // 문제 특성상 zeroIdx는 반드시 존재한다고 가정
            weight[zeroIdx] = 0L;
        }

        // 가중치 정렬 (오름차순)
        Arrays.sort(weight);

        // 가장 큰 가중치에 9, 그 다음 8, ... , 제일 작은 가중치에 0 배정
        long answer = 0L;
        int digit = 9;
        for (int i = 9; i >= 0; i--) {
            answer += weight[i] * digit;
            digit--;
        }

        System.out.println(answer);
    }
}
