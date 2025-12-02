import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String yName = sc.nextLine();
        int[] yScore = getLOVE(yName);
        
        int N = Integer.parseInt(sc.nextLine());
        String[] nameList = new String[N];
        int[] scoreList = new int[N];
        for(int i = 0; i < N; i++) {
            String name = sc.nextLine();
            int[] nameScore = getLOVE(name);
            nameList[i] = name;
            scoreList[i] = getScore(nameScore, yScore);
        }
        String result = nameList[IntStream.range(0, N)
                .boxed()
                .sorted(Comparator.comparingInt((Integer i) -> scoreList[i] * -1).thenComparing(i -> nameList[i]))
                .findFirst()
                .orElse(0)];
        System.out.println(result);
    }
    
    public static int[] getLOVE(String name) {
        int[] result = new int[4];
        for(int i = 0; i < name.length(); i++) {
            if(name.charAt(i) == 'L') result[0]++;
            if(name.charAt(i) == 'O') result[1]++;
            if(name.charAt(i) == 'V') result[2]++;
            if(name.charAt(i) == 'E') result[3]++;
        }
        return result;
    }
    
    public static int getScore(int[] base, int[] target) {
        int[] temp = new int[]{base[0] + target[0], base[1] + target[1], base[2] + target[2], base[3] + target[3]};
        return ((temp[0] + temp[1]) * (temp[0] + temp[2]) * (temp[0] + temp[3]) * (temp[1] + temp[2]) * (temp[1] + temp[3]) * (temp[2] + temp[3])) % 100;
    }
}