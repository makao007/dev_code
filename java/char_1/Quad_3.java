class Quad_3 {
    double a,b,c;
    public double getA () { return a;}
    public double getB () { return b;}
    public double getC () { return c;}

    public void setA (double newA ) { a = newA; }
    public void setB (double newB ) { b = newB; }
    public void setC (double newC ) { c = newC; }

    public Quad_3 () {
        a = 0;
        b = 0;
        c = 0;
    }

    public Quad_3 (double newA,double newB,double newC) {
        a = newA;
        b = newB;
        c = newC;
    }


    double b2a4 () {
        return (b*b-4*a*c);
    }
    
    double x1,x2;
    void cal () {
        if (b2a4() == 0)
            System.out.println("x1=x2=" + ((-b-Math.sqrt (b2a4()))/(2*a)));
        else if (b2a4() > 0) {
            System.out.println("x1=" + ((-b-Math.sqrt(b2a4()))/(2*a)));
            System.out.println("x2=" + ((-b+Math.sqrt(b2a4()))/(2*a)));
        }
        else
            System.out.println("no result");
    }

    public static void main (String [] args)
    {
        Quad_3 q = new Quad_3 (1,2,1);
        q.cal();
    }

}

