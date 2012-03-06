class Maths {
    public static double sec (double a) {
        return 1.0/Math.sin(a);
    }

    public static double cosec (double a) {
        return 1.0/Math.cos(a);
    }

    public static double cotan(double a) {
        return Math.cos(a)/Math.sin(a);
    }

}

class TestMaths {
    public static void main (String [] args)
    {
        double a=3.14/4.0;
        System.out.println("sec=" + Maths.sec(a));
        System.out.println("cosec=" + Maths.cosec(a));
        System.out.println("cotan=" + Maths.cotan(a));
    }
}

