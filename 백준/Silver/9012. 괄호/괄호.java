import java.util.Scanner;

public class Main {
//    public static void main(String[] args) {
//        String AbRoute = "C:\\Users\\qkrckstjq\\Desktop\\backend\\java-server-example\\src\\Data.json";
//        String rlRoute = "..\\Data.json";
//        JsonFileReader reader1 = new JsonFileReader(AbRoute);
//        JsonFileReader reader2 = new JsonFileReader(rlRoute);
//        reader1.readJsonFileToText();
//        reader2.readJsonFileToText();
//    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int stack = 0;
        StringBuilder answer = new StringBuilder();

        int index = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < index; i++) {
            String ps = scanner.nextLine();
            char first = ps.charAt(0);

            for (char p : ps.toCharArray()) {
                if(p == '(') {
                    stack++;
                } else {
                    stack--;
                }
                if(stack < 0) {
                    answer.append("NO\n");
                    break;
                }
            }
            
            if (stack == 0) {
                answer.append("YES\n");
            } else if (stack > 0){
                answer.append("NO\n");
            }
            stack = 0;
        }

        System.out.println(answer);
    }
}
