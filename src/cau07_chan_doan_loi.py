# Code đã sửa lỗi hoàn chỉnh:
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Chuyển thành float để thực hiện phép toán
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")       # Đổi tên đúng biến 'dien_nang_kwh' và đóng ngoặc ')'

# MÔ TẢ LỖI ĐÃ PHÁT HIỆN:
# 1. TypeError: cong_suat_w chưa ép kiểu nên mang kiểu 'str', không thể nhân chia số học.
# 2. NameError: Biến 'dien_nang' sai tên so với biến được định nghĩa là 'dien_nang_kwh'.
# 3. SyntaxError: Thiếu dấu đóng ngoặc tròn ')' ở cuối lệnh print.