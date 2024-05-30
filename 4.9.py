# Hệ số a
a = 1 / 20

# Phân phối xác suất biên của X
PX = [3 * a, 2 * a, 5 * a]  # Sửa giá trị PX dựa trên a = 1/20

# Phân phối xác suất biên của Y
PY = [2 * a, 1 * a, 7 * a]  # Sửa giá trị PY dựa trên a = 1/20

# Tính P[X|Y] và P[Y|X]
P_X_given_Y = [[1 / 2, 1 / 2, 0],  # Sửa giá trị P_X_given_Y
                [1 / 6, 1 / 3, 2 / 3],
                [1 / 6, 2 / 5, 2 / 5]]

P_Y_given_X = [[1, 0, 0],  # Sửa giá trị P_Y_given_X
                [1 / 2, 1 / 2, 0],
                [1 / 7, 4 / 7, 2 / 7]]

# In kết quả
print("Phân phối xác suất biên của X:")
for i, px in enumerate(PX):
    print(f"P(X={i + 1}) = {px:.2f}")

print("\nPhân phối xác suất biên của Y:") 
for i, py in enumerate(PY):
    print(f"P(Y={i + 1}) = {py:.2f}")

print("\nXác suất điều kiện P[X|Y]:")
for i in range(3):
    for j in range(3):
        print(f"P(X={i + 1}|Y={j + 1}) = {P_X_given_Y[i][j]:.2f}")

print("\nXác suất điều kiện P[Y|X]:")
for i in range(3):
    for j in range(3):
        print(f"P(Y={i + 1}|X={j + 1}) = {P_Y_given_X[i][j]:.2f}")
