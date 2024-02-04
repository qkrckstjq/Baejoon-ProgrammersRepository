
import java.util.*;
public class Main {
    public static int[] ufa;

    public static int find (int vertex) {
        if(ufa[vertex] == vertex) {
            return vertex;
        }
        return ufa[vertex] = find(ufa[vertex]);
    }

    public static void union (int a, int b) {
        int fa = find(a);
        int fb = find(b);
        if(fa != fb) {
            ufa[fb] = ufa[fa];
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] splitedVI = sc.nextLine().split(" ");

        int vertex = Integer.parseInt(splitedVI[0]);
        int inputNumber = Integer.parseInt(splitedVI[1]);

        ufa = new int[vertex+1];


        for(int i = 0; i < ufa.length; i++) {
            ufa[i] = i;
        }

        for(int i = 0; i < inputNumber; i++) {
            String[] BVV = sc.nextLine().split(" ");
            int type = Integer.parseInt(BVV[0]);
            int vertex1 = Integer.parseInt(BVV[1]);
            int vertex2 = Integer.parseInt(BVV[2]);

            if(type == 0) {
                union(vertex1, vertex2);
            } else {
                if (find(vertex1) == find(vertex2)) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
        
    }



}
