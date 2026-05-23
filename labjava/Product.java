

public class Product{
    private Integer id;
    private String name;
    private String category;
    private double price;
    private double rating;
    private Integer inStock;

    

    public Product(Integer id, String name, String category, double price, double rating, Integer inStock){
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
        this.rating = rating;
        this.inStock = inStock;
    }

    @Override
    public String toString() {
        return String.format("\n----------------------\nId: %d\nName: %s\nCategory: %s\nPrice: %.2f\nRating: %.2f\ninStock: %d\n----------------------\n", id, name, category, price, rating, inStock);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public Integer getInStock() {
        return inStock;
    }

    public void setInStock(Integer inStock) {
        this.inStock = inStock;
    }
}