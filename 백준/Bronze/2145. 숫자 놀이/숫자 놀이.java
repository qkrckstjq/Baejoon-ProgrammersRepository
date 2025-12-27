import java.io.*;

class Main {
    public static int temp;
    public static String result;
    
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while((input = rd.readLine()) != null && !input.equals("0")) {
            result = "";
            recursion(input);
            System.out.println(result);
        }
    }
    
    public static void recursion(String sNum) {
        if(sNum.length() == 1) {
            result = sNum;
            return;
        }
        temp = 0;
        for(int i = 0; i < sNum.length(); i++) {
            temp += sNum.charAt(i) - '0';
        }
        recursion(Integer.toString(temp));
        return;
    }
}