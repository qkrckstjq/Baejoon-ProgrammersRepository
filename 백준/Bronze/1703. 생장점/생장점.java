import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while(true) {
            line = rd.readLine();
            if(line.equals("0")) break;
            int answer = 1;
            String[] list = line.split(" ");
            int a = Integer.parseInt(list[0]);
            for(int i = 1; i <= a * 2; i+=2) {
                int mult = Integer.parseInt(list[i]);
                int spli = Integer.parseInt(list[i + 1]);
                answer *= mult;
                answer -= spli;
            }
            System.out.println(answer);
        }
    }
}