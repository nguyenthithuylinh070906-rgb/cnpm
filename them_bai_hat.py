songs = []  # danh sách bài hát

while True:
    print("\n--- MENU ---")
    print("1. Thêm bài hát")
    print("2. Xem danh sách bài hát")
    print("3. Thoát")

    choice = input("Chọn (1/2/3): ")

    if choice == "1":
        song = input("Nhập tên bài hát: ")
        songs.append(song)
        print("Đã thêm!")
    elif choice == "2":
        print("\nDanh sách bài hát:")
        for s in songs:
            print("- " + s)
    elif choice == "3":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ!")

