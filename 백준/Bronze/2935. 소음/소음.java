import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String op = br.readLine();
        String b = br.readLine();
        StringBuilder answer = new StringBuilder("");
        if(op.equals("*")) {
            answer.append(a);
            for(int i = 0; i < b.length() - 1; i++) {
                answer.append("0");    
            }
        } else {
            int i = a.length() - 1;
            int j = b.length() - 1;
            
            while(i >= 0 || j >= 0) {
                int tA = i < 0 ? 0 : a.charAt(i) - '0';
                int tB = j < 0 ? 0 : b.charAt(j) - '0';
                
                
                int temp = tA + tB;
                answer.append(Integer.toString(temp));
                i--;
                j--;
            }
            answer.reverse();
        }
        System.out.println(answer.toString());
    }
}