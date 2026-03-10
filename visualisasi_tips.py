import pandas as pd
import matplotlib.pyplot as plt

# membaca data
data = pd.read_csv("tips.csv")

# menghitung jumlah laki-laki dan perempuan
gender_count = data['sex'].value_counts()

# menghitung persentase
gender_percent = (gender_count / gender_count.sum()) * 100

# membuat pie chart
plt.figure()
plt.pie(gender_percent, labels=gender_percent.index, autopct='%1.1f%%')

plt.title("Persentase Laki-laki dan Perempuan yang Memberikan Tips")

plt.show()