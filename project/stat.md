#R
### ตัวอย่างการใช้ภาษา R ในการสร้างกราฟต่างและคำนวณ
[https://www.canva.com/design/DAFcU4AWUuA/kygtg952lpTN1s9_Zli-xA/edit?utm_content=DAFcU4AWUuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFcU4AWUuA/kygtg952lpTN1s9_Zli-xA/edit?utm_content=DAFcU4AWUuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

![image](https://github.com/user-attachments/assets/22554bbb-f22f-4a68-becc-f62e7b783618)
![image](https://github.com/user-attachments/assets/206d77cb-5e02-481b-8cd0-9b038cd1e101)

### ตัวอย่าง code ภาษา R

```R
#T-Test
result <- t.test(data_read,data_work,var.equal = TRUE)
cat("# T-test results : ")
cat("Sample sizes: ", result$parameter, "\n")
cat("T-statistic: ", result$statistic, "\n")
cat("P-value: ", result$p.value, "\n")

# Correlation between Read & Work Data
corr_read_work = cor(data_read,data_work)
sprintf("Correlation between Read & Work Data : %f",corr_read_work)

# Margin of error of Read Data
confidence_level <- 0.95
z <- qnorm(1 - (1 - confidence_level)/2)
margin_error <- z * (sd_read / sqrt(length_read))
sprintf("Margin of error Read Data : %f",margin_error)

# Simple Linear Regression
linear_regression = lm(data_read ~ data_work)
coeffs = coefficients(linear_regression)
summary(linear_regression)
sprintf("Correlation between groups >> %f",corr_read_work)
sprintf("Simple regression equation >> %f",coeffs)
sprintf("Coefficient of decision is %f",summary(linear_regression)$r.squared)

hist(data_read)
```
