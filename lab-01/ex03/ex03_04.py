# Nhập tuple từ người dùng theo định dạng (1,-2,3,4,-5)
user_input = input("Nhập một tuple (ví dụ: (1,-2,3,4,-5)): ")

# Loại bỏ dấu ngoặc tròn, sau đó tách các phần tử theo dấu ','
numbers = tuple(map(int, user_input.strip("()").split(',')))

# Lấy phần tử đầu tiên và cuối cùng
first_element = numbers[0]
last_element = numbers[-1]

# In kết quả
print("Tuple đã nhập:", numbers)
print("Phần tử đầu tiên:", first_element)
print("Phần tử cuối cùng:", last_element)
