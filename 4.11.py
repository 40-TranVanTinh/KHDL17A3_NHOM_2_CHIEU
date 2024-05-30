# Bảng phân phối xác suất đồng thời
p_xy = [
    [0.10, 0.05, 0.05],
    [0.10, 0.20, 0.05],
    [0.05, 0.35, 0],
]

# Tính tổng xác suất
p_sum = 0
for row in p_xy:
    for cell in row:
        p_sum += cell

# Tính p
p = 1 - p_sum
print("Giá trị p:", p)

# Xác định phân phối xác suất biên cho X
p_x = [0] * len(p_xy[0])
for row in p_xy:
    for i, cell in enumerate(row):
        p_x[i] += cell

print("Phân phối xác suất biên cho X:", p_x)

# Xác định phân phối xác suất biên cho Y
p_y = [0] * len(p_xy)
for i in range(len(p_xy[0])):
    for row in p_xy:
        p_y[i] += row[i]

print("Phân phối xác suất biên cho Y:", p_y)

# Tính hiệp phương sai
cov_xy = 0
for i in range(len(p_xy)):
    for j in range(len(p_xy[0])):
        x = i * 10  # Lương (triệu đồng)
        y = j * 5  # Thưởng (triệu đồng)
        mean_x = sum([x * p_x[i] for i in range(len(p_x))])
        mean_y = sum([y * p_y[j] for j in range(len(p_y))])
        cov_xy += (x - mean_x) * (y - mean_y) * p_xy[i][j]

print("Hiệp phương sai Cov(X, Y):", cov_xy)

# Tính hệ số tương quan
var_x = 0
for i in range(len(p_x)):
  x = i * 10  # Lương (triệu đồng)
  mean_x = sum([x * p_x[i] for i in range(len(p_x))])
  var_x += (x - mean_x)**2 * p_x[i]

var_y = 0
for i in range(len(p_y)):
  y = i * 5  # Thưởng (triệu đồng)
  mean_y = sum([y * p_y[i] for i in range(len(p_y))])
  var_y += (y - mean_y)**2 * p_y[i]

rho_xy = (cov_xy / (var_x * var_y))**0.5
print("Hệ số tương quan rho_xy:", rho_xy)

# Tính kì vọng và phương sai của lương khi thưởng là 5 triệu đồng
# Lọc dữ liệu khi Y = 5
p_xy_5 = [row[1] for row in p_xy]
print("Dữ liệu lọc khi Y = 5:", p_xy_5)

# Kì vọng của X khi Y = 5:
E_X_5 = 0
for i in range(len(p_xy_5)):
  x = i * 10  # Lương (triệu đồng)
  E_X_5 += x * p_xy_5[i]

print("Kì vọng của X khi Y = 5:", E_X_5)

# Phương sai của X khi Y = 5:
var_X_5 = 0
for i in range(len(p_xy_5)):
  x = i * 10  # Lương (triệu đồng)
  mean_x = sum([x * p_xy_5[i] for i in range(len(p_xy_5))])
  var_X_5 += (x - mean_x)**2 * p_xy_5[i]

print("Phương sai của X khi Y = 5:", var_X_5)
