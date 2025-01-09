package Bank;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class Account_Test {

    private Account account;

    // ตั้งค่าก่อนการทดสอบ
    @BeforeEach
    void setUp() {
        // สร้างบัญชีใหม่สำหรับการทดสอบ
        account = new Account("bob", "001", 1000.0);
    }

    // ทดสอบการทำงานของ getName()
    @Test
    void TSB006_TCB01() {
        assertEquals("bob", account.getName(), "ชื่อผู้ถือบัญชีควรเป็น 'bob'");
    }

    // ทดสอบการทำงานของ setName()
    @Test
    void TSB007_TCB01() {
        account.setName("jcop");
        assertEquals("jcop", account.getName(), "ชื่อผู้ถือบัญชีควรเป็น 'jcop' หลังจากตั้งค่าใหม่");
    }

    // ทดสอบการทำงานของ getAccountNumber()
    @Test
    void TSB008_TCB01() {
        assertEquals("001", account.getAccountNumber(), "หมายเลขบัญชีควรเป็น '001'");
    }

    // ทดสอบการทำงานของ setAccountNumber()
    @Test
    void TSB009_TCB01() {
        account.setAccountNumber("002");
        assertEquals("002", account.getAccountNumber(), "หมายเลขบัญชีควรเป็น '002' หลังจากตั้งค่าใหม่");
    }

    // ทดสอบการทำงานของ getBalance()
    @Test
    void TSB010_TCB01() {
        assertEquals(1000.0, account.getBalance(), 0.001, "ยอดคงเหลือควรเป็น 1000.0");
    }

    @Test
    void TSB011_TCB01() {
    	account.setBalance(2000.0);
        assertEquals(2000.0, account.getBalance(), 0.001, "ยอดคงเหลือควรเป็น 2000.0");
    }
    
    // ทดสอบการทำงานของ deposit()
    @Test
    void TSB012_TCB01() {
        account.deposit(500.0);
        assertEquals(1500.0, account.getBalance(), 0.001, "ยอดคงเหลือควรเป็น 1500.0 หลังจากฝากเงิน 500.0");
    }

    // ทดสอบการทำงานของ withdraw() ในกรณีปกติ
    @Test
    void TSB013_TCB01() {
        account.withdraw(500.0);
        assertEquals(500.0, account.getBalance(), 0.001, "ยอดคงเหลือควรเป็น 500.0 หลังจากถอนเงิน 500.0");
    }

    // ทดสอบการทำงานของ getAccountInfo()
    @Test
    void TSB014_TCB01() {
        String testInfo = "Name: bob, Account Number: 001, Balance: 1000.0";
        assertEquals(testInfo, account.getAccountInfo(), "ข้อมูลบัญชีควรถูกต้องตามข้อมูลที่ตั้งไว้");
    }
}
