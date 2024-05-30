#a
def f_X(x):
    return 4 * x * (1 - x**2)

def f_Y(y):
    return 4 * y**2

# 
x_value = 0.4
y_value = 0.6
print(f"f_X({x_value}) =", f_X(x_value))
print(f"f_Y({y_value}) =", f_Y(y_value))
#b
def f_X_given_Y(x, y):
    return 2 * x / y

def f_Y_given_X(y, x):
    return 2* y / (1 - x**2)

# 
x_value = 0.4
y_value = 0.6
print(f"f_X_given_Y({x_value}|{y_value}) =", f_X_given_Y(x_value, y_value))
print(f"f_Y_given_X({y_value}|{x_value}) =", f_Y_given_X(y_value, x_value))

# 
x_value = 0.4
y_value = 0.6
print(f"f_X({x_value}) =", f_X(x_value))
print(f"f_Y({y_value}) =", f_Y(y_value))




#c
def f_X(x):
    return 4 * x * (1 - x**2)

def f_Y(y):
    return 4 * y**2

def riemann_sum(func, lower, upper, num_samples=1000):
    delta_x = (upper - lower) / num_samples
    total_sum = 0
    for i in range(num_samples):
        x_i = lower + i * delta_x
        total_sum += x_i * func(x_i) * delta_x
    return total_sum

# Calculate E(X) and E(Y)
E_X = riemann_sum(f_X, 0, 1)
E_Y = riemann_sum(f_Y, 0, 1)

# Calculate E(X^2) and E(Y^2)
E_X_squared = riemann_sum(lambda x: x**2 * f_X(x), 0, 1)
E_Y_squared = riemann_sum(lambda y: y**2 * f_Y(y), 0, 1)

# Calculate V(X) and V(Y)
V_X = E_X_squared - E_X**2
V_Y = E_Y_squared - E_Y**2

print(f"E(X) = {E_X:.4f}")
print(f"E(Y) = {E_Y:.4f}")
print(f"V(X) = {V_X:.4f}")
print(f"V(Y) = {V_Y:.4f}")
#d
def f_xy(x, y):
    if 0 < x <= y < 1:
        return 8 * x * y
    else:
        return 0

def f_Y(y):
    # Hàm mật độ xác suất của Y
    return 8 * y

def E_X_given_y(y):
    # Tính E(X|y)
    num_points = 1000  # Số điểm chia khoảng [0, y] thành
    dx = y / num_points
    expectation = 0
    for i in range(num_points):
        x = i * dx
        expectation += x * f_xy(x, y) * dx
    return expectation

def E_Y_given_x(x):
    # Tính E(Y|x)
    num_points = 1000  # Số điểm chia khoảng [x, 1] thành
    dy = (1 - x) / num_points
    expectation = 0
    for i in range(num_points):
        y = x + i * dy
        expectation += y * f_xy(x, y) * dy
    return expectation


E_X_y = E_X_given_y(0.4)
E_Y_x = E_Y_given_x(0.6)

print(f"E(X|y=0.4) = {E_X_y:.4f}")
print(f"E(Y|x=0.6) = {E_Y_x:.4f}")
#e
dx=0.01
dy=0.01
# Tính Cov(X, Y)
Cov_XY = 0
for i in range(1, 101):
    x = i * dx
    for j in range(1, 101):
        y = j * dy
        if 0 < x <= y < 1:
            Cov_XY += (x - E_X) * (y - E_Y) * 8 * x * y * dx * dy

print("Cov(X, Y): ", Cov_XY)

# Tính hệ số tương quan ρ(X, Y)
rho_XY = Cov_XY / ((V_X * 0.5) * (V_Y * 0.5))
print("ρ(X, Y): ", rho_XY)