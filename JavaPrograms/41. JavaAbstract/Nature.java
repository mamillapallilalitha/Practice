abstract class Nature{
    public abstract void Forest();
    public void view() {
       System.out.println("beautiful");
    }
    public void SayHi(){
        System.out.println("hellow");
    }
}
class Trees extends Nature {
    public void Forest() {
        System.out.println("trees are soo tall");
    }
}
class Birds extends Trees {
    public void Forest() {
        System.out.println("birds look colourful");
    }
}
class Main {
    public static void main(String[] args) {
        Trees myTrees = new Trees();
        myTrees.view();
        myTrees.Forest();
        Birds myBirds = new Birds();
        myBirds.view();
        myBirds.Forest();
        myBirds.SayHi();
    }
}




