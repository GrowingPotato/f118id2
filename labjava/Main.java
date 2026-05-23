import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Main{
    public static void main(String args[]){
    Product p1 = new Product(1, "Смартфон X", "Электроника", 75000.0, 4.8, 12);
    Product p2 = new Product(2, "Ноутбук Pro", "Электроника", 150000.0, 4.9, 5);
    Product p3 = new Product(3, "Кофемашина", "Дом", 25000.0, 4.2, 0);
    Product p4 = new Product(4, "Чайник", "Дом", 3500.0, 4.5, 20);
    Product p5 = new Product(5, "Кроссовки", "Спорт", 8000.0, 4.7, 15);
    Product p6 = new Product(6, "Коврик для йоги", "Спорт", 1500.0, 4.0, 0);
    Product p7 = new Product(7, "Блендер", "Дом", 5000.0, 3.8, 8);
    Product p8 = new Product(8, "Игровая мышь", "Электроника", 4500.0, 4.6, 50);
    Product p9 = new Product(9, "Рюкзак", "Аксессуары", 3000.0, 4.3, 30);
    Product p10 = new Product(10, "Умные часы", "Электроника", 18000.0, 4.1, 7);
    Product p11 = new Product(11, "Настольная лампа", "Дом", 2200.0, 4.4, 10);
    Product p12 = new Product(12, "Бутылка для воды", "Спорт", 800.0, 4.8, 100);
    Product p13 = new Product(13, "Наушники", "Электроника", 12000.0, 4.5, 0);
    Product p14 = new Product(14, "Зимняя куртка", "Одежда", 15000.0, 4.7, 3);
    Product p15 = new Product(15, "Солнцезащитные очки", "Аксессуары", 5000.0, 3.9, 10);
    Product p16 = new Product(16, "Гантели 5кг", "Спорт", 2400.0, 4.9, 4);
    Product p17 = new Product(17, "Монитор 4K", "Электроника", 35000.0, 4.6, 6);
    Product p18 = new Product(18, "Пылесос", "Дом", 13000.0, 4.0, 2);
    Product p19 = new Product(19, "Толстовка", "Одежда", 4500.0, 4.5, 25);
    Product p20 = new Product(20, "Клавиатура", "Электроника", 6000.0, 4.3, 0);
    List<Product> products = Arrays.asList(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20);

    products.stream()
        .filter(p -> p.getPrice() > 500)
        .forEach(System.out::println);
        
    products.stream()
        .filter(p -> p.getName().equals("name") )
        .forEach(System.out::println);

    products.stream()
        .filter(p -> p.getInStock() == 0)
        .forEach(p -> System.out.println(p.getName()));

    products.stream()
        .map(Product::getPrice).sorted()
        .forEach(System.out::println);

    products.stream()
        .map(Product::getRating).sorted(Comparator.reverseOrder())
        .forEach(System.out::println);

    List<String> names = products.stream()
        .map(Product::getName)
        .collect(Collectors.toList());
    System.out.println(names.get(3));

    double averageprices  =
        products.stream()
            .mapToDouble(Product::getPrice) 
            .average()
            .orElse(0.0);
    System.out.println(averageprices);


    products.stream()
        .sorted(Comparator.comparing(Product::getPrice).reversed())
        .findFirst()
        .ifPresent(System.out::println);
    
    long count = products.stream()
    .filter(p -> p.getRating() > 4.5)
    .count();
    System.out.println(count);

    boolean existance =
    products.stream()
    .anyMatch(p -> p.getInStock() == 0);
    if (existance == true){
        System.out.println("На складе отсутствует минимум 1 товар");
    }
    else{
        System.out.println("На складе присутствуют все товары");
    }
    
    

    List<Product> tasklist = products.stream()
    .filter(p -> p.getPrice() > 1000)
    .filter(p -> p.getRating() >= 4.0)
    .filter(p -> p.getInStock() > 0)
    .collect(Collectors.toList());
    
    System.out.println(tasklist);

    Map<String, List<Product>> categoryfiltered = products.stream()
    .collect(Collectors.groupingBy(Product::getCategory));
    System.out.println(categoryfiltered);

    List<Product> topthree = products.stream()
    .sorted(Comparator.comparing(Product::getPrice).reversed())
    .limit(3)
    .collect(Collectors.toList());

    System.out.println(topthree);
 }
    

}
