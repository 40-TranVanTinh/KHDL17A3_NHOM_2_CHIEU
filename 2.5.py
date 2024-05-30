# Xác suất ném trúng rổ của mỗi người
p_trung = [0.7, 0.8]

# Số lần ném của mỗi người
n = 2

# Tạo bảng phân phối xác suất
P = []

# Tính xác suất cho từng trường hợp
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        p = 1
        for k in range(2):
            # Xác suất ném của người thứ k
            p_k = p_trung[k] if i < n else 0
            # Xác suất trượt của người thứ k
            p_truot_k = 1 - p_trung[k]
            # Tính xác suất cho người thứ k
            p *= p_k ** i * p_truot_k ** (n - i)
        row.append(p)
    P.append(row)

# In bảng phân phối xác suất
print("Bảng phân phối xác suất của X:")
for row in P:
    print(row)


# Xác suất có 1 quả trúng và 1 quả trượt
P_1_trung_1_truot = P[1][1] + P[2][0]

# Xác suất có 2 quả trúng
P_2_trung = P[2][2]

# Xác suất tổng cộng
P_bang_nhau = P_1_trung_1_truot + P_2_trung

print("Xác suất để số quả ném trúng rổ của hai người bằng nhau:", P_bang_nhau)