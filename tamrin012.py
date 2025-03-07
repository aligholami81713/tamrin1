def square_numbers_before(n):
    for i in range(n):
        print(f"{i}^2 = {i**2}")

# دریات ورودی از کاربر
num = int(input("یک عدد وارد کنید: "))
square_numbers_before(num)

