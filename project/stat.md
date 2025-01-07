### ตัวอย่างการใช้ภาษา R ในการสร้างกราฟต่างและคำนวณ
[https://www.canva.com/design/DAFcU4AWUuA/kygtg952lpTN1s9_Zli-xA/edit?utm_content=DAFcU4AWUuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFcU4AWUuA/kygtg952lpTN1s9_Zli-xA/edit?utm_content=DAFcU4AWUuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

![image](https://github.com/user-attachments/assets/22554bbb-f22f-4a68-becc-f62e7b783618)
![image](https://github.com/user-attachments/assets/206d77cb-5e02-481b-8cd0-9b038cd1e101)

### ตัวอย่าง code ภาษา R

```R
    # all data collect from Google form 103 response
dataform <- read.csv("dataform.csv")
dataform

data_read <- dataform$read
data_read

length_read = length(data_read)
mean_read = mean(data_read)
sd_read = sd(data_read)
median_read = median(data_read)
sderr_read = sd_read/length_read
var_read = var(data_read)
range_read = max(data_read)-min(data_read)


sprintf("Amount of read data is %d",length_read)
sprintf("Mean of reaed data is %f",mean_read)
sprintf("Standard diviaion of read data is %.4f",sd_read)
sprintf("Median of read data is %.4f",median_read)
sprintf("Standard Error of read data is %f",sderr_read)
sprintf("Variance of read data is %f",var_read)
sprintf("Range of read data is %f",range_read)

#-------------------------------------------#
```
