// product class
public class Product implements IDedObject {

    // private variables
    private int productID;
    private String productName;
    private String supplierName;

    // empty constructor
    public Product() {
        productID = 0;
        productName = "";
        supplierName = "";
    }

    // constructor with parameters
    public Product(int productID, String productName, String supplierName) {
        this.productID = productID;
        this.productName = productName;
        this.supplierName = supplierName;
    }

    // returns the ID
    public int getID() {
        return productID;
    }

    // prints all the info
    public void printID() {
        System.out.println(productID);
        System.out.println(productName);
        System.out.println(supplierName);
    }

    // getters
    public int getProductID() {
        return productID;
    }

    public String getProductName() {
        return productName;
    }

    public String getSupplierName() {
        return supplierName;
    }

    // setters
    public void setProductID(int productID) {
        this.productID = productID;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public void setSupplierName(String supplierName) {
        this.supplierName = supplierName;
    }
}
