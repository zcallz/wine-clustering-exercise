# Gerekli kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Veri Yükleme
df = pd.read_csv("wine-clustering.csv")  # Dosya aynı klasörde olmalı
print("Veri boyutu:", df.shape)
print(df.head())

# 2. Temel Analiz
print("\nVeri bilgisi:")
print(df.info())
print("\nEksik değerler:")
print(df.isnull().sum())
print("\nTanımlayıcı istatistikler:")
print(df.describe())

# 3. Korelasyon Matrisi
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.show()

# 4. Standardizasyon
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 5. Elbow Method
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(K, inertia, 'bo-')
plt.xlabel("Küme Sayısı")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# 6. Silhouette Skoru
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    preds = kmeans.fit_predict(scaled_data)
    score = silhouette_score(scaled_data, preds)
    print(f"Küme sayısı: {k} => Silhouette Skoru: {score:.3f}")

# 7. PCA ile 2 Boyuta İndirgeme ve Görselleştirme
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

kmeans = KMeans(n_clusters=3, random_state=42)  # Örnek: 3 küme
clusters = kmeans.fit_predict(scaled_data)

plt.figure(figsize=(8,6))
sns.scatterplot(x=pca_data[:,0], y=pca_data[:,1], hue=clusters, palette="viridis")
plt.title("Kümeleme Sonucu (PCA 2D)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend(title="Küme")
plt.grid(True)
plt.show()

# 8. Küme İstatistikleri
df["Cluster"] = clusters
print("\nKüme Ortalamaları:")
print(df.groupby("Cluster").mean())
