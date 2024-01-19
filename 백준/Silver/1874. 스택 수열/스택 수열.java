import java.util.Scanner;
import java.util.Stack;

//public class JsonFileReaderTest {
////    public static void main(String[] args) {
////        String AbRoute = "C:\\Users\\qkrckstjq\\Desktop\\backend\\java-server-example\\src\\Data.json";
////        String rlRoute = "..\\Data.json";
////        JsonFileReader reader1 = new JsonFileReader(AbRoute);
////        JsonFileReader reader2 = new JsonFileReader(rlRoute);
////        reader1.readJsonFileToText();
////        reader2.readJsonFileToText();
////    }
//}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder answer = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(scanner.nextLine());

        int currentNumber = 1;
        //가장 마지막에 스택에 푸쉬될 수 + 1;

        for (int i = 0; i < n; i++) {
            int target = Integer.parseInt(scanner.nextLine());

            while (currentNumber <= target) {
                stack.push(currentNumber);
                answer.append("+\n");
                currentNumber++;
            }

            if (!stack.isEmpty() && stack.peek() == target) {
                stack.pop();
                answer.append("-\n");
            } else {
                System.out.println("NO");
                return;
            }
        }
        //이미 스택이 비어있으면 만들 수 없음
        System.out.println(answer);
    }
}
// 1. 스택의 마지막 값이 입력받은 값보다 크면 이미 스택에서 팝을 할 시점을 놓침
