# 🚀 Termux OSINT Aracı
## 👤 Kullanıcı Arama | 🌍 IP Sorgu | 🌐 Domain Lookup


## ✨ Başlarken - Kurulum Adımları

# 1. Python kurulumu
pkg install python -y


# 2. Gerekli Python kütüphanelerini kur
pip install requests                   # HTTP istekleri için

pip install rich                       # Renkli terminal çıktısı

pip install dnspython                  # DNS kayıtları çekme

pip install python-whois               # Domain WHOIS bilgisi

# 3. OSINT aracını başlat
python osint.py
