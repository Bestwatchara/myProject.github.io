#include <iostream>
using namespace std;

class Khmer_dog_park{
    public:
        int package,point,i,ans;
        float hight;
        void showMenu(){
            cout << "-----------\n   Menu\n-----------\n[1]package detail\n[2]check hight\n[3]choose package\n[4]pay\n[0]Exit" << endl;
        }
        int setPackage(int a)
        {   
            int pack;
            while(true){
                cout << "--------------\nchoose package\n--------------\n[1]Extream package 300 baht\n[2]Family package 250 baht\n[3]Other package 200 baht\n[4]All you can play package 400 baht\n[0]Exit" << endl;
                cin >> ans ;
                switch (ans)
                {
                    case 1:
                        pack = pack + 300;
                    case 2 :
                        pack = pack + 250;
                    case 3 :
                        pack = pack + 200;
                    case 4 :
                        pack = pack + 400;
                    case 0 :
                        break;
                }
                a--;
                if(a==0){
                    break;
                }
            }
            return pack;
        };
        //แสดง package และ ราคา
        float getHigh(){
            cout << "------------------------\n#Tell me your hight#\n------------------------" << endl;
            cout << "Enter your hight :";
            cin >> hight;
            return hight;
        }//รับค่าความสูง
        int showPackage(){
            cout << "-------\npackage\n-------\n#Extream package# 300 baht#\n-Roller Coaster\n-Raptor\n-Falcon\n-Viking\n" << endl;
            cout << "#Family package# 250 baht#\n-bouncing castle\n-inflatable house\n-swan boat\n" << endl;
            cout << "#Other package# 200 baht#\n-carousel and giant house\n\n#All you can play package# 400 baht#\n-you can play anything you want in Khmerdogpark\n" << endl;
            
            // return 0;
        }//แสดงรายละเอียดของ packageทั้งหมด
        Khmer_dog_park();
};
Khmer_dog_park::Khmer_dog_park(){
    cout << "\n------------------------\nWelcome to Khmerdogpark\n------------------------" << endl;
    i=0;
}
class Rule:public Khmer_dog_park{
    public:
        void checkRule(){
            if (hight>=131){
                cout << "\nyou can play #Extream-zone# #carousel and giant house#" << endl;
            }else{
                cout << "\nyou can play #Family-zone# #carousel and giant house#" << endl;
            }
        }//ตรวจสอบส่วนสูงของผู้ใช้งาน
};
class customer:public Rule{
    public:
       int chooseMenu(){
            cout << "choose : ";
            cin >> i;
            return i;
       }
};
int main()
{
    customer player;
    Khmer_dog_park money;
    int i=0;
    int price;
    /*r1.showPackage();
    r1.getHigh();
    r1.checkRule();
    r1.setPackage();*/
    cout << "How many poeple in your group : " << endl;
    cin >> price;
    while(true)
    {
        player.showMenu();
        i = player.chooseMenu();
        if (i==1){
            i = player.showPackage();
        }
        if (i==2){
            player.getHigh();
            player.checkRule();
        }
        if (i==3){
            price = player.setPackage(price);
            cout << "PRICE : " << price << endl;
        }
        if (i==4){
            cout << "Price : " << price << "bath :" << endl;
        }
        if (i==0){
            break;
        }
        
    };
    
    
}