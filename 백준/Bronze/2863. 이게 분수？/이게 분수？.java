import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input1 = rd.readLine().split(" ");
        String[] input2 = rd.readLine().split(" ");
        
        Double[] arr = new Double[]{Double.parseDouble(input1[0]), Double.parseDouble(input1[1]), Double.parseDouble(input2[1]), Double.parseDouble(input2[0])};
        int[] list = new int[]{0, 1, 2, 3};
        
        double total = 0;
        int cnt = 0;
        for(int i = 0; i < 4; i++) {
            double sum = (arr[list[0]] / arr[list[3]]) + (arr[list[1]] / arr[list[2]]);
            // System.out.println(sum);
            if(total < sum) {
                cnt = i;
                total = sum;
            }
            for(int j = 0; j < 4; j++) {
                if(list[j] - 1 < 0) {
                    list[j] = 3;
                } else {
                    list[j] -= 1;
                }
            }
        }
        System.out.println(cnt);
    }
}