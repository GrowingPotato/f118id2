public class Main{
    public static void main(){
        List List = new List();
        List.addDeveloper("nikita buyanow", 30, 99999, "python");
        List.findByName("nikita buyanow").showInfo();
    }
}