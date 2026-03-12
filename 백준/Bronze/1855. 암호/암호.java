import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        String input = rd.readLine();
        int row = n, col = input.length() / n + 1;
        String[][] list = new String[col][row];
        
        int idx = 0;
        int rv = 0;
        for(int i = 0; i < col; i++) {
            for(int j = 0; j < row; j++) {
                if(idx >= input.length()) break;
                list[i][rv % 2 != 0 ? (row - 1) - j : j] = Character.toString(input.charAt(idx++));
            }
            rv++;
        }
        
        // for(int i = 0; i < col; i++) {
        //     for(int j = 0; j < row; j++) {
        //         if(list[i][j] == null) break;
        //         System.out.printf(list[i][j]);
        //     }
        //     System.out.println();
        // }
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(list[j][i] == null) break;
                answer.append(list[j][i]);
            } 
        }
        
        System.out.println(answer.toString());
    }
}