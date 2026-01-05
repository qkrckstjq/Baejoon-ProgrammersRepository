import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split("-");
        StringBuilder answer = new StringBuilder("");
        for(String s : input) {
            answer.append(s.charAt(0));
        }
        System.out.println(answer.toString());
    }
}