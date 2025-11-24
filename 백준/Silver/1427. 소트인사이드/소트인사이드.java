import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer = Arrays.stream(sc.nextLine().split(""))
            .sorted(Comparator.comparing(s -> Integer.parseInt(s) * -1))
            .reduce("", (result, i) -> result + i);
        System.out.println(answer);
    }
}