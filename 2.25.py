# Hàm mật độ f(x) cho x > 2
def f(x):
    return 4 / x**3

# Phương pháp tích phân số học (phương pháp hình thang)
def integrate(f, start, end, steps):
    total_area = 0
    step_size = (end - start) / steps

    for i in range(steps):
        begin = start + i * step_size
        end = start + (i + 1) * step_size
        total_area += (f(begin) + f(end)) * step_size / 2

    return total_area

# Tính xác suất chi cho y tế trong năm là trên 3 triệu đồng
# Vì hàm mật độ giảm nhanh, nên ta giới hạn phạm vi tích phân
xac_suat = integrate(f, 3, 1000, 100000)

print(f'Xác suất chi cho y tế trong năm là trên 3 triệu đồng là: {xac_suat}')

# Hàm mật độ f(x)
def f(x):
    if x <= 0:
         return 0
    elif x <= 2:
        return x / 4
    else:
        return 4 / x**3
# Tính kỳ vọng E(X)
def expected_value():
    result = 0
# Tích phân từ 0 đến 2
    for i in range(0, 2000):
        x = i / 1000
        result += x * (x / 4) * (1 / 1000)
# Tích phân từ 2 đến vô cùng
    for i in range(2000, 10000):
        x = i / 1000
        result += x * (4 / x**3) * (1 / 1000)
    return result

# Tính phương sai Var(X)
def variance(expected_x):
    result = 0
# Tích phân từ 0 đến 2
    for i in range(0, 2000):
        x = i / 1000
        result += ((x - expected_x)**2) * (x / 4) * (1 / 1000)
# Tích phân từ 2 đến vô cùng
    for i in range(2000, 10000):
        x = i / 1000
        result += ((x - expected_x)**2) * (4 / x**3) * (1 / 1000)
    return result

# Tính toán kỳ vọng và phương sai
E_X = expected_value()
Var_X = variance(E_X)

print(f"Kỳ vọng E(X): {E_X}")
print(f"Phương sai Var(X): {Var_X}")