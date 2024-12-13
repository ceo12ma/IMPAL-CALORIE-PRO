// Kelas untuk menyimpan data produk
class Product {
    private String id;
    private String name;
    private double price;
    
    public Product(String id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
    
    // Getter methods
    public String getId() { return id; }
    public String getName() { return name; }
    public double getPrice() { return price; }
}

// Kelas untuk detail order
class OrderDetail {
    private Product product;
    private int quantity;
    private double subtotal;
    
    public OrderDetail(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
        this.subtotal = calculateSubTotal();
    }
    
    public double calculateSubTotal() {
        return product.getPrice() * quantity;
    }
    
    // Getter methods
    public Product getProduct() { return product; }
    public int getQuantity() { return quantity; }
    public double getSubtotal() { return subtotal; }
}

// Kelas utama untuk order
class Order {
    private String orderId;
    private List<OrderDetail> orderDetails;
    private double totalAmount;
    private Printer printer;
    
    public Order() {
        this.orderId = generateOrderId();
        this.orderDetails = new ArrayList<>();
        this.printer = new Printer();
    }
    
    private String generateOrderId() {
        // Generate unique order ID
        return "ORD-" + System.currentTimeMillis();
    }
    
    public void addItem(Product product, int quantity) {
        OrderDetail detail = new OrderDetail(product, quantity);
        orderDetails.add(detail);
        calculateTotal();
    }
    
    private void calculateTotal() {
        totalAmount = orderDetails.stream()
                     .mapToDouble(OrderDetail::getSubtotal)
                     .sum();
    }
    
    public void printOrder() {
        printer.printOrderDetails(this);
    }
    
    // Getter methods
    public String getOrderId() { return orderId; }
    public List<OrderDetail> getOrderDetails() { return orderDetails; }
    public double getTotalAmount() { return totalAmount; }
}

// Kelas untuk menangani print
class Printer {
    public void printOrderDetails(Order order) {
        System.out.println("\n=== ORDER RECEIPT ===");
        System.out.println("Order ID: " + order.getOrderId());
        System.out.println("------------------------");
        
        for (OrderDetail detail : order.getOrderDetails()) {
            System.out.printf("%s x%d\n", 
                detail.getProduct().getName(),
                detail.getQuantity());
            System.out.printf("Subtotal: $%.2f\n", 
                detail.getSubtotal());
            System.out.println("------------------------");
        }
        
        System.out.printf("TOTAL: $%.2f\n", order.getTotalAmount());
        System.out.println("=== Thank You ===\n");
    }
}

// Contoh penggunaan
public class POSSystem {
    public static void main(String[] args) {
        // Buat beberapa produk
        Product p1 = new Product("P001", "Keyboard", 50.0);
        Product p2 = new Product("P002", "Mouse", 25.0);
        
        // Buat order baru
        Order order = new Order();
        
        // Tambah item ke order
        order.addItem(p1, 2);  // 2 keyboard
        order.addItem(p2, 3);  // 3 mouse
        
        // Print receipt
        order.printOrder();
    }
}