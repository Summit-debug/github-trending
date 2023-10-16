import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Fruit {
    String name;
    double pricePerKg;
    int quantity;

    public Fruit(String name, double pricePerKg, int quantity) {
        this.name = name;
        this.pricePerKg = pricePerKg;
        this.quantity = quantity;
    }

    public double calculatePrice(double weight) {
        return weight * pricePerKg;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Price per kg: $" + pricePerKg);
        System.out.println("Quantity available: " + quantity);
    }
}

class Customer {
    private List<Fruit> cart;
    private double totalCost;

    public Customer() {
        cart = new ArrayList<>();
        totalCost = 0.0;
    }

    public void selectAndBuyFruits(List<Fruit> fruitList) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Fruit Shop!");
        System.out.println("Here are the available fruits:");

        while (true) {
            System.out.println("\nFruit List:");
            for (int i = 0; i < fruitList.size(); i++) {
                System.out.println((i + 1) + ". " + fruitList.get(i).name);
            }
            System.out.println((fruitList.size() + 1) + ". Finish shopping");

            System.out.print("Enter the number of the fruit you want to buy or "
                    + (fruitList.size() + 1) + " to finish: ");
            int selection = scanner.nextInt();

            if (selection >= 1 && selection <= fruitList.size()) {
                Fruit selectedFruit = fruitList.get(selection - 1);

                selectedFruit.displayInfo();
                System.out.print("Enter the weight (in kg) you want to buy: ");
                double weight = scanner.nextDouble();

                if (weight > 0) {
                    if (weight <= selectedFruit.quantity) {
                        double cost = selectedFruit.calculatePrice(weight);
                        totalCost += cost;
                        selectedFruit.quantity -= (int) weight;

                        cart.add(new Fruit(selectedFruit.name, selectedFruit.pricePerKg, (int) weight));
                        System.out.println("Added " + weight + " kg of " + selectedFruit.name + " to your cart.");
                        System.out.println("Subtotal: $" + totalCost);
                    } else {
                        System.out.println("Insufficient quantity available.");
                    }
                } else {
                    System.out.println("Invalid weight. Please select a valid weight.");
                }
            } else if (selection == fruitList.size() + 1) {
                break;
            } else {
                System.out.println("Invalid selection. Please enter a valid number.");
            }
        }

        System.out.println("Your cart contains:");
        for (Fruit item : cart) {
            System.out.println(item.name + " - " + item.quantity + " kg");
        }
        System.out.println("Total Cost: $" + totalCost);
        System.out.println("\n\t\tThank you for shopping at the Fruit Shop!\n\n\n");
    }
}

public class FruitShop2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Create a list of available fruits
        List<Fruit> fruitList = new ArrayList<>();
        fruitList.add(new Fruit("Apple", 2.5, 100));
        fruitList.add(new Fruit("Banana", 1.5, 150));
        fruitList.add(new Fruit("Orange", 3.0, 80));

        System.out.print("Enter the number of customers: \n");
        int numCustomers = scanner.nextInt();

        List<Customer> customers = new ArrayList<>();

        for (int i = 1; i <= numCustomers; i++) {
            Customer customer = new Customer();
            customers.add(customer);
            customer.selectAndBuyFruits(fruitList);
        }

        System.out.println("\n\n\t\tAll customers have finished shopping. Thank you for visiting the Fruit Shop!");
        scanner.close();
    }
}
