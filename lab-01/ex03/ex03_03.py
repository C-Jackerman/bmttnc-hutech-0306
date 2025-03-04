# Nhập danh sách số từ người dùng, cách nhau bởi dấu ','
numbers = tuple(map(int, input("Nhập các số, cách nhau bởi dấu phẩy (,): ").split(',')))

# In kết quả
print("Tuple được tạo:", numbers)
