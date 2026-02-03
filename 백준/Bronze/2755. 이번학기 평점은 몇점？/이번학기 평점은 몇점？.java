import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(rd.readLine());
        int i = T;
        float totalGrade = 0;
        float totalRank = 0;
        float answer = 0;
        while(0 < i--) {
            String[] input = rd.readLine().split(" ");
            totalGrade += (Integer.parseInt(input[1]) * def(input[2]));
            totalRank += Integer.parseInt(input[1]);
        }
        System.out.printf("%.2f", totalGrade / totalRank);
    }
    
    public static float def(String input) {
        if(input.equals("F")) return 0;
        char rank = input.charAt(0);
        char apl = input.charAt(1);
        
        float answer = (rank * -1) + 69;
        answer += (apl == '+') ? 0.3 : (apl == '-') ? -0.3 : 0;
        return answer;
    }
}