import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = new String[2];
        int o = 0;
        int w = 0;
        int i = 1;
        boolean live = true;
        while(true) {
            input = reader.readLine().split(" ");
            if(input[0].equals("0") && input[1].equals("0")) break;
            if(input[0].equals("E")) {
                if(!live) continue;
                w -= Integer.parseInt(input[1]);
                if(w <= 0) live = false;
            } else if(input[0].equals("F")) {
                if(!live) continue;
                w += Integer.parseInt(input[1]);
            } else if(input[0].equals("#")){
                if(w <= 0) {
                    System.out.printf("%d RIP\n", i);
                } else if(o / 2 < w && w < o * 2) {
                    System.out.printf("%d :-)\n", i);
                } else {
                    System.out.printf("%d :-(\n", i);
                }
                i++;
                live = true;
            } else {
                o = Integer.parseInt(input[0]);
                w = Integer.parseInt(input[1]);
            }
        }
        return;
    }
}