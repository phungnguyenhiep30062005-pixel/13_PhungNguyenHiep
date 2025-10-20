# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên
      trên một dòng theo định dạng: 
      " - Ten: [Họ tên], Nam sinh: [Năm sinh], Dia chi: [Địa chỉ]"
    """
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for sv in student_list:
            print(f" - Ten: {sv['name']}, Nam sinh: {sv['year_of_birth']}, Dia chi: {sv['address']}")
