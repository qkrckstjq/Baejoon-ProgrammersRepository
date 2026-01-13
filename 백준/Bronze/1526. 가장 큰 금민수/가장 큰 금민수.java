import java.io.*;

class Main {
    public static int answer = 0;
    public static int target;
    
    public static void main(String[] args) throws Exception {        
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        target = Integer.parseInt(rd.readLine());
        
        dfs("");
        System.out.println(answer);
    }
    
    public static void dfs(String num) {
        int temp = 0;
        if(num.length() > 0) {
            temp = Integer.parseInt(num);
            if(temp > target) {
                return;
            }    
        }
        
        answer = Math.max(temp, answer);
        
        dfs(num + "4");
        dfs(num + "7");
    }
}