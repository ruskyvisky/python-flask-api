# Dockerfile

# Resmi Python 3.11 slim (küçük boyutlu) imajını temel al
FROM python:3.11-slim

# Uygulama kodunun bulunacağı dizini ayarla
WORKDIR /app

# requirements.txt dosyasını container'a kopyala
COPY requirements.txt .

# Gerekli Python kütüphanelerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Tüm proje dosyalarını (app.py vb.) container'a kopyala
COPY . .

# Flask uygulamasının çalışacağı portu belirt (dokümantasyon amaçlı)
EXPOSE 5000

# Container başladığında çalışacak komut
# Gunicorn gibi bir üretim sunucusu kullanmak daha iyi olsa da, başlangıç için basitçe Python ile çalıştıralım:
CMD ["python", "app.py"]