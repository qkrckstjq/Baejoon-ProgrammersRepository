import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            String line = rd.readLine();
            if(line.equals("#")) break;
            char target = line.charAt(0);
            String str = line.substring(2, line.length()).toLowerCase();
            int result = 0;
            for(int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if(target == c) {
                    result += 1;
                }
            }
            System.out.printf("%s %d\n", target, result);
        }
    }
}