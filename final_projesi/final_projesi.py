import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#csv dosyasını okuttum
veriler = pd.read_csv("ETH_USD_6ay.csv")

# verileri satır ve sütun şeklinde dilimledim
x = veriler.iloc[:, 0:1]
y = veriler.iloc[:, 1:]

# Numpy dizisine dönüştürdüm
X = x.values
Y = y.values

# Numpy dizisindeki verileri grafik oluşturup, grafiğe aktardım
plt.scatter(X,Y,color="orange")
plt.xlabel("Gün")
plt.ylabel("Fiyat")
plt.title("Fiyat Değişim Grafiği")
plt.show()

# doğrusal artış çizgisini tanımlayıp X ve Y değişkenlerini fit fonksiyonu ile eğittim
linreg = LinearRegression()
linreg.fit(X, Y)

# doğrusal artış çizgisini grafiğe aktardım.
plt.scatter(X, Y, color="orange")
plt.plot(x, linreg.predict(X), color="green")
plt.xlabel("Gün")
plt.ylabel("Fiyat")
plt.title("Lineer Regresyon")
plt.show()

# grafikteki veriler ile doğrusal çizgideki kesişim noktalarına göre tahmin yapıyor (çizgi doğrusal olduğu için pek yararlı olmadı doğru tahmin etme olasığı düşük)
print("Lineer Regresyon Tahmin:", linreg.predict([[230]]))

# polinomsal çizgide açıyı en tutarlı olan 7 olarak belirledim ve fit fonksiyonu ile eğittim (iniş ve çıkışları gösterdiği için doğruluk payı daha yüksek)
polreg = PolynomialFeatures(degree=7)
xpol = polreg.fit_transform(X)
linreg = LinearRegression()
linreg.fit(xpol, y)

# polinomsal artış çizgisini grafiğe aktardım
plt.scatter(X, Y, color="orange")
plt.plot(X, linreg.predict(polreg.fit_transform(X)), color="green")
plt.xlabel("Gün")
plt.ylabel("Fiyat")
plt.title("Polinomsal Regresyon (Derece:7)")
plt.show()

# grafikteki veriler ile polinomsal çizgideki kesişim noktalarına göre tahmin yapıyor
print("Polinomsal Regresyon Tahmin:", linreg.predict(polreg.fit_transform([[230]])))

# tahminleri csv dosyasındaki verilere göre yapmaktadır. Verileri kullanarak eğitim gerçekleşiyor daha sonra o verilere göre tahmin yapıyor.
# Örnek olarak 6 aylık verileri gösteren csv dosyasını import ettiğimizde 6.ayın son gününe kadar veriler bulunmakta. Bu tahmini 7.ayın ilk gününe göre yapmaktadır. 
