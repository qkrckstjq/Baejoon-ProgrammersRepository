import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] yx = rd.readLine().split(" ");
        int n = Integer.parseInt(rd.readLine());
        Double minPrice = Double.parseDouble(yx[0]) / Double.parseDouble(yx[1]);
        for(int i = 0; i < n; i++) {
            String[] input = rd.readLine().split(" ");
            double price = Double.parseDouble(input[0]);
            double g = Double.parseDouble(input[1]);
            price /= g;
            minPrice = Math.min(minPrice, price);
        }
        System.out.printf("%.2f", minPrice * 1000);
    }
}
