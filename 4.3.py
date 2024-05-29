# Bảng phân phối xác suất chung cho (X, Y)
bpp = {
(1, 1): 0.15,
(2, 1): 0.20,
(3, 1): 0.10,
(1, 2): 0.35,
(2, 2): 0.05,
(3, 2): 0.15
}

# Tính hàm mật độ biên của X và Y
def ham_mat_do_bien(joint_dist):
    f_X = {x: 0 for x in range(1, 4)}
    f_Y = {y: 0 for y in range(1, 3)}

    for (x, y), p in joint_dist.items():
        f_X[x] += p
        f_Y[y] += p

    return f_X, f_Y

# Kiểm tra sự độc lập giữa X và Y
def doc_lap(f_X, f_Y, joint_dist):
    for x in f_X:
        for y in f_Y:
            if (x, y) in joint_dist:
                if joint_dist[(x, y)] != f_X[x] * f_Y[y]:
                    return False
    return True

# Tính xác suất có điều kiện P(X=1|Y=2)
def xac_suat(joint_dist, f_Y):
    return joint_dist[(1, 2)] / f_Y[2]

# Thực hiện tính toán
f_X, f_Y = ham_mat_do_bien(bpp)
independence = doc_lap(f_X, f_Y, bpp)
conditional_prob = xac_suat(bpp, f_Y)

# In kết quả
print("Hàm mật độ biên của X:", f_X)
print("Hàm mật độ biên của Y:", f_Y)
print("X và Y độc lập:", independence)
print("P(X=1|Y=2):", conditional_prob)
