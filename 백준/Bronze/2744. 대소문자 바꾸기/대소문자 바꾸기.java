import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < input.length(); i++) {
            String w = Character.toString(input.charAt(i));
            String uW = w.toUpperCase();
            if(w.equals(uW)) {
                answer.append(w.toLowerCase());
            } else {
                answer.append(uW);
            }
        }
        System.out.println(answer.toString());            
    }
}