import math

# Các thông số
BNN_X = 2.2
sigma_X = 0.4
BNN_Y = 2.5
sigma_Y = 0.6
a = -0.5

# Trung bình và độ lệch chuẩn của tổng thời gian
BNN_T = BNN_X + BNN_Y
sigma_T = math.sqrt(sigma_X**2 + sigma_Y**2 - 2 * a * sigma_X * sigma_Y)

# Giá trị 5 giờ
T = 5

# Tính z-score
z = (T - BNN_T) / sigma_T

# Tính xác suất
def standard_normal_cdf(x):
    """Tính hàm phân phối chuẩn tiêu chuẩn (CDF) tại x."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

p = 1 - standard_normal_cdf(z)
print(f"Xác suất tổng thời gian học và giải trí lớn hơn 5 giờ: {p:.4f}")

#b
import math

# Các thông số
BNN_X = 2.2
sigma_X = 0.4
BNN_Y = 2.5
sigma_Y = 0.6
a= -0.5

# Trung bình và độ lệch chuẩn của tổng thời gian
BNN_T = BNN_X + BNN_Y
sigma_T = math.sqrt(sigma_X**2 + sigma_Y**2 - 2 * a * sigma_X * sigma_Y)

# Giá trị 0 giờ (vì thời gian học không thể âm)
T = 0

# Tính z-score
z = (T - BNN_T) / sigma_T

# Tính xác suất
def standard_normal_cdf(x):
    """Tính hàm phân phối chuẩn tiêu chuẩn (CDF) tại x."""
    return (1 + math.erf(x / math.sqrt(2.0))) / 2.0

p = 1 - standard_normal_cdf(z)
print(f"Xác suất thời gian học lớn hơn thời gian giải trí: {p:.4f}")
