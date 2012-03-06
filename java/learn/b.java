public class b {
    int a,b;
    public void t_switch () {
        a = 12;
        switch (a) {
            case 1:
                b = 1;
                break;
            case 2:
                b = 2;
                break;
            case 3:
            case 4:
            case 5:
                b = 5;
                break;
            case 6:
                b = 6;
                break;
            default:
                b = 10;
        }
        System.out.println("test switch");
        System.out.println(b);
    }
    public void t_for () {
        int i;
        for (i=0;i<10;i++)
            System.out.print(i+" ");
    }
    public void t_while () {
        int i,n,sum;
        i = sum = 0;
        n = 10;
        while (i<n) {
            sum += i++;
        }
        System.out.println("sum of 1 to 10 = " + sum);
    }
    void t_do () {
        int i,n,sum;
        i = sum = 0;
        n = 10;
        do {
            sum += i;
            i ++;
        } while (i<n) ;
        System.out.println("test do,sum 1 to 10 equal " + sum);
    }

    void t_type () {
        char c;
        c = 'a';
        int i;
        float f;
        long l;
        double d;
        l = 123L;
        i = (int)l;
        f = 23.23f;
        d = f;
        String s =  new String (" ");
        s = "hello" + i +" " + f + " "+ d;
        System.out.println(s);
    }
    void mysort (int data[]) {
        int i,j,k,temp;
        int length;

        for (i=0,length=data.length; i<length-1; i++) {
            k = i;
            for (j=i+1; j<length; j++) 
               if (data[j] > data[i])
                   k = j;
            if (i != k) {
                temp = data[i];
                data[i] = data[k];
                data[k] = temp;
            }
        }
        print_array (data);
    }

    int [] t_array (int n) {
        int mydata[] = new int [n];
        int i;
        for (i=0;i<n;i++) 
            mydata[i] = i*i;
        print_array (mydata);
        return mydata;
    }

    void cal () {
        int i,j,k,temp;

        for(i=0;i<21;i++) {
            for (j=0;j<34;j++) {
                k = 100 - i -j;
                if (i * 5 + j * 3 + k/3.0 == 100){
                    System.out.print ("公鸡 " + i );
                    System.out.print ("只;母鸡 " + j );
                    System.out.print ("只;小鸡 " + k);
                    System.out.println();
                }
            }
        }
        System.out.println();
    }
        
    void print_array (int data[]){
        for (int i=0;i<data.length;i++) 
            System.out.print(data[i] + " " );
        System.out.println();
    }

    void max_min_avg (int data[]) {
        int max,min,i;
        float avg;
        if (data.length == 0)
            return;
        max = data[0];
        min = data[0];
        avg = data[0];
        for (i=1;i<data.length;i++) {
            if (data[i] > max)
                max = data[i];
            if (data[i] < min)
                min = data[i];
            avg += data[i];
        }
        avg /= data.length;
        System.out.println("Max=" + max + "; Min=" + min + "; avg=" + avg);
    }

    void plusplus () {


    public static void main (String [] args) {
        int data[] = {4,2,1,3};
        b bb = new b();
        bb.t_switch();
        bb.t_for();
        bb.t_while();
        bb.t_type();
        bb.t_do();
        bb.mysort(data);
        bb.cal();
        bb.max_min_avg (data);
    }
}
