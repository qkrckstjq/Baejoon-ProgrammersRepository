import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();
        int num = 0;
        for(int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if('a' <= c && c <= 'z') {
                num += (c - 96);
            } else {
                num += (c - 38);
            }
        } 
        boolean[] primeList = new boolean[num + 1];
        for(int i = 2; i <= (int) Math.sqrt(num); i++) {
            if(!primeList[i]) {
                for(int j = i; j <= num; j += i) {
                    if(num % j == 0) {
                        System.out.println("It is not a prime word.");
                        return;
                    }
                    primeList[j] = true;
                }
            }
        }
        System.out.println("It is a prime word.");
    }
}