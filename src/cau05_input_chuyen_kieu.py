ma_may = input("Nhập mã máy: ")
cong_suat_str = input("Nhập công suất W: ")
so_phut_str = input("Nhập số phút sử dụng: ")
don_gia_str = input("Nhập đơn giá điện/kWh: ")

print("\nKiểu dữ liệu ban đầu:")
print("Mã máy:", type(ma_may))
print("Công suất:", type(cong_suat_str))
print("Số phút:", type(so_phut_str))
print("Đơn giá:", type(don_gia_str))

# Chuyển kiểu
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\nKết quả:")
print("Điện năng (kWh):", dien_nang_kwh)
print("Chi phí (VND):", chi_phi)