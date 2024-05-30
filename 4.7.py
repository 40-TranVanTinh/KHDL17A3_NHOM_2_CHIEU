import math

x = [1, 1.5, 2]
y = [100, 200, 300]
P = [
    [0.05, 0.10, 0.14],
    [0.05, 0.20, 0.15],
    [0.01, 0.05, 0.15]
]

#a. Tính kỳ vọng và phương sai của quảng cáo:
# Tính kỳ vọng của quảng cáo
E_y = sum(y[j] * sum(P[i][j] for i in range(len(x))) for j in range(len(y)))
print("Kỳ vọng của quảng cáo:", E_y)

# Tính phương sai của quảng cáo
V_y = sum(P[i][j] * (y[j] - E_y)**2 for i in range(len(x)) for j in range(len(y)))
print("Phương sai của quảng cáo:", V_y)

#b. Tính xác suất quảng cáo 300 triệu đồng với điều kiện kinh doanh số bán hàng là 2:
P_y300_x2 = P[2][2]
print("Xác suất quảng cáo 300 triệu đồng với điều kiện kinh doanh số bán hàng là 2:", P_y300_x2)

#c. Tính hiệp phương sai và hệ số tương quan giữa X và Y
# Tính kỳ vọng của X
E_x = sum(x[i] * sum(P[i][j] 
     for j in range(len(y))) 
          for i in range(len(x)))
print("Kỳ vọng của X:", E_x)

# Tính hiệp phương sai giữa X và Y
Cov_xy = sum((x[i] - E_x) * (y[j] - E_y) * P[i][j] 
    for i in range(len(x))
        for j in range(len(y)))
print("Hiệp phương sai giữa X và Y:", Cov_xy)

# Tính hệ số tương quan giữa X và Y
# Tính độ lệch chuẩn của X
V_x = sum(P[i][j] * (x[i] - E_x)**2 
    for i in range(len(x)) 
        for j in range(len(y)))
std_x = math.sqrt(V_x)
print("Độ lệch chuẩn của X:", std_x)

# Tính độ lệch chuẩn của Y (đã có từ câu a)
std_y = math.sqrt(V_y)
print("Độ lệch chuẩn của Y:", std_y)

# Hệ số tương quan
corr_xy = Cov_xy / (std_x * std_y)
print("Hệ số tương quan giữa X và Y:", corr_xy)

#d. Tính kỳ vọng và phương sai khi doanh số bán hàng là 1,5
E_y_x1_5 = sum(y[j] * P[i][j] 
    for i in range(len(x)) 
        for j in range(len(y)) if x[i] == 1.5)
print("Kỳ vọng của quảng cáo khi doanh số bán hàng là 1,5 triệu:", E_y_x1_5)

