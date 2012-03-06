package learn;

class t1 {
    double a=123,b,c;
    double x1,x2;
    t1 () {
        a = 1;
        b = 2;
        c = 3;
    }
    int t1 (double newA,double newB,double newC) {

        a = newA;
        b = newB;
        c = newC;
        return 1;
    }
    public String toString (){
        return (a + " " + b + " " + c + " ");
    }
}
