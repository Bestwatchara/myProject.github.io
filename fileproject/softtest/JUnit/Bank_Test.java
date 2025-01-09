package Bank;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;

class Bank_Test {

    private Bank bank;
    private Account account1;
    private Account account2;

    // ตั้งค่าก่อนการทดสอบ
    @BeforeEach
    void setUp() {
        bank = new Bank();  // สร้าง Bank ใหม่สำหรับการทดสอบ
        account1 = new Account("bob", "001", 1000.0);  // สร้างบัญชีแรก
        account2 = new Account("jcop", "002", 2000.0);  // สร้างบัญชีที่สอง
    }

    // ทดสอบการเพิ่มบัญชีใน Bank
    @Test
    void TSB001_TCB01() {
        bank.addAccount(account1);
        ArrayList<Account> accounts = bank.getAccounts();
        assertTrue(accounts.contains(account1), "บัญชีควรถูกเพิ่มในรายการบัญชี");
    }
    @Test
    void TSB001_TCB02() {
        bank.addAccount(account1);
        bank.addAccount(account1);
        ArrayList<Account> accounts = bank.getAccounts();
        assertTrue(accounts.contains(account1), "บัญชีควรถูกเพิ่มในรายการบัญชี");
        assertEquals(1, accounts.size(), "ควรมีบัญชีแค่หนึ่งบัญชีในรายการบัญชี");
    }

    // ทดสอบการลบบัญชีใน Bank
    @Test
    void TSB002_TCB01() {
        bank.addAccount(account1);
        bank.removeAccount(account1);
        ArrayList<Account> accounts = bank.getAccounts();
        assertFalse(accounts.contains(account1), "บัญชีควรถูกลบออกจากรายการบัญชี");
        assertEquals(0, accounts.size(), "ไม่มีบัญชีเหลืออยู่ในรายการบัญชี");
    }
    
    @Test
    void TSB002_TCB02() {
        bank.removeAccount(account2);
        ArrayList<Account> accounts = bank.getAccounts();
        assertFalse(accounts.contains(account1), "บัญชีควรถูกลบออกจากรายการบัญชี");
        assertEquals(0, accounts.size(), "ไม่มีบัญชีเหลืออยู่ในรายการบัญชี");
    }

    // ทดสอบการฝากเงินเข้าบัญชี
    @Test
    void TSB003_TCB01() {
        bank.addAccount(account1);
        bank.depositMoney(account1, 1000.0);
        assertEquals(2000.0, account1.getBalance(), 0.001, "ยอดคงเหลือควรเพิ่มขึ้นหลังจากการฝากเงิน");
    }
    
    @Test
    void TSB003_TCB02() {
        bank.addAccount(account1);
        bank.depositMoney(account1, 0.0);
        assertEquals(1000.0, account1.getBalance(), 0.001, "ยอดคงเหลือเท่าเดิมหลังจากการฝากเงิน");
    }
    
    @Test
    void TSB003_TCB03() {
        bank.addAccount(account1);
        bank.depositMoney(account1, -1000.0);
        assertEquals(1000.0, account1.getBalance(), 0.001, "ไม่ควรฝากเงินจำนวนติดลบได้");
    }

    // ทดสอบการถอนเงินจากบัญชี
    @Test
    void TSB004_TCB01() {
        bank.addAccount(account1);
        bank.withdrawMoney(account1, 1000.0);
        assertEquals(0.0, account1.getBalance(), 0.001, "ยอดคงเหลือควรลดลงหลังจากการถอนเงิน");
    }
    @Test
    void TSB004_TCB02() {
        bank.addAccount(account1);
        bank.withdrawMoney(account1, 0.0);
        assertEquals(1000.0, account1.getBalance(), 0.001, "ยอดเงินคงเหลือเท่าเดิมหลังจากการถอนเงิน");
    }
    @Test
    void TSB004_TCB03() {
        bank.addAccount(account1);
        bank.withdrawMoney(account1, 2000.0);
        assertEquals(1000.0, account1.getBalance(), 0.001, "ไม่ควรถอนเงินเกินยอดคงเหลือในบัญชี");
    }
    
    // ทดสอบการดูรายการบัญชีทั้งหมด
    @Test
    void TSB005_TCB01ounts() {
        bank.addAccount(account1);
        bank.addAccount(account2);
        ArrayList<Account> accounts = bank.getAccounts();
        assertEquals(2, accounts.size(), "ควรมีบัญชีสองบัญชีในรายการบัญชี");
        assertTrue(accounts.contains(account1), "ควรมีบัญชี 'account1' ในรายการบัญชี");
        assertTrue(accounts.contains(account2), "ควรมีบัญชี 'account2' ในรายการบัญชี");
    }
    @Test
    void TSB005_TCB02() {
        ArrayList<Account> accounts = bank.getAccounts();
        assertEquals(0, accounts.size(), "ควรมีบัญชีสองบัญชีในรายการบัญชี");
    }
}

