class Player:
    def __init__(self, ma, name, speed_score, technique_score, goal_score):
        self.id = ma.upper()
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.__average_score = 0
        self.__performance_type = ""
        self.calculate_average()
        self.classify_performance()

    @property
    def average_score(self):
        return self.__average_score

    @property
    def performance_type(self):
        return self.__performance_type

    def calculate_average(self):
        raw_score = (self.speed_score * 0.3) + (self.technique_score * 0.4) + (self.goal_score * 0.3)
        self.__average_score = round(raw_score, 2)

    def classify_performance(self):
        if self.__average_score < 5.0:
            self.__performance_type = "Dự bị yếu"
        elif self.__average_score < 6.5:
            self.__performance_type = "Trung bình"
        elif self.__average_score < 8.0:
            self.__performance_type = "Tốt"
        else:
            self.__performance_type = "Ngôi sao"




class PlayerManager:
    def __init__(self):
        self.players = []

    def find_player_by_id(self, ma):
        for i in self.players:
            if i.id == ma.upper():
                return i

    def get_valid_score(self, diem):
        while True:
            try:
                value = float(input(diem))
                if value < 0 or value > 10:
                    print("Điểm số bắt buộc phải nằm trong khoảng từ 0 đến 10!")
                else:
                    return value
            except ValueError:
                print("Định dạng sai! Vui lòng nhập lại")
    def show_all(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng!")
            return

        print("\n" + "="*100)
        print(f"{'Mã số':<10} | {'Họ và tên cầu thủ':<25} | {'Tốc độ':<8} | {'Kỹ thuật':<8} | {'Ghi bàn':<8} | {'Điểm ĐG':<8} | {'Phong độ'}")
        print("-" * 95)
        for p in self.players:
            print(f"{p.id:<10} | {p.name:<25} | {p.speed_score:<8} | {p.technique_score:<8} | {p.goal_score:<8} | {p.average_score:<8} | {p.performance_type}")
        print("="*100)

    def add_product(self):
        while True:
            ma = input("Nhập Mã cầu thủ: ").strip().upper()
            if not ma:
                print("Mã cầu thủ không được để trống!")
                continue
            if self.find_player_by_id(ma):
                print("Mã cầu thủ này đã tồn tại trong hệ thống!")
                continue
            break

        while True:
            name = input("Nhập Họ tên cầu thủ: ").strip()
            if not name:
                print("Họ tên không được để trống!")
            else:
                break

        speed_score = self.get_valid_score("Nhập điểm tốc độ: ")
        technique_score = self.get_valid_score("Nhập điểm kỹ thuật: ")
        goal_score = self.get_valid_score("Nhập điểm ghi bàn: ")

        new_player = Player(ma, name, speed_score, technique_score, goal_score)
        self.players.append(new_player)
        print("Thêm cầu thủ thành công!")

    def update_player(self):
        ma = input("Nhập mã cầu thủ cần cập nhật: ").strip()
        player = self.find_player_by_id(ma)

        if not player:
            print("Không tìm thấy cầu thủ cần cập nhật!")
            return

        print(f"Đang cập nhật cho cầu thủ: {player.name}")
        speed_score = self.get_valid_score("Nhập điểm tốc độ moi: ")
        technique_score = self.get_valid_score("Nhập diểm kỹ thuật mới: ")
        goal_score = self.get_valid_score("Nhập điểm ghi bàn mới: ")

        player.speed_score = speed_score
        player.technique_score = technique_score
        player.goal_score = goal_score
        
        player.calculate_average()
        player.classify_performance()
        print("Cập nhật cầu thủ thành công!")

    def delete_player(self):
        ma = input("Nhập mã cầu thủ cần xóa: ").strip()
        player = self.find_player_by_id(ma)

        if not player:
            print("Không tìm thấy cầu thủ cần xóa!")
            return

        confirm = input(f"Bạn có chắc muốn xóa cầu thủ {player.name} không? (Y/N): ").strip().upper()
        if confirm == 'Y':
            self.players.remove(player)
            print("Xóa cầu thủ thành công!")
        elif confirm == 'N':
            print("Đã hủy thao tác!")
        else:
            print("Bạn vui lòng nhập đúng kí tự")

    def search_player(self):
        key = input("Nhập tên cầu thủ bạn cần tìm: ").strip().lower()
        list_tam = []

        for i in self.players:
            if key in i.name.lower():
                list_tam.append(i)

        if not list_tam:
            print("Không tìm thấy cầu thủ phù hợp!")
        else:
            for i in list_tam:
                print(f"Mã: {i.id} | Tên: {i.name} | Điểm ĐG: {i.average_score} | Phong độ: {i.performance_type}")



def main():
    def hien_thi_menu():
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật thông tin cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Thoát")
        print("=====================================")

    manager = PlayerManager()

    while True:
        hien_thi_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case '1':
                manager.show_all()
            case '2':
                manager.add_product()
            case '3':
                manager.update_player()
            case '4':   
                manager.delete_player()
            case '5':
                manager.search_player()
            case '6':
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý cầu thủ bóng đá!")
                break
            case _:
                print("Lựa chọn menu không hợp lệ, vui lòng nhập lại!")


main()


