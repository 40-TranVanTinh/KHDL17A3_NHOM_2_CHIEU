import math

# Giá trị kỳ vọng của X
E_X = 5

# Giá trị E[X(X-1)]
E_X_X_minus_1 = 27.5

# Tính phương sai V(X)
V_X = E_X_X_minus_1 + E_X**2 - E_X**2
print("Phương sai V(X):", V_X)

# Tính độ lệch chuẩn σ(X)
sigma_X = math.sqrt(V_X)
print("Độ lệch chuẩn σ(X):", sigma_X)