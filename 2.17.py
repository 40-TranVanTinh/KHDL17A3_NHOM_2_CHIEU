import sympy as sp
def ham_so(x, a):
    return sp.Piecewise((a, (x >= 0) & (x <= 1)), (0, True))

# 1) Xác định a để f(x) là hàm mật độ của một biến ngẫu nhiên liên tục X nào đó
x, a = sp.symbols('x a')
tich_phan = sp.integrate(ham_so(x, a), (x, 0, 1))
gia_tri_a = sp.solve(tich_phan - 1, a)[0]
print(f"Giá trị của a để f(x) là hàm mật độ của một biến ngẫu nhiên liên tục X là: {gia_tri_a}")

# 2) Tính P(1/4 < X < 1/2)
P_X = sp.integrate(ham_so(x, gia_tri_a), (x, 1/4, 1/2))
print(f"P(1/4 < X < 1/2) = {P_X}")

# 3) Xác định hàm phân phối xác suất của X
F = sp.integrate(ham_so(x, gia_tri_a), (x, -sp.oo, x))
print(f"Hàm phân phối xác suất của X là: F(x) = {F}")
