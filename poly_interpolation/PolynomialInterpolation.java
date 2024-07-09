/* *****************************************************************************
 * Given a set of points, determine the polynomial of minimal degree that fits
 **************************************************************************** */

import java.util.ArrayList;
import java.util.List;

public class PolynomialInterpolation {
    static class RationalPoint {
        private Rational x, y;

        public RationalPoint(Rational x, Rational y) {
            this.x = x;
            this.y = y;
        }

        public Rational x() {
            return x;
        }

        public Rational y() {
            return y;
        }

        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    private static List<Polynomial> generatePascal(int N) {
        List<Polynomial> pascal = new ArrayList<>();
        pascal.add(new Polynomial(1, 0));

        Polynomial x = new Polynomial(1, 1);

        for (int i = 0; i < N; i++) {
            pascal.add(pascal.get(i).times(x).plus(pascal.get(i)));
        }

        for (int i = 0; i <= N; i++) {
            pascal.set(i, pascal.get(i).minus(new Polynomial(1, i)));
        }

        return pascal;
    }

    public static Polynomial interpolate(List<RationalPoint> points) {
        if (points.size() == 1) {
            return new Polynomial(points.get(0).y(), 0);
        }

        final Polynomial x = new Polynomial(1, 1);

        List<RationalPoint> differences = new ArrayList<>();

        // boolean isZero = true;
        for (int i = 0; i < points.size() - 1; i++) {
            Rational dy = points.get(i + 1).y().subtract(points.get(i).y());
            // if (dy != 0) {
            //     isZero = false;
            // }
            differences.add(new RationalPoint(points.get(i).x(), dy));
        }


        // if (isZero) {
        //     return new Polynomial(0, 0);
        // }

        Polynomial differencePoly = interpolate(differences);

        if (differencePoly.equals(new Polynomial(0, 0))) {
            return new Polynomial(points.get(0).y(), 0);
        }

        List<Polynomial> pascal = generatePascal(differencePoly.degree() + 1);

        Polynomial temp = differencePoly;
        Polynomial result = new Polynomial(0, 0);
        for (int i = differencePoly.degree() + 1; i > 0; i--) {
            Rational coeff = (temp.degree() == i - 1) ? temp.coeff().divide(new Rational(i, 1)) :
                             new Rational(0, 1);
            Polynomial diff = pascal.get(i).times(new Polynomial(coeff, 0));
            temp = temp.minus(pascal.get(i).times(new Polynomial(coeff, 0)));
            result = result.times(x).plus(new Polynomial(coeff, 0));
        }

        result = result.times(x);

        result = result.plus(
                new Polynomial(points.get(0).y().subtract(result.evaluate(points.get(0).x())),
                               0));

        // StdOut.println(points);
        // StdOut.println(differences);
        // StdOut.println(result);

        return result;
    }

    public static void main(String[] args) {
        int[] x = new int[] { 1, 2, 3, 4, 5, 6, 7, 8 };
        int[] y = new int[] { 1, 588, 28776, 406154, 2859504, 13274478, 46915636, 136936388 };


        List<RationalPoint> points = new ArrayList<>();
        for (int i = 0; i < x.length; i++) {
            points.add(new RationalPoint(new Rational(x[i], 1), new Rational(y[i], 1)));
        }

        Polynomial result = interpolate(points);
        System.out.println(result);
        System.out.println(result.evaluate(x[x.length - 1] + 1));
    }
}
