import math

# Hàm mật độ biên của X
def marginal_density_X(x):
    if 0 <= x <= math.pi/2:
        return math.sin(x) * (math.pi/2) + 2
    else:
        return 0

# Hàm mật độ biên của Y
def marginal_density_Y(y):
    if 0 <= y <= math.pi/2:
        return 2 + math.sin(y) * (math.pi/2)
    else:
        return 0

# Hàm tính tích phân bằng phương pháp hình thang
def trapezoidal_rule(f, a, b, n=1000):
    h = (b - a) / n
    sum_f = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum_f += f(a + i * h)
    return sum_f * h

# Tính xác suất
def probability_X_Y(x_lower, x_upper, y_lower, y_upper):
    def joint_density(x, y):
        return marginal_density_X(x) * marginal_density_Y(y)

    def integrate_Y(x):
        return trapezoidal_rule(lambda y: joint_density(x, y), y_lower, y_upper)

    return trapezoidal_rule(integrate_Y, x_lower, x_upper)

# Giới hạn của X và Y
x_lower = math.pi/6
x_upper = math.pi/2
y_lower = math.pi/4
y_upper = math.pi/3

# Tính và in ra hàm mật độ biên và xác suất
for x in [x_lower, x_upper]:
    print(f"Hàm mật độ biên của X tại x = {x} là: {marginal_density_X(x)}")
for y in [y_lower, y_upper]:
    print(f"Hàm mật độ biên của Y tại y = {y} là: {marginal_density_Y(y)}")

prob = probability_X_Y(x_lower, x_upper, y_lower, y_upper)
print("Xác suất P(pi/6 < X < pi/2, pi/4 < Y < pi/3) là:", prob)
