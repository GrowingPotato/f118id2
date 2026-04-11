public class Parking {

    private Cars[][] SpotsList;
    public Parking(){
    this.SpotsList = new Cars[GlobalVars.LEVELCOUNT][GlobalVars.SPOTSPERLEVEL];
    for(int i = 0; i < GlobalVars.LEVELCOUNT; i++){
        for(int k = 0; k < GlobalVars.SPOTSPERLEVEL; k++){
            Cars car = new Cars(i*GlobalVars.LEVELCOUNT+GlobalVars.SPOTSPERLEVEL, '.', 0);
            SpotsList[i][k] = car;
        }
    }
}



    public void showparking(){
        System.out.println();
    for(int l = 0; l < GlobalVars.LEVELCOUNT; l++){
        for (int k = 0; k < GlobalVars.SPOTSPERLEVEL; k++){
            System.out.printf("%s", this.SpotsList[l][k].getType());
        }
        System.out.println();
        
        }
    }


    public void findfree(){
        loop:
        for(int l = 0; l < GlobalVars.LEVELCOUNT; l++){
            for (int k = 0; k < GlobalVars.SPOTSPERLEVEL; k++){
                if(this.SpotsList[l][k].getType() == '.'){
                    System.out.printf("\n Место %d на уровне %d свободно", k, l);
                    break loop;
                }
            }
        }
        
    }

    public void park(int level, int spot,  char type, int timein){
        this.SpotsList[level][spot].setType(type);
        this.SpotsList[level][spot].setTime(timein);
    }

    public int unpark(int level, int spot, int timeout){
        int timedelta = timeout - this.SpotsList[level][spot].getTime();
        int price = 0;
        if (this.SpotsList[level][spot].getType() == 'В'){
            price = timedelta * Tariffs.SUV;
        }
        else if (this.SpotsList[level][spot].getType() == 'М'){
            price = timedelta * Tariffs.MOTO;
        }
        else if (this.SpotsList[level][spot].getType() == 'Л'){
            price = timedelta * Tariffs.LIGHT;
        }
        return price;
    }

    public void setfree(int level, int spot){
        this.SpotsList[level][spot].setTime(0);
        this.SpotsList[level][spot].setType('.');
    }

    public void setbusy(int level, int spot, char type, int timein){
        this.SpotsList[level][spot].setTime(timein);
        this.SpotsList[level][spot].setType(type);
    }
}
