class Point {
    private int x;
    private int y;

    void setX (int newX) { x = newX; }
    void setY (int newY) { y = newY; }

    int getX () { return x; }
    int getY () { return y; }

    Point (int newX,int newY) {
        x = newX;
        y = newY;
    }

    public String toString () { return ("Point  x:" + x + "; y:" + y); }
}


class ColorPoint extends Point {
    private int color ;

    void setColor (int newColor) { color = newColor; }
    int  getColor () { return color; }

    ColorPoint (int newX,int newY, int newColor) {
        super (newX,newY);
        color = newColor;
    }
    public String toString () { return "Color " + super.toString() + "; color:" + color ; }
}

public class MapColorPoint extends ColorPoint {
    private String name;
    
    void setName (String newName) { name = newName; }
    String getName () { return name; }

    MapColorPoint (int newX, int newY, int newColor, String newName ) {
        super (newX,newY,newColor);
        name = newName;
    }

    public String toString () { return ("Map " + super.toString() + "; name:" + name); }

    public static void main (String [] args)
    {
        Point p1 = new MapColorPoint (3,4,120,"Califolina");
        System.out.println(p1);

        p1 = new ColorPoint(3,4,120);
        System.out.println(p1);

        p1 = new Point(3,4);
        System.out.println(p1);
    }

}


