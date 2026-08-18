import java.util.ArrayList;
import java.util.Scanner;

public class Sistema {

    static class I {
        public String a;
        public double b;
        public int c;

        public I(String a, double b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
    }

    static class P {
        public String a;
        public String b;
        public ArrayList<I> c = new ArrayList<>();

        public void x() {
            double s = 0.0;
            double d = 0.0;

            for (I i : c) {
                double v = i.b * i.c;
                s = s + v;

                if (i.a.equals("LIVRO")) {
                    d = d + v * 0.05;
                } else if (i.a.equals("ELETRONICO")) {
                    d = d + v * 0.02;
                } else if (i.a.equals("OUTRO")) {
                    d = d + 0;
                }
            }

            double r = s - d;

            if (a.equals("PREMIUM")) {
                double z = r * 0.10;
                d = d + z;
                r = r - z;
            }

            double f = 0.0;

            if (b.equals("RETIRADA")) {
                f = 0.0;
            } else if (b.equals("NORMAL")) {
                if (r >= 150.0) {
                    f = 0.0;
                } else {
                    f = 12.0;
                }
            } else if (b.equals("EXPRESSA")) {
                f = 25.0;
            }

            double t = r + f;

            System.out.printf("SUBTOTAL=%.2f%n", s);
            System.out.printf("DESCONTO=%.2f%n", d);
            System.out.printf("FRETE=%.2f%n", f);
            System.out.printf("TOTAL=%.2f%n", t);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        P p = new P();

        p.a = sc.nextLine().trim();
        p.b = sc.nextLine().trim();

        int n = Integer.parseInt(sc.nextLine().trim());

        for (int k = 0; k < n; k++) {
            String[] x = sc.nextLine().trim().split("\\s+");

            p.c.add(
                new I(
                    x[0],
                    Double.parseDouble(x[1]),
                    Integer.parseInt(x[2])
                )
            );
        }

        p.x();

        sc.close();
    }
}