import math

# Hàm mật độ xác suất của X
def f_X(x, a, b):
    if x >= a and x <= b:
        return 1/(b-a)
    else:
        return 0

# Hàm mật độ xác suất của Y = e^X
def f_Y(y, a, b):
    if y >= math.exp(a) and y <= math.exp(b):
        return 1/((b-a)*y)
    else:
        return 0

# Hàm mật độ xác suất của Z = ln(X)
def f_Z(z, a, b):
    if z >= math.log(a) and z <= math.log(b):
        return (1/(b-a)) * math.exp(z)
    else:
        return 0

# Kiểm tra kết quả
a = 2  
b = 5  

x_value = 2.5  # Giá trị x
y_value = math.exp(x_value)  # Giá trị y
z_value = math.log(x_value)  # Giá trị z

print("f_X(x) =", f_X(x_value, a, b))
print("f_Y(y) =", f_Y(y_value, a, b))
print("f_Z(z) =", f_Z(z_value, a, b))