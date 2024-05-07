# Bài 1
Num_1 = int(input("Enter the first number: "))
Num_2 = int(input("Enter the second number: "))
Cal = Num_1 * Num_2
print(f"{Num_1} * {Num_2} = {Cal}")

# Bài 2:
diem_toan = float(input("Vui lòng nhập điểm toán: "))
diem_ly = float(input("Vui lòng nhập điểm lý: "))
diem_hoa = float(input("Vui lòng nhập điểm hoá: "))
result = sum([diem_toan, diem_ly, diem_hoa])/3
print("Điểm trung bình 3 môn học là ",result)

# Bài 3:
def tinh_van_toc_met_moi_phut(van_toc_km_gio):
    van_toc_met_gio = van_toc_km_gio * 1000  # chuyển đơn vị từ km/h sang m/h
    van_toc_met_phut = van_toc_met_gio / 60  # chia cho 60 để tính vận tốc mỗi phút
    return van_toc_met_phut

def tinh_quang_duong_sau_thoi_gian(van_toc_km_gio, gio, phut):
    thoi_gian_gio = gio + phut / 60  # chuyển thời gian từ giờ và phút sang giờ
    quang_duong_km = van_toc_km_gio * thoi_gian_gio
    return quang_duong_km

# Nhập vận tốc của đoàn tàu
van_toc_km_h = float(input("Nhập vận tốc của đoàn tàu (km/h): "))

# a. Tính vận tốc trung bình mỗi phút
van_toc_met_phut = tinh_van_toc_met_moi_phut(van_toc_km_h)
print("Vận tốc trung bình mỗi phút của đoàn tàu là:", van_toc_met_phut, "m/s")

# b. Tính quãng đường sau 1 giờ 12 phút
gio = 1
phut = 12
quang_duong_km = tinh_quang_duong_sau_thoi_gian(van_toc_km_h, gio, phut)
print("Sau 1 giờ 12 phút, đoàn tàu đi được quãng đường là:", quang_duong_km, "km")
