import java.util.*;

public class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> resultSet = new HashSet<>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                resultSet.add(numbers[i] + numbers[j]);
            }
        }

        List<Integer> resultList = new ArrayList<>(resultSet);
        Collections.sort(resultList);

        int[] answer = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            answer[i] = resultList.get(i);
        }

        return answer;
    }
}