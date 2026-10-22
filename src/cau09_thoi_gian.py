from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Giải thích:
# - datetime: Đối tượng kiểu ngày giờ đầy đủ.
# - str: Chuỗi kí tự được định dạng từ datetime để hiển thị.
# - timedelta: Biểu thị một khoảng thời gian (hiệu của 2 mốc datetime).