import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");
        Arrays.stream(arr)
            .mapToInt(Integer::parseInt)
            .sorted()
            .map(i -> {
                System.out.printf("%d ", i);
                return i;
            })
            .toArray();
        
    }
}