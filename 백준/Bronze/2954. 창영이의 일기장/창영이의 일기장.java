import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                i += 2;
            }
            answer.append(c);
        }
        System.out.println(answer.toString());
    }
}