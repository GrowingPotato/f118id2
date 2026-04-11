public class Cars {

    private int spotid;
    private char type;
    private int timein;

    public Cars(int spotid, char type, int timein){
        this.spotid = spotid;
        this.type = type;
        this.timein = timein;
    }

    public int getId(){
        return spotid;
    }

    public void setId(int id){
        this.spotid = id;
    }

    public char getType(){
        return type;
    }

    public void setType(char type){
            this.type = type;
        }

    public int getTime(){
        return timein;
    }

    public void setTime(int time){
        this.timein = time;

    }
    

}



