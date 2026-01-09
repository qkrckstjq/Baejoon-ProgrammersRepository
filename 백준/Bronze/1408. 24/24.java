import java.io.*;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int start = toInt(rd.readLine());
        int end = toInt(rd.readLine());
        int dif = end >= start ? end - start : (end + 24 * 3600) - start;
        String h = Integer.toString(dif / 3600);
        String m = Integer.toString((dif % 3600) / 60);
        String s = Integer.toString(dif % 3600 % 60);
        
        StringBuilder answer = new StringBuilder("");
        answer.append("0".repeat(2 - h.length()) + h + ":");
        answer.append("0".repeat(2 - m.length()) + m + ":");
        answer.append("0".repeat(2 - s.length()) + s);
        System.out.println(answer.toString());
    }
    
    public static int toInt(String input) {
        String[] temp = input.split(":");
        int h = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        int s = Integer.parseInt(temp[2]);
        return 3600 * h + 60 * m + s;
    }
}