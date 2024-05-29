#Bài 4.5: cho hai biến ngẫu nhiên X và Y độc lập có phân phối đều trên {a;b}. Xác định hàm phân phối của Z=X+Y

def probability_Z(a, b, z):
    if z < 2 * a or z > 2 * b:
        return 0.0
    else:
        return 1 / (b - a) ** 2
#ví dụ: 
a = 1
b = 5
# Giá trị Z cần tính hàm phân phối
z_value = 7
result = probability_Z(a, b, z_value)
print(f"Hàm phân phối của Z tại giá trị {z_value} là: {result:.4f}")




