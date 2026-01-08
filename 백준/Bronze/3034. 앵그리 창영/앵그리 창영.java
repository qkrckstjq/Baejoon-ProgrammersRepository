import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int t = Integer.parseInt(input[0]);
        double w = Double.parseDouble(input[1]);
        double h = Double.parseDouble(input[2]);
        
        double maxL = Math.sqrt(w * w + h * h);
        for(int i = 0; i <t; i++ ){
            int num = Integer.parseInt(rd.readLine());
            if(maxL >= num) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
        }
            
    }    
}
