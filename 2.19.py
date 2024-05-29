import sympy as sp
def F(thoi_gian):
    return sp.Piecewise((0, thoi_gian <= 0), (2*thoi_gian**3 - 3*thoi_gian**2 + 2*thoi_gian, (thoi_gian > 0) & (thoi_gian <= 1)), (1, thoi_gian > 1))

# 1) Tính xác suất một khách hàng đứng lại tại cửa hàng ít nhất là 20 phút
thoi_gian_gio = 20 / 60
xac_suat = 1 - F(thoi_gian_gio)
print(f"Xác suất một khách hàng đứng lại tại cửa hàng ít nhất là 20 phút là: {xac_suat.evalf()}")

# 2) Xác định hàm mật độ xác suất của X
thoi_gian = sp.symbols('thoi_gian')
f = sp.diff(F(thoi_gian), thoi_gian)
print(f"Hàm mật độ xác suất của X là: f(thoi_gian) = {f}")

# 3) Tính kì vọng, phương sai của X
ki_vong = sp.integrate(thoi_gian*f, (thoi_gian, -sp.oo, sp.oo))
print(f"Kì vọng của X là: E[X] = {ki_vong.evalf()}")

ki_vong_binh_phuong = sp.integrate(thoi_gian**2*f, (thoi_gian, -sp.oo, sp.oo))
phuong_sai = ki_vong_binh_phuong - ki_vong**2
print(f"Phương sai của X là: Var(X) = {phuong_sai.evalf()}")
