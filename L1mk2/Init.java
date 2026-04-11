public class Init{

    public static int levelcount = GlobalVars.LEVELCOUNT;
    public static int spotsperlevel = GlobalVars.SPOTSPERLEVEL;
    public static Cars[][] init(){
    Cars[][] SpotsList;
    SpotsList = new Cars[GlobalVars.LEVELCOUNT][GlobalVars.SPOTSPERLEVEL];
    for(int i = 0; i < GlobalVars.LEVELCOUNT; i++){
        for(int k = 0; k < GlobalVars.SPOTSPERLEVEL; k++){
            Cars car = new Cars(i*GlobalVars.LEVELCOUNT+GlobalVars.SPOTSPERLEVEL, '.', 0);
            SpotsList[i][k] = car;
        }
    }
    return SpotsList;
}
}