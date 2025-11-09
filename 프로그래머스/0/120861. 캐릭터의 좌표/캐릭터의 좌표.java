import java.util.*;
class Solution {
    public int[] dy = new int[]{0, 0, 1, -1};
    public int[] dx = new int[]{1, -1, 0, 0};
    public int[] solution(String[] keyinput, int[] board) {
        Map<String, Integer> dir = new HashMap<>();
        dir.put("left", 1);
        dir.put("right", 0);
        dir.put("up", 2);
        dir.put("down", 3);
        int x = (board[0] - 1) / 2;
        int y = (board[1] - 1) / 2;
        return Arrays.stream(keyinput)
            .reduce(new int[]{0, 0}, (result, str) -> {
                int idx = dir.get(str);
                result[0] += (Math.abs(result[0] + dx[idx]) <= x ? dx[idx] : 0);
                result[1] += (Math.abs(result[1] + dy[idx]) <= y ? dy[idx] : 0);
                return result;
            }, (a, b) -> new int[]{a[0] + b[0], a[1] + b[1]});
    }
}