import math
lamda = 0.01

# 1) Tính xác suất bóng đèn hoạt động tốt trước to giờ
t = 10  # giả sử t = 10 giờ
hd = 1 - math.exp(-lamda * t)
print(f"Xác suất bóng đèn hoạt động tốt trước {t} giờ là: {hd}")

# 2) Tính kì vọng của thời gian hoạt động tốt
tg = 1 / lamda
print(f"Kì vọng của thời gian hoạt động tốt là: {tg} giờ")
