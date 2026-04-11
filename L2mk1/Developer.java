public class Developer extends Employee{
    private String programmingLanguage;
    public Developer(String name, int age, int salary, String programmingLanguage) {
        super(name, age, salary);
        this.programmingLanguage = programmingLanguage;
    }

    public void setProgrammingLanguage(String programmingLanguage){
        this.programmingLanguage = programmingLanguage;
    }

    public String getProgrammingLanguage(){
        return this.programmingLanguage;
    }

    @Override
    public void showInfo(){
        System.out.printf("Имя:%s\nЯзык программирования:%s\nВозраст:%s\nЗарплата:%s\n", this.getName(), this.getProgrammingLanguage(), this.getAge(), this.getSalary());
    }
    @Override   
    public void work(){
        System.out.printf("%s Программирует", this.getName());
    }
    

   
    
}
