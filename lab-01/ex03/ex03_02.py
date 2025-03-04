# Nhập danh sách số từ người dùng, cách nhau bởi dấu ','
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu phẩy (,): ").split(',')))

# Đảo ngược danh sách
reversed_numbers = numbers[::-1]

# In kết quả
print("Danh sách sau khi đảo ngược:", reversed_numbers)
