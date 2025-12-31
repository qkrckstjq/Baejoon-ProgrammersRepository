import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int w = Integer.parseInt(input[0]);
        int h = Integer.parseInt(input[1]);
        int x = Integer.parseInt(input[2]);
        int y = Integer.parseInt(input[3]);
        int t = Integer.parseInt(input[4]);
        
        int minY = y;
        int minX = x;
        
        int maxY = minY + h;
        int maxX = minX + w;
        
        double cY = (minY + maxY) / 2;
        
        double[] cen1 = new double[]{cY, minX};
        double[] cen2 = new double[]{cY, maxX};
        
        int answer = 0;
        for(int i = 0; i < t; i++) {
            String[] xy = rd.readLine().split(" ");
            double curY = Double.parseDouble(xy[1]);
            double curX = Double.parseDouble(xy[0]);
            
            if(minY <= curY && curY <= maxY && minX <= curX && curX <= maxX) {
                answer += 1;
                continue;
            }
            
            double d1 = getD(cen1, new double[]{curY, curX});
            double d2 = getD(cen2, new double[]{curY, curX});
            
            // System.out.printf("\n%f, %f\n", d1, d2);
            
            if(d1 <= maxY - cY || d2 <= maxY - cY) {
                answer += 1;
            }
        }
        
        System.out.println(answer);
    }
    
    public static double getD(double[] a, double[] b) {
        double w = Math.abs(a[1] - b[1]);
        double h = Math.abs(a[0] - b[0]);
        return Math.sqrt(w * w + h * h);
    }
}