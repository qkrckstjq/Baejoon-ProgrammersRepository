import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = "";
        while((input = rd.readLine()) != null) {
            if(input.equals("#")) break;
            String[] arr = input.split(" ");
            StringBuilder answer = new StringBuilder("");
            for(int i = 0; i < arr.length; i++) {
                StringBuilder str = new StringBuilder(arr[i]);
                answer.append(str.reverse()).append(" ");
            }
            System.out.println(answer.toString());
        }
    }
}