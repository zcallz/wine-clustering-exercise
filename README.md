# wine-clustering-exercise
---

## 🍷 Wine Clustering with K-Means and PCA

Bu proje, şarapların kimyasal özelliklerine dayanarak benzerliklerine göre gruplandırılmasını (kümelenmesini) amaçlamaktadır. Proje, veri ön işleme, küme sayısını belirleme ve kümeleme sonuçlarını görselleştirme adımlarını içermektedir.

### 📊 Veri Seti
Çalışmada kullanılan veri seti, Kaggle'dan elde edilen ve farklı şarapların kimyasal analiz sonuçlarını içeren bir veri setidir. Veri seti, Alkol, Malic Acid, Proline gibi toplam 13 farklı özellik (feature) barındırmaktadır.

### 🛠️ Proje Adımları ve Uygulanan Metodlar

#### 1. Veri Keşfi ve Ön İşleme
Projenin ilk aşamasında veri setinin temel yapısı incelenmiştir. `df.info()` ve `df.describe()` gibi metotlarla eksik veri, veri tipleri ve temel istatistikler kontrol edilmiştir. Eksik veri olmadığı tespit edilmiştir.
Ek olarak, özellikler arasındaki ilişkileri anlamak için bir **korelasyon matrisi** oluşturulmuştur. Bu matris, `Proline` ve `Alcohol` gibi bazı özellikler arasında yüksek pozitif korelasyonlar olduğunu göstermektedir. Bu analiz, veri yapısını anlamak için önemli bir ilk adımdır.
### Korelasyon Matrisi
![Korelasyon Matrisi](Figure_1.png)


#### 2. Standardizasyon
Veri setindeki özelliklerin farklı ölçeklerde olması, kümeleme algoritmasının performansını etkileyebilir. Bu nedenle, tüm özellikler **`StandardScaler`** kullanılarak standardize edilmiştir. Bu işlem, ortalamayı 0 ve standart sapmayı 1'e getirerek verinin K-Means gibi mesafe tabanlı algoritmalara uygun hale gelmesini sağlar.

#### 3. Optimum Küme Sayısını Belirleme
K-Means algoritması için en uygun küme sayısını belirlemek kritik bir adımdır. Bu projede iki farklı yöntem kullanılmıştır:

* **Elbow Metodu:** Bu metot, farklı küme sayıları için **inertia** (küme içi toplam kareler sapması) değerini görselleştirir. Grafikteki "dirsek" noktasını bularak en uygun küme sayısına karar verilir.
Yukarıdaki grafikte, `k=3`'ten sonra eğimin belirgin bir şekilde azaldığı görülmektedir. Bu da optimum küme sayısının **3** olabileceğini işaret etmektedir.

* **Silhouette Skoru:** Her bir örneğin kendi kümesi içindeki uyumunu ve diğer kümelerden ne kadar ayrıldığını ölçen bir metriktir. 2 ile 10 küme sayısı arasındaki denemelerde en yüksek skor `k=3` ve `k=2` değerleri için elde edilmiştir.
Her iki metodun sonuçları da `k=3` küme sayısının makul bir seçim olduğunu göstermektedir.

### Elbow Metodu
![Elbow Metodu](Figure_2.png)


#### 4. K-Means Kümelemesi ve Görselleştirme
Seçilen 3 küme sayısı ile **K-Means** algoritması standardize edilmiş veri üzerinde çalıştırılmıştır. Kümeleme sonuçlarını iki boyutlu bir düzlemde görselleştirmek için **Principal Component Analysis (PCA)** kullanılmıştır. PCA, veri setinin boyutunu en önemli iki bileşene (PCA 1 ve PCA 2) indirgeyerek veriyi daha kolay yorumlanabilir hale getirir.
Görselleştirme, şarapların üç farklı gruba başarıyla ayrıldığını açıkça göstermektedir. Küme 0, 1 ve 2 olarak etiketlenen bu gruplar, kimyasal özelliklerine göre birbirlerinden belirgin şekilde farklılaşmaktadır.

### Principal Component Analysis (PCA)
![Temel Bileşen Analizi (PCA)](Figure_3.png)

### 🎯 Sonuçlar
Projenin sonunda, her bir kümenin ortalama özellik değerleri incelenerek her kümenin kendine özgü karakteristiği belirlenmiştir. Bu analiz, kümeleme işleminin yalnızca veri noktalarını gruplamakla kalmayıp, aynı zamanda her bir grubun temel özelliklerini ortaya çıkardığını göstermektedir.

Küme 0: Bu kümedeki şaraplar, özellikle yüksek Alcohol, Proline ve Color_Intensity değerleriyle öne çıkmaktadır. Bu özellikler, bu kümedeki şarapların muhtemelen daha güçlü ve yoğun bir profile sahip olduğunu göstermektedir.

Küme 1: Bu gruptaki şaraplar, yüksek Flavanoids, Total_Phenols ve OD280/OD315_of_diluted_wines değerlerine sahiptir. Bu kimyasallar, genellikle kırmızı şaraplarda bulunan tanen ve renk pigmentleri ile ilişkilidir ve bu şarapların daha zengin ve karmaşık bir yapıya sahip olduğunu işaret eder.

Küme 2: Bu küme, diğer gruplara göre daha düşük Flavanoids ve Total_Phenols değerleri sergilerken, Malic_Acid ve Ash_Alcanity değerlerinin daha yüksek olduğu gözlemlenmiştir. Bu profil, genellikle beyaz şarapların karakteristik özelliklerine daha yakındır.

Bu çalışma, gözetimsiz öğrenme (unsupervised learning) tekniklerinin veri setindeki gizli yapıları keşfetmek ve bu yapıları anlamlı gruplara ayırmak için ne kadar güçlü araçlar olduğunu ortaya koymaktadır. Küme ortalamalarını inceleyerek, her bir kümenin ne tür bir şarabı temsil ettiğine dair değerli içgörüler elde edilmiştir.
