import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder answer = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(scanner.nextLine());

        int currentNumber = 1;

        for (int i = 0; i < n; i++) {
            int target = Integer.parseInt(scanner.nextLine());

            // 현재 숫자가 목표 숫자보다 작을 때까지 push
            while (currentNumber <= target) {
                stack.push(currentNumber);
                answer.append("+\n");
                currentNumber++;
            }

            // 스택의 맨 위가 목표 숫자와 같을 때 pop
            if (!stack.isEmpty() && stack.peek() == target) {
                stack.pop();
                answer.append("-\n");
            } else {
                // 만들 수 없는 경우
                System.out.println("NO");
                return;
            }
        }

        System.out.println(answer);
    }
}