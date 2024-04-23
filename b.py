import sqlite3

def jaccard(metin1, metin2):
    # Metinleri kelimelere ayır
    kelimeler1 = set(metin1.split())
    kelimeler2 = set(metin2.split())
    
    # Kümelerin kesişimini ve birleşimini hesapla
    kesisim = len(kelimeler1.intersection(kelimeler2))
    birlesim = len(kelimeler1.union(kelimeler2))
    
    # Jaccard benzerlik katsayısını hesapla
    jaccard_katsayisi = kesisim / birlesim if birlesim != 0 else 0
    
    return jaccard_katsayisi

# SQLite veritabanı dosyasını oluştur
conn = sqlite3.connect('metinler.db')

# Bir tablo oluştur
conn.execute('''CREATE TABLE IF NOT EXISTS metinler
             (id INTEGER PRIMARY KEY,
             metin TEXT NOT NULL)''')

# İlk metni ekle
conn.execute("INSERT INTO metinler (metin) VALUES (?)", ("araba ile gelirken kaza yaptık",))

# İkinci metni ekle
conn.execute("INSERT INTO metinler (metin) VALUES (?)", ("araba ile",))

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()

# Metinleri veritabanından çek
cursor = conn.execute("SELECT metin FROM metinler")
metinler = [row[0] for row in cursor]

# Jaccard benzerlik katsayısını hesapla
benzerlik = jaccard(metinler[0], metinler[1])

# Benzerlik durumunu ekrana yazdır
print("Jaccard Benzerlik Katsayısı:", benzerlik)

# Benzerlik durumunu dosyaya yazdır
with open("benzerlik_durumu.txt", "w") as dosya:
    if benzerlik > 0.5:
        dosya.write("Metinler birbiriyle benzerdir.")
    else:
        dosya.write("Metinler birbirinden farklıdır.")

# Bağlantıyı kapat
conn.close()
