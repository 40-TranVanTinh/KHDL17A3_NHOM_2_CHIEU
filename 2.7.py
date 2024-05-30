# Tỷ lệ phế phẩm của máy sản xuất
p_defect_machine = 0.02

# Tỷ lệ phế phẩm của lô hàng
p_defect_batch = 0.4

# Tạo bảng phân phối xác suất của X
X_values = [0, 1, 2]
X_probs = [p_defect_machine * (1 - p_defect_batch),
          p_defect_machine * p_defect_batch + (1 - p_defect_machine) * (1 - p_defect_batch),
          (1 - p_defect_machine) * p_defect_batch]

print("Bảng phân phối xác suất của X:")
for x, p in zip(X_values, X_probs):
    print(f"X = {x}, P(X) = {p:.3f}")

# Tính kì vọng của X
E_X = 0 * X_probs[0] + 1 * X_probs[1] + 2 * X_probs[2]
print(f"\nE(X) = {E_X:.3f}")

# Tính phương sai của X
Var_X = 0 * (X_values[0] - E_X)**2 * X_probs[0] + \
        1 * (X_values[1] - E_X)**2 * X_probs[1] + \
        2 * (X_values[2] - E_X)**2 * X_probs[2]
print(f"Var(X) = {Var_X:.3f}")

# Tính kì vọng và phương sai của Y
E_Y = 2 * E_X - 5
Var_Y = 4 * Var_X

print(f"\nE(Y) = {E_Y:.3f}")
print(f"Var(Y) = {Var_Y:.3f}")

# Tính xác suất để số sản phẩm tốt do máy sản xuất và số sản phẩm tốt lấy ra từ lô hàng bằng nhau
p_equal_good = p_defect_machine * (1 - p_defect_batch) + (1 - p_defect_machine) * p_defect_batch
print(f"\nXác suất để số sản phẩm tốt do máy sản xuất và số sản phẩm tốt lấy ra từ lô hàng bằng nhau: {p_equal_good:.3f}") 