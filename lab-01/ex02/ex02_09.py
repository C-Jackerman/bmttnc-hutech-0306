def kiem_tra_SNT(n):
    if n<1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_SNT(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "Không phải là số nguyên tố.")