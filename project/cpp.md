# C++
### ตัวอย่าง code กรอกจำนวนกลุ่ม
    
```cpp

    int main() {
            Customer player;
            int i = 0;
            int price = 0; // เก็บราคาสุดท้าย
            int groupCount = 0; // เก็บจำนวนคนในกลุ่ม

            cout << "How many people in your group: ";
            cin >> groupCount;
```
![image](https://github.com/user-attachments/assets/52991e31-1d9d-4fb0-9682-98bcf253f5e4)


### ตัวอย่าง code หน้าเมนู
    
```cpp

            while (true) {
                player.showMenu();  // แสดงเมนู
                i = player.chooseMenu();  // รับคำสั่งจากผู้ใช้

                if (i == 1) {
                    player.showPackage();  // แสดงรายละเอียดแพ็คเกจ
                }
                else if (i == 2) {
                    player.getHigh();  // รับค่าความสูง
                    player.checkRule();  // ตรวจสอบกฎตามความสูง
                }
                else if (i == 3) {
                    int totalPackage = player.setPackage(groupCount);  // เพิ่มราคาของกลุ่ม
                    price += totalPackage;  // รวมราคา
                    cout << "Total Price: " << price << " baht" << endl;  // แสดงราคา
                }
                else if (i == 4) {
                    cout << "Total Price: " << price << " baht" << endl;  // แสดงราคาเมื่อเลือกจ่าย
                }
                else if (i == 0) {
                    break;  // ออกจากโปรแกรม
                }
            }

            return 0;
        }
```
![image](https://github.com/user-attachments/assets/9ccd92ff-d630-4967-8efc-ca5206ee1cb8)


### ตัวอย่าง code เช็คแพ็คเกจ
    
```cpp

void showPackage() {
        cout << "-------\nPackage\n-------\n#Extreme package# 300 baht\n-Roller Coaster\n-Raptor\n-Falcon\n-Viking\n" << endl;
        cout << "#Family package# 250 baht\n-Bouncing castle\n-Inflatable house\n-Swan boat\n" << endl;
        cout << "#Other package# 200 baht\n-Carousel and giant house\n\n#All you can play package# 400 baht\n-You can play anything you want in Khmerdogpark\n" << endl;
    }
```
![image](https://github.com/user-attachments/assets/56bc107c-a8f0-438c-abda-99e8afe392df)


### ตัวอย่าง code เช็คส่วนสูงตัวเองว่าสามารถเข้าเล่นเครื่องเล่นไหนได้บ้าง
    
```cpp

float getHigh() {
        cout << "------------------------\n#Tell me your height#\n------------------------" << endl;
        cout << "Enter your height: ";
        cin >> hight;
        return hight;
    }
class Rule : public Khmer_dog_park {
public:
    // ตรวจสอบส่วนสูงของผู้ใช้งาน
    void checkRule() {
        if (hight >= 131) {
            cout << "\nYou can play in #Extreme-zone# and #carousel and giant house#" << endl;
        } else {
            cout << "\nYou can play in #Family-zone# and #carousel and giant house#" << endl;
        }
    }
};
```
![image](https://github.com/user-attachments/assets/8af5e8af-92dd-4330-b355-89d24190d8c7)


### ตัวอย่าง code เช็คราคา
    
```cpp

 int setPackage(int a) {
        int pack = 0; // กำหนดค่าเริ่มต้นให้กับ pack
        while (true) {
            cout << "--------------\nChoose package\n--------------\n[1]Extreme package 300 baht\n[2]Family package 250 baht\n[3]Other package 200 baht\n[4]All you can play package 400 baht\n[0]Exit" << endl;
            cin >> ans;
            switch (ans) {
                case 1:
                    pack += 300; // เพิ่มค่า 300
                    break;
                case 2:
                    pack += 250; // เพิ่มค่า 250
                    break;
                case 3:
                    pack += 200; // เพิ่มค่า 200
                    break;
                case 4:
                    pack += 400; // เพิ่มค่า 400
                    break;
                case 0:
                    break; // ออกจากการเลือก package
            }
            a--;
            if (a == 0) {
                break; // ถ้าจำนวนคนครบแล้ว ให้หยุด
            }
        }
        return pack; // ส่งกลับราคาที่คำนวณได้
    }
 int totalPackage = player.setPackage(groupCount);  // เพิ่มราคาของกลุ่ม
            price += totalPackage;  // รวมราคา
            cout << "Total Price: " << price << " baht" << endl;  // แสดงราคา
```
![image](https://github.com/user-attachments/assets/981c2248-2e76-4df5-9b2a-b0b3e57a537a)


