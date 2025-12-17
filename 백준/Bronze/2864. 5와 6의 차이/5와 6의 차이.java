import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] inputList = rd.readLine().split(" ");
        int maxA = Integer.parseInt(replaceString(inputList[0], "6"));
        int minA = Integer.parseInt(replaceString(inputList[0], "5"));
        
        int maxB = Integer.parseInt(replaceString(inputList[1], "6"));
        int minB = Integer.parseInt(replaceString(inputList[1], "5"));
        
        System.out.printf("%d %d", minA + minB, maxA + maxB);
    }
    
    public static String replaceString(String input, String trans) {
        if(trans.equals("5")) {
            return input.replaceAll("6", trans);
        } else {
            return input.replaceAll("5", trans);
        }
        
    }
}
