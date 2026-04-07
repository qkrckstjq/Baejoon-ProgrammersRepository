import java.io.*;

class Main { 
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();
        int answer = 0;
        int num = 1;
        for(int i = 0; i < input.length(); i++) {
            for(int k = 0; k < input.length(); k++) {
                if(k + num * 2 <= input.length()) {
                    int sumA = 0;
                    int sumB = 0;
                    for(int j = k; j < k + num; j++) {
                        sumA += input.charAt(j) - '0';
                    }
                    
                    for(int j = k + num; j < k + num * 2; j++) {
                        sumB += input.charAt(j) - '0';
                    }
                    // System.out.printf("%d, %d\n", sumA, sumB);
                    if(sumA == sumB) answer = num;
                } else {
                    break;
                }
            }
            num++;
        }
        System.out.println(answer * 2);
    }
}