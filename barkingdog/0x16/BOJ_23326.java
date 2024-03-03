import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class BOJ_23326 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        TreeSet<Integer> tour = new TreeSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            if (Integer.parseInt(st.nextToken()) == 1) {
                tour.add(i);
            }
        }

        int x = 1;
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            if (cmd == 1) {
                int i = Integer.parseInt(st.nextToken());
                if (tour.contains(i)) {
                    tour.remove(i);
                } else {
                    tour.add(i);
                }
            } else if (cmd == 2) {
                int i = Integer.parseInt(st.nextToken());
                x = (x + i) % N;
                if (x == 0) {
                    x = N;
                }
            } else { // 3
                if (tour.isEmpty()) {
                    sb.append("-1").append("\n");
                    continue;
                }

                if (tour.contains(x)) {
                    sb.append("0").append("\n");
                    continue;
                }

                Integer i = tour.higher(x);
                if (i == null) {
                    sb.append(N - x + tour.higher(0)).append("\n");
                } else {
                    sb.append(i - x).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}
