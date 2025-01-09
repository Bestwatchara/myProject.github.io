package Bank;

import java.util.ArrayList;

public class Bank {
	
	// Declare an ArrayList to store Account objects
	private ArrayList<Account> accounts;
	
	// Constructor
	public Bank() {
		accounts = new ArrayList<Account>();
	}
	
	// Method to add an Account to the accounts list
	public void addAccount(Account account) {
		accounts.add(account);
	}
	
	// Method to remove an Account from the accounts list
	public void removeAccount(Account account) {
		accounts.remove(account);
	}
	
	// Method to deposit money into a specific Account
	public void depositMoney(Account account, double amount) {
		account.deposit(amount);
	}
	
	// Method to withdraw money from a specific Account
	public void withdrawMoney(Account account, double amount) {
		account.withdraw(amount);
	}
	
	// Method to get the list of all accounts
	public ArrayList<Account> getAccounts() {
		return accounts;
}
} 
