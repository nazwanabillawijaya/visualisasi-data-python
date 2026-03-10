import pandas as pd
import matplotlib.pyplot as plt

# membaca dataset
data = pd.read_csv("SpotifyFeatures.csv")

# menghitung jumlah lagu per genre
genre_count = data['genre'].value_counts().head(10)

# membuat grafik bar
genre_count.plot(kind='bar')

plt.title("Top 10 Genre Lagu Paling Banyak di Spotify Dataset")
plt.xlabel("Genre")
plt.ylabel("Jumlah Lagu")

plt.xticks(rotation=45)

plt.show()
