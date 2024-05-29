# 1)

#Hàm từ đề bài
def f(x):
    if x <= 2:
        return 0
    elif 2 < x <= 3:
        return (x - 2)**2
    else:
        return 0

#Hàm tính tích phân
def integrate(a, b, function, num_steps=10000):
    step_size = (b - a) / num_steps
    area = 0
    for i in range(num_steps):
        area += function(a + i * step_size) * step_size
    return area


# 2) Tính P(1 < X < 1.6)
def probability(a, b):
    p = 0
    step = 0.001  # Độ chính xác của phép tính
    x = a
    while x < b:
        p += f(x) * step
        x += step
    return p

result = probability(1, 1.6)


# 3)
# Tính kỳ vọng E(X)
def expected_value():
    return integrate(2, 3, lambda x: x * f(x))

# Tính E(X^2)
def expected_value_squared():
    return integrate(2, 3, lambda x: (x**2) * f(x))

# Tính phương sai Var(X)
def variance(ex, ex2):
    return ex2 - ex**2

ex = expected_value()
ex2 = expected_value_squared()
vx = variance(ex, ex2)


# 4)
# Tính moment bậc 3 E(X^3)
def third_moment():
    return integrate(2, 3, lambda x: (x**3) * f(x))

# Tính moment bậc 4 E(X^4)
def fourth_moment():
    return integrate(2, 3, lambda x: (x**4) * f(x))

#Tính hệ số bất đối xứng và hệ số nhọn 
def skewness_kurtosis(ex, ex2, ex3, ex4, var):
    skewness = (ex3 - 3*ex*ex2 + 2*ex**3) / var**(3/2)
    kurtosis = (ex4 - 4*ex*ex3 + 6*ex2*ex**2 - 3*ex**4) / var**2
    return skewness, kurtosis

ex3 = third_moment()
ex4 = fourth_moment()
skewness, kurtosis = skewness_kurtosis(ex, ex2, ex3, ex4, vx)

#Tìm mốt của
def find_mode(density_func, start, end, step):
    max_density = 0
    mode_value = None
    for x in range(int((end - start) / step)):
        x_value = start + x * step
        density = density_func(x_value)
    if density > max_density:
        max_density = density
        mode_value = x_value
    return mode_value

# Tính mốt của X
#Mốt của ( X ) là giá trị mà tại đó hàm mật độ xác suất đạt giá trị lớn nhất, trong trường hợp này là ( x = 3 )
mode_of_X = find_mode(f, 2, 3, 0.000001)

print(f"Hàm mật độ xác suất f(x):")
print('f(x)=(2x-4),2<x<=3')
print("P(1 < X < 1.6) =", result)
print(f"Kỳ vọng E(X): {ex}")
print(f"E(X^2): {ex2}")
print(f"Phương sai Var(X): {vx}")
print(f"Mốt của X là: {mode_of_X}")
print("Hệ số bất đối xứng của X:", skewness)
print("Hệ số nhọn của X:", kurtosis)