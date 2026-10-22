tong_phut = 135
cong_suat_w = 250

# Tính giờ và phút
so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60
print(f"Thời gian: {so_gio} giờ {phut_con_lai} phút")

# Biểu thức logic / so sánh
su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)

print("Sử dụng lâu (>60p):", su_dung_lau)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# Kiểm chứng độ ưu tiên toán tử
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)