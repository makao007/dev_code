public class hello extends Person{
    public hello (String a,int b){
        super(a,b);
    }
    public String toString (){
        return "class hello";
    }
    
    public static void main (String [] args)
    {
        Person h1 = new hello("mkw",24);
        Person h2 = new Person("mkw",24);

        System.out.println(h1.toString());
        System.out.println(h2.toString());
    }
}

class Person {
    private String name;
    private int age;
    public void setName (String newName) {
        name = newName;
    }
    public void setAge  (int newAge) {
        age  = newAge;
    }
    public String getName () {
        return name;
    }
    public int  getAge () {
        return age;
    }
    public Person () {
        age = 0;
        name = "";
    }
    public Person (String newName,int newAge ) {
        name = newName;
        age  = newAge;
    }
    public String toString (){
        return ("Name: " + name + "; Age: " + age);
    }

}

