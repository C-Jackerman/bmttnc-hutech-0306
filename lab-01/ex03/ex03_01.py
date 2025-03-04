def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

# Người dùng nhập danh sách số nguyên
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu phẩy: ").split(',')))

# Tính tổng các số chẵn
result = sum_even_numbers(numbers)

# In kết quả
print("Tổng các số chẵn trong danh sách là:", result)
