import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        while(t-- > 0) {
            String[] input = rd.readLine().split(" ");
            StringBuilder answer = new StringBuilder("");
            int i = input[0].length() - 1;
            int j = input[1].length() - 1;
            int temp = 0;
            while(i >= 0 || j >= 0) {
                int num1 = i < 0 ? 0 : input[0].charAt(i--) - '0';
                int num2 = j < 0 ? 0 : input[1].charAt(j--) - '0';
                int s = num1 + num2 + temp;
                if(s == 0) {
                    answer.append("0");
                } else if(s == 1) {
                    answer.append("1");
                    temp = 0;
                } else if(s == 2) {
                    answer.append("0");
                    temp = 1;
                } else {
                    answer.append("1");
                    temp = 1;
                }
            }
            if(temp == 1) answer.append("1");
            String result = answer.reverse().toString();
            int idx;
            for(idx = 0; idx < result.length(); idx++) {
                if(result.charAt(idx) == '1') break;
            }
            System.out.println(idx == result.length() ? "0" : result.substring(idx));
        }
    }
}