# Bài 1
integer_number = 10
float_number = 9.637
string_text = "Hello everyone!"
print("Số nguyên",integer_number)
print("Số thực",float_number)
print("Chuỗi",string_text)
# Bài 2
PI = 3.14
r = 5
chuvi = 2 * PI * r
print("Chu vi hình tròn là :",chuvi)
# Bài 3
a = int(input("Số nguyên thứ nhất:"))
b = int(input("Số ngyên thứ hai:"))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
print("Tổng:",tong)
print("Hiệu:",hieu)
print("Tích:",tich)
print("Thương:",thuong)
# Bài 4
def sun_two_numbers(a,b):
    return a+b
number1 = int(input("Nhập số nguyên thứ nhất:"))
number2 = int(input("Nhập số nguyên thứ hai:"))
ketqua = sun_two_numbers(number1,number2)
print("Tổng hai số nguyên:",ketqua)
# Bài 5
name = "Linh"
age = 18
average_score = 9,5
age_next_year = age + 1
doubled_score = average_score * 2
print("name",type(name))
print("age",type(age))
print("average_score",type(average_score))
print("age next year",age_next_year)
print("doubled_score",doubled_score)
# Bài 6
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("Nhập một số nguyên:"))
print(is_even(n))
# Bài 7
a = int(input("Nhập số nguyên thứ nhất:"))
b = int(input("Nhập số nguyên thứ hai:"))
c = int(input("Nhập số nguyên thứ ba:"))
max_number = max(a,b,c)
print("Số lớn nhất là:",max_number)
# Bài 8
def greet( name ="student"):
    print("Hello",name + "!")
greet()
greet("Linh")
# Bài 9
age = int(input("Nhập tuổi:"))
if age >= 1 and age <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")
# Bài 10
s = input("Nhập một chuổi:")
count = s.count("a")
print("Số lần chữ 'a' xuất hiện là :",count)
# Bài 11
C = float(input("Nhập nhiệt độ theo độ C:"))
F = C * 9 / 5 + 32
print("Nhiệt độ theo độ F là:",F)
# Bài 12
weight = float(input("Nhập cân nặng(kg):"))
height = float(input("Nhập chiều cao(m):"))
BMI = weight / (height * height)
print("BMI của cơ thể là:",round (BMI,2))
# Bài 13
a = int(input("Nhập số chia nguyên thứ nhất:"))
b = int(input("nhập số chia nguyên thứ hai:"))
if b == 0:
    print("Lỗi : Không thể chia cho 0")
else:
    result = a / b
    print("Kết quả phép chia là:",result)
# Bài 14
number = float(input("Nhập một số :"))
if number < 0:
    print("Lỗi, không thể tính căn bậc hai của số âm")
else:
    square_root = number ** 0.5
    print("Căn bậc hai của số là:",square_root)
# Bài 15
for i in range(1, 4):
    print("Sinh viên",i)
    name = input("Nhập tên sinh viên:")
    math = float(input("Nhập điểm toán:"))
    physics = float(input("Nhập điểm lý:"))
    chemsitry = float(input("Nhập điểm hóa:"))
    average =(math + physics + chemsitry)/3
    print("Tên học sinh:",name)
    print("Điểm trung bình của ba môn:",average)
    print("--------------------------")
































