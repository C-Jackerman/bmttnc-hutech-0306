# Nhập danh sách từ người dùng, các phần tử cách nhau bởi dấu cách
words = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Tạo dictionary đếm số lần xuất hiện
count_dict = {}

for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1  # Tăng số lần xuất hiện

# Hiển thị dictionary trước khi xóa
print("Dictionary ban đầu:", count_dict)

# Nhập key cần xóa
key_to_delete = input("Nhập key cần xóa: ")

# Xóa key nếu nó tồn tại trong dictionary
if key_to_delete in count_dict:
    del count_dict[key_to_delete]
    print("Dictionary sau khi xóa:", count_dict)
else:
    print("Key không tồn tại trong dictionary.")
