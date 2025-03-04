class Student:
    student_id_counter = 1
    
    def __init__(self, name, gender, major, gpa):
        self.id = Student.student_id_counter
        Student.student_id_counter += 1
        self.name = name
        self.gender = gender
        self.major = major
        self.gpa = gpa
    
    def get_academic_performance(self):
        if self.gpa >= 8:
            return "Giỏi"
        elif self.gpa >= 6.5:
            return "Khá"
        elif self.gpa >= 5:
            return "Trung bình"
        else:
            return "Yếu"
    
    def __str__(self):
        return f"ID: {self.id} | Tên: {self.name} | Giới tính: {self.gender} | Chuyên ngành: {self.major} | GPA: {self.gpa} | Học lực: {self.get_academic_performance()}"

class StudentManagement:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, gender, major, gpa):
        student = Student(name, gender, major, gpa)
        self.students.append(student)
        print("\nSinh viên đã được thêm thành công!")
    
    def update_student(self, student_id, name=None, gender=None, major=None, gpa=None):
        for student in self.students:
            if student.id == student_id:
                if name:
                    student.name = name
                if gender:
                    student.gender = gender
                if major:
                    student.major = major
                if gpa is not None:
                    student.gpa = gpa
                print("\nThông tin sinh viên đã được cập nhật!")
                return
        print("\nKhông tìm thấy sinh viên với ID đã nhập!")
    
    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print("\nSinh viên đã được xóa!")
                return
        print("\nKhông tìm thấy sinh viên với ID đã nhập!")
    
    def search_student(self, name):
        results = [student for student in self.students if name.lower() in student.name.lower()]
        if results:
            print("\nDanh sách sinh viên tìm được:")
            for student in results:
                print(student)
        else:
            print("\nKhông tìm thấy sinh viên với tên đã nhập!")
    
    def sort_by_gpa(self):
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        print("\nDanh sách sinh viên đã được sắp xếp theo điểm trung bình!")
    
    def sort_by_major(self):
        self.students.sort(key=lambda x: x.major)
        print("\nDanh sách sinh viên đã được sắp xếp theo chuyên ngành!")
    
    def display_students(self):
        if not self.students:
            print("\nDanh sách sinh viên trống!")
        else:
            print("\nDanh sách sinh viên:")
            for student in self.students:
                print(student)

def main():
    management = StudentManagement()
    while True:
        print("\n----- Quản lý Sinh viên -----")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp danh sách theo điểm trung bình")
        print("6. Sắp xếp danh sách theo tên chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == "1":
            name = input("Nhập tên sinh viên: ")
            gender = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            gpa = float(input("Nhập điểm trung bình: "))
            management.add_student(name, gender, major, gpa)
        
        elif choice == "2":
            student_id = int(input("Nhập ID sinh viên cần cập nhật: "))
            name = input("Nhập tên mới (bỏ trống nếu không đổi): ") or None
            gender = input("Nhập giới tính mới (bỏ trống nếu không đổi): ") or None
            major = input("Nhập chuyên ngành mới (bỏ trống nếu không đổi): ") or None
            gpa_input = input("Nhập điểm trung bình mới (bỏ trống nếu không đổi): ")
            gpa = float(gpa_input) if gpa_input else None
            management.update_student(student_id, name, gender, major, gpa)
        
        elif choice == "3":
            student_id = int(input("Nhập ID sinh viên cần xóa: "))
            management.delete_student(student_id)
        
        elif choice == "4":
            name = input("Nhập tên sinh viên cần tìm: ")
            management.search_student(name)
        
        elif choice == "5":
            management.sort_by_gpa()
        
        elif choice == "6":
            management.sort_by_major()
        
        elif choice == "7":
            management.display_students()
        
        elif choice == "8":
            print("\nThoát chương trình!")
            break
        
        else:
            print("\nLựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()
