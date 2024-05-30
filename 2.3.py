# Xác suất đỗ của từng vòng thi
p1 = 0.8  
p2 = 0.6  
p3 = 0.55 

p_all = p1 * p2 * p3
print("Xác suất để thí sinh đỗ cả ba vòng là:", p_all)

# Lập bảng phân phối xác suất cho số vòng thi đỗ
probabilities = [0, 0, 0, 0]  # Số vòng từ 0 đến 3
probabilities[3] = p_all  
probabilities[2] =  p1*p2*(1-p3)+(1-p1)*p2*p3+p1*(1-p2)*p3 
probabilities[1] = (1-p1)*p2*(1-p3)+(1-p1)*(1-p2)*p3+p1*(1-p2)*(1-p3)
probabilities[0] = (1-p1)*(1-p2)*(1-p3) 

# In bảng phân phối xác suất
print("\nBảng phân phối xác suất cho số vòng thi đỗ:")
print("Số vòng thi đỗ | Xác suất")
for i, prob in enumerate(probabilities):
    print(f"{i}                | {prob}")

# Tính kỳ vọng và phương sai của số vòng thi đỗ
exp = sum(prob * i for i, prob in enumerate(probabilities))
var = sum(prob * (i - exp) ** 2 for i, prob in enumerate(probabilities))

print("\nKỳ vọng của số vòng thi đỗ là:", exp)
print("Phương sai của số vòng thi đỗ là:", var)