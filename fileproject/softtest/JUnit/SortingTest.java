import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SortingTest {

    private int[] TS01_Array;
    private int[] TS02_Array;
    private int[] TS03_Array;
    private int[] TS04_Array;
    private int[] TS05_Array;
    private int[] TS06_Array;
    private int[] TS07_Array;
    private int[] TS08_Array;

    @BeforeEach
    void setUp() {
        // กำหนดค่าให้กับอาเรย์ทดสอบแต่ละตัว
        TS01_Array = new int[]{1, 2, 3, 4, 5};  // ข้อมูลเรียงแล้ว n = 5
        TS02_Array = new int[]{5, 4, 3, 2, 1};  // ข้อมูลเรียงกลับ n = 5
        TS03_Array = new int[]{5, 1, 3, 2, 4};  // ข้อมูลไม่เรียง n = 5
        TS04_Array = new int[]{-1, 2, 3, -4, -5};  // ข้อมูลที่มีค่าติดลบ n = 5
        TS05_Array = new int[]{1};  // ข้อมูล 1 ตัว n = 1
        TS06_Array = new int[]{ };  // อาเรย์ว่าง n = 0
        TS07_Array = new int[]{1, 2, 3, 4, 5};  // ข้อมูลเรียงแล้ว n = 5
        TS08_Array = new int[]{1, 2, 3, 4, 5};  // ข้อมูลเรียงแล้ว n = 5
    }

    @Test
    void TS01() {
        // ทดสอบกับอาเรย์ที่เรียงลำดับแล้ว
        Sorting.bubbleSort(TS01_Array, 5 ); // n = 5
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, TS01_Array);
        Sorting.printArray(TS01_Array, 5);
    }
    
    @Test
    void TS02() {
        // ทดสอบกับอาเรย์ที่เรียงลำดับกลับด้าน
    	Sorting.bubbleSort(TS02_Array, 5 ); // n = 5
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, TS02_Array);
        Sorting.printArray(TS02_Array, 5);
    }

    @Test
    void TS03() {
        // ทดสอบกับอาเรย์ที่เรียงลำดับแบบไม่เรียง
    	Sorting.bubbleSort(TS03_Array, 5 ); // n = 5
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, TS03_Array);
        Sorting.printArray(TS03_Array, 5);
    }
    
    @Test
    void TS04() {
        // ทดสอบกับอาเรย์ที่มีค่าติดลบ
    	Sorting.bubbleSort(TS04_Array, 5 ); // n = 5
        assertArrayEquals(new int[]{-5, -4, -1, 2, 3}, TS04_Array);
        Sorting.printArray(TS04_Array, 5);
    }

    @Test
    void TS05() {
        // ทดสอบกับอาเรย์ที่มีข้อมูลเพียง 1 ค่า
    	Sorting.bubbleSort(TS05_Array, 1 ); // n = 1
        assertArrayEquals(new int[]{1}, TS05_Array);
        Sorting.printArray(TS05_Array, 1);
    }

    @Test
    void TS06() {
        // ทดสอบกับอาเรย์ที่ไม่มีข้อมูล (ว่าง)
    	Sorting.bubbleSort(TS06_Array, 0 ); // n = 0
        assertArrayEquals(new int[]{ }, TS06_Array);
        Sorting.printArray(TS06_Array, 0);
    }

    @Test
    void TS07() {
        // ทดสอบการส่งขนาดอาเรย์ที่ผิดพลาด (n = 6 แต่มีข้อมูลแค่ 5 ค่า)
    	Sorting.bubbleSort(TS07_Array, 6 ); // n = 6
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, TS07_Array);
        Sorting.printArray(TS07_Array, 6);
    }

    @Test
    void TS08() {
        // ทดสอบการส่งขนาดอาเรย์ที่ผิดพลาด (n = 4 แต่มีข้อมูล 5 ค่า)
    	Sorting.bubbleSort(TS08_Array, 4 ); // n = 4
        assertArrayEquals(new int[]{1, 2, 3, 4}, TS08_Array);
        Sorting.printArray(TS08_Array, 4);
    }

}
