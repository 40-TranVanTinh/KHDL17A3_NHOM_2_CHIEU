x1 = 0
x2 = 26

# Xác suất P(X = x1)
p_x1 = 0.2

# Tính P(X = x2)
p_x2 = 1 - p_x1

p_x2_pow = pow(0.8, 2)

# Hiển thị phân phối xác suất
print("Phân phối xác suất:")
print(f"X = {x1}: P(X = {x1}) = {p_x1}")
print(f"X = {x2}: P(X = {x2}) = {p_x2_pow}")
