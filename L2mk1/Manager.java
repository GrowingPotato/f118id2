public class Manager extends Employee{
    private String department;

    public Manager(String name, int age, int salary, String department) {
        super(name, age, salary);
        this.department = department;
    }

    public void setDepartment(String department){
        this.department = department;
    }

    public String getDepartment(){
        return department;
    }

    @Override
    public void showInfo(){
        System.out.printf("Имя:%s\nДепартамент:%s\nВозраст:%s\nЗарплата:%s\n", this.getName(), this.department, this.getAge(), this.getSalary());
    }
    @Override   
    public void work(){
        System.out.printf("%s управляет", this.getName());
    }
}


