import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Giả sử bạn có một danh sách 100 phần tử chứa giá trị 1 và 0
data = pd.read_csv('data/diabetes.csv')
# Tính tần suất xuất hiện của giá trị 1 và 0
labels = ['0', '1']  # Nhãn cho các phần tử
sizes = [np.sum(data['Outcome'] == 0), np.sum(data['Outcome'] == 1)]  # Số lượng phần tử 0 và 1

# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'], startangle=90)
plt.axis('equal')  # Đảm bảo biểu đồ là hình tròn
plt.show()