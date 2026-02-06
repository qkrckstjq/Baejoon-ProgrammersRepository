import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();
        int[] arr = new int[4];
        arr[1] = 1;
        for(int i = 0; i < input.length(); i++) {
            int j, h;
            if(input.charAt(i) == 'A') {
                j = 1;
                h = 2;
            } else if(input.charAt(i) == 'B') {
                j = 2;
                h = 3;
            } else {
                j = 1;
                h = 3;
            }
            int temp = arr[j];
            arr[j] = arr[h];
            arr[h] = temp;
        }
        for(int i = 1; i <= 3; i++) {
            if(arr[i] == 1) {
                System.out.println(i);
            }
        }
    }
}