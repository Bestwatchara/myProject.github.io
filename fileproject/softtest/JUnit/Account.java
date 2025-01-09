package Bank;

public class Account {
    private String name;
    private String accountNumber;
    private double balance;

    // Constructor
    public Account(String name, String accountNumber, double balance) {
        // Set the variables
        this.name = name;
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    // Method to retrieve the name of the account holder
    public String getName() {
        return name;
    }

    // Method to set the name of the account holder
    public void setName(String name) {
        this.name = name;
    }

    // Method to retrieve the account number
    public String getAccountNumber() {
        return accountNumber;
    }

    // Method to set the account number
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    // Method to retrieve the balance of the account
    public double getBalance() {
        return balance;
    }

    // Method to set the balance of the account
    public void setBalance(double balance) {
        this.balance = balance;
    }

    // Method to deposit a specified amount into the account
    public void deposit(double amount) {
        balance += amount;
    }

    // Method to withdraw a specified amount from the account
    public void withdraw(double amount) {
        balance -= amount;
    }

    // Method to retrieve the account information
    public String getAccountInfo() {
        return "Name: " + name + ", Account Number: " + accountNumber + ", Balance: " + balance;
    }
}
