import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int h = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        if (h == 0) {
            sb.append('1');
        } else if (h == 1) {
            sb.append('0');
        } else {
            if ((h & 1) == 1) {
                sb.append('4');
                h -= 1;
            }
            int cnt8 = h / 2;
            for (int i = 0; i < cnt8; i++) sb.append('8');
        }

        System.out.print(sb.toString());
    }
}