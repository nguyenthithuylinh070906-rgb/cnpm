# main.py - Quản lý học sinh
students = []

def add_student():
    name = input("Nhập tên học sinh: ")
    age = input("Nhập tuổi học sinh: ")
    students.append({"name": name, "age": age})
    print(f"Đã thêm {name}")

def show_students():
    if not students:
        print("Chưa có học sinh nào.")
        return
    for i, student in enumerate(students):
        print(f"{i+1}. {student['name']} - {student['age']} tuổi")

def edit_student():
    show_students()
    idx = int(input("Chọn số thứ tự học sinh muốn sửa: ")) - 1
    if 0 <= idx < len(students):
        name = input("Nhập tên mới: ")
        age = input("Nhập tuổi mới: ")
        students[idx] = {"name": name, "age": age}
        print("Đã cập nhật thông tin học sinh.")
    else:
        print("Không tồn tại học sinh này.")

def delete_student():
    show_students()
    idx = int(input("Chọn số thứ tự học sinh muốn xóa: ")) - 1
    if 0 <= idx < len(students):
        removed = students.pop(idx)
        print(f"Đã xóa {removed['name']}")
    else:
        print("Không tồn tại học sinh này.")

def menu():
    while True:
        print("\n1. Thêm học sinh")
        print("2. Xem danh sách học sinh")
        print("3. Sửa học sinh")
        print("4. Xóa học sinh")
        print("5. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Chọn chức năng không hợp lệ.")

if __name__ == "__main__":
    menu()
h