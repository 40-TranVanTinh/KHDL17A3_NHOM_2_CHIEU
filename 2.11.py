import numpy as np
p_thanh_cong = 1/4

# Phân phối xác suất
x = np.array([1, 2, 3, 4])
P_x = np.array([1/4, 3/16, 9/64, 27/256])

print("Phân phối xác suất:")
print("X", P_x)

# Kì vọng
E_X = np.sum(x * P_x)
print("\nKì vọng:", E_X)

# Phương sai
Var_X = np.sum((x - E_X)**2 * P_x)
print("Phương sai:", Var_X)

# Hàm phân phối xác suất 
def hppxs(x):
  if x < 1:
    return 1/4
  elif x < 2:
    return 1/4 + 3/16
  else:
    return 1/4 + 3/16 + 9/64

A = np.array([hppxs(xi) for xi in x])

print("\nHàm phân phối xác suất (CDF):")
print("X", A)

# Mốt
mode = x[P_x == P_x.max()]
print("\nMốt:", mode)
