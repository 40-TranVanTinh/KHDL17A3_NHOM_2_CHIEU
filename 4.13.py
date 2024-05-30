# Mật độ biên f_X tại x=1
x = 1
dy = 0.01
integral = 0
y = dy
while y <= 10:
    if x > 0 and y > 0:
        integral += (2.718281828459045 ** (-x - y)) * dy  # e^(-x-y)
    y += dy

print("Mật độ biên f_X tại x=1: ", integral)

# Mật độ biên f_Y tại y=1
y = 1
dx = 0.01
integral = 0
x = dx
while x <= 10:
    if x > 0 and y > 0:
        integral += (2.718281828459045 ** (-x - y)) * dx  # e^(-x-y)
    x += dx

print("Mật độ biên f_Y tại y=1: ", integral)


# Mật độ có điều kiện f_X|Y tại x=1, y=1
x = 1
y = 1
numerator = (2.718281828459045 ** (-x - y)) if x > 0 and y > 0 else 0  # e^(-x-y)

y = 1
dx = 0.01
denominator = 0
x_val = dx
while x_val <= 10:
    if x_val > 0 and y > 0:
        denominator += (2.718281828459045 ** (-x_val - y)) * dx  # e^(-x-y)
    x_val += dx

conditional_f_X_given_Y = numerator / denominator
print("Mật độ có điều kiện f_X|Y tại x=1, y=1: ", conditional_f_X_given_Y)

# Mật độ có điều kiện f_Y|X tại y=1, x=1
x = 1
y = 1
numerator = (2.718281828459045 ** (-x - y)) if x > 0 and y > 0 else 0  # e^(-x-y)

x = 1
dy = 0.01
denominator = 0
y_val = dy
while y_val <= 10:
    if x > 0 and y_val > 0:
        denominator += (2.718281828459045 ** (-x - y_val)) * dy  # e^(-x-y)
    y_val += dy

conditional_f_Y_given_X = numerator / denominator
print("Mật độ có điều kiện f_Y|X tại y=1, x=1: ", conditional_f_Y_given_X)

from math import log

c = log(2)
dx = 0.01
dy = 0.01
integral = 0
y = dy
while y <= c:
    x = dx
    while x <= y:
        if x > 0 and y > 0:
            integral += (2.718281828459045 ** (-x - y)) * dx * dy  # e^(-x-y)
        x += dx
    y += dy

print("P(X ≤ Y ≤ c): ", integral)
# Tính P(X < Y)
dx = 0.01
dy = 0.01
integral = 0
x = dx
while x <= 10:
    y = x + dy
    while y <= 10:
        if x > 0 and y > 0:
            integral += (2.718281828459045 ** (-x - y)) * dx * dy  # e^(-x-y)
        y += dy
    x += dx

print("P(X < Y): ", integral)

# Tính P(X + Y ≤ 3)
dx = 0.01
dy = 0.01
integral = 0
x = dx
while x <= 3:
    y = dy
    while y <= 3 - x:
        if x > 0 and y > 0:
            integral += (2.718281828459045 ** (-x - y)) * dx * dy  # e^(-x-y)
        y += dy
    x += dx

print("P(X + Y ≤ 3): ", integral)