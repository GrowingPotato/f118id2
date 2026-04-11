public class Employee {
    private String name;
    private int age;
    private int salary;

    public Employee(String name, int age, int salary){
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public void showInfo(){
        System.out.printf("Имя:%s\nВозраст:%s\nЗарплата:%s\n", this.name, this.age, this.salary);
    }

    public void work(){
        System.out.printf("%s работает", this.name);
    }

    public String getName(){
        return name;
    }
    
    public void setName(String name){
        if (this.name != ""){
            this.name = name;
        }
        else{
            System.out.println("Имя не может быть пустым.");
        }
    }

    public int getAge(){
        return age;
    }
    
    public void setAge(int age){
        if (age > 17){
            this.age = age;
        }
        else{
            System.out.println("Возраст не может быть меньше 18.");
        }
    }

    public int getSalary(){
        return salary;
    }

    public void setSalary(int salary){
        if (salary > 86200){
        this.salary = salary;
        }
        else{
            System.out.println("Зарплата не может быть меньше 0.");
        }
    }
}
