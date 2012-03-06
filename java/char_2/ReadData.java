import java.io.*;

class ReadData {
    char c;
    int num=0;
    public static void main (String [] args) throws IOException
    {
        ReadData r = new ReadData();
        r.c = (char)System.in.read();
        while (r.c!='#') {
            r.num ++;
            r.c = (char)System.in.read();
        }
        System.out.println("word length is " + r.num);
    }
}
