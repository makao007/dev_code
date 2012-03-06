// test interface 

class tinterf implements interf {
    double x1,y1;
    public double log (double x) { return Math.log (x); };
    public double  lg (double x) { return Math.log(x)/Math.log(10); }

    double x1plusy1 () { return (x1+y1); }

    tinterf () {
        x1 = 1;
        y1 = 1;
    }

    tinterf (double newX1, double newY1) {
        x1 = newX1;
        y1 = newY1;
    }

    public static void main (String [] args)
    {
        tinterf t = new tinterf (10,14);
        System.out.println(t.x1plusy1());
        System.out.println(t.log(100));
        System.out.println(t.lg(100));
    }
}
