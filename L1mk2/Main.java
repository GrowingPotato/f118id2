public class Main{
    public void main() {

    Parking Spotlist = new Parking();
    
    Spotlist.setbusy(0, 0, 'В', 15);
    
    Spotlist.setbusy(0, 4, 'Л', 25);

    int b;
    b = Spotlist.unpark(0, 0, 40);

    System.out.println(b);

    Spotlist.findfree();
    Spotlist.showparking();
    }
}
