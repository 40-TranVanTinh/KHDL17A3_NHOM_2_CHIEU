def calculate_k():
    
    integral = 0
    for x in range(0, 2):
        for y in range(0, 2):
            integral += x * y
    k = 6/ integral
    return k

k_value = calculate_k()
print(f"Giá trị của tham số k là: {k_value}")
#b
def calculate_fx(x):
    # Tính hàm mật độ xác suất biên của biến X
    return (k / 2) * x**2

def calculate_fy(y):
    # Tính hàm mật độ xác suất biên của biến Y
    return (k / 2) * y**2

def calculate_fz(z):
    # Hàm mật độ xác suất biên của biến Z
    return 1


k = 6

# Test với giá trị x, y, z bất kỳ
x_value = 0.4
y_value = 0.6
z_value = 0.9

print(f"f_X({x_value}) = {calculate_fx(x_value)}")
print(f"f_Y({y_value}) = {calculate_fy(y_value)}")
print(f"f_Z({z_value}) = {calculate_fz(z_value)}")
#c
def calculate_f_X_given_Y(x, y):
    # Tính hàm mật độ điều kiện của biến X biết Y = y
    return (k * x * y) / (k * y)

def calculate_f_Y_given_XZ(y, x, z):
    # Tính hàm mật độ điều kiện của biến Y biết X = x và Z = z
    return (k * x * y * z) / (k * x * z)



# Test với giá trị x, y, z bất kỳ
x_value = 1
y_value = 2
z_value = 4

print(f"f_X|Y({x_value}|{y_value}) = {calculate_f_X_given_Y(x_value, y_value)}")
print(f"f_Y|XZ({y_value}|{x_value}, {z_value}) = {calculate_f_Y_given_XZ(y_value, x_value, z_value)}")


