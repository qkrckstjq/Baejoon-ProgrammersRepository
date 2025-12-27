import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while((input = rd.readLine()) != null && !input.equals("0")) {
            String result = recursion(input);
            System.out.println(result);
        }
    }
    
    public static String recursion(String sNum) {
        while(sNum.length() > 1) {
            int temp = 0;
            for(int i = 0; i < sNum.length(); i++) {
                temp += sNum.charAt(i) - '0';
            }
            sNum = Integer.toString(temp);
        }
        return sNum;
    }
}