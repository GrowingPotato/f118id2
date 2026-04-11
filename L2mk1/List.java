import java.util.ArrayList;
import java.util.NoSuchElementException;

public class List {
    private ArrayList<Employee> list = new ArrayList<>();
    

    public void addEmployee(String name, int age, int salary){
        Employee emp = new Employee(name, age, salary);
        list.add(emp);
    }

    public void addManager(String name, int age, int salary, String department){
        Manager emp = new Manager(name, age, salary, department);
        list.add(emp);
    }

    public void addDeveloper(String name, int age, int salary, String programmingLanguage){
        Developer emp = new Developer(name, age, salary, programmingLanguage);
        list.add(emp);
    }

    public void showEveryone(){
        for(int i = 0; i < list.size(); i++){
            list.get(i).showInfo();
        }
    }

    public Employee findByName(String name){
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).getName() == name){
                return list.get(i);
            }
        }
        throw new NoSuchElementException("Нет сотрудника с таким именем");
    }

    public void deleteByName(String name){
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).getName() == name){
                list.remove(i);
                System.out.printf("Все записи с именем %s удалены", name);
            }
        }
    }

    public void setSalary(String name, int newSalary){
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).getName() == name){
                list.get(i).setSalary(newSalary);
            }
        }
    }

    public void countEmployees(){
        int managerCount = 0;
        int developerCount = 0;

         for(int i = 0; i < list.size(); i++){
            if(list.get(i) instanceof Manager){
                managerCount++;
            }
            else if(list.get(i) instanceof Developer){
                developerCount++;
            }
        }
        System.out.printf("Всего %s сотрудников, из них:\n %s менеджеров\n%s девелоперов", managerCount+developerCount, managerCount, developerCount);
    }
}
