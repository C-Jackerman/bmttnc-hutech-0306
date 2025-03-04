# Nhập danh sách từ người dùng, các phần tử cách nhau bởi dấu cách
words = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Tạo dictionary đếm số lần xuất hiện
count_dict = {}

for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1  # Tăng số lần xuất hiện

# In kết quả
print("Số lần xuất hiện của các phần tử:", count_dict)
