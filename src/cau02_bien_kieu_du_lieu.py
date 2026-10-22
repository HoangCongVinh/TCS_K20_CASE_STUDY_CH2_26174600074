# Tạo biến theo quy tắc snake_case
ma_phien = "LAB026"         # str
ma_may = "PC12"             # str
cong_suat_w = 250.0        # float
thoi_gian_phut = 90         # int
dang_hoat_dong = True       # bool
ghi_chu = None              # NoneType

# In giá trị và kiểm tra kiểu bằng type()
print("Mã phiên:", ma_phien, type(ma_phien))
print("Mã máy:", ma_may, type(ma_may))
print("Công suất (W):", cong_suat_w, type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, type(thoi_gian_phut))
print("Trạng thái:", dang_hoat_dong, type(dang_hoat_dong))
print("Ghi chú:", ghi_chu, type(ghi_chu))

# Gán lại thời gian từ 90 thành 120
thoi_gian_phut = 120
print("Thời gian mới (phút):", thoi_gian_phut)
