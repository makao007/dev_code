class Point {
    private int x;
    private int y;
    public int getX () {
        return x;
    }
    public int getY () {
        return y;
    }
    public void setX (int newX){
        x = newX;
    }
    public void setY (int newY){
        y = newY;
    }
    double distance (){
        return (Math.sqrt (x*x+y*y));
    }
    public static void main (String [] args)
    {
        Point p1 = new Point ();
        //p1.setX (10);
        //p1.setY (8);
        System.out.println ("distance = " + p1.distance());
    }
}
