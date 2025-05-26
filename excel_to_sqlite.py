import sqlite3
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("stoklar.xlsx")

# Veritabanına bağlan
conn = sqlite3.connect("stok.db")
cursor = conn.cursor()

# Tabloyu oluştur (varsa silip yeniden yaz)
cursor.execute("DROP TABLE IF EXISTS parcalar")
cursor.execute("""
CREATE TABLE parcalar (
    parca_no TEXT PRIMARY KEY,
    stok_adet INTEGER,
    fiyat REAL
)
""")

# Verileri ekle veya güncelle
for _, row in df.iterrows():
    cursor.execute(
        "INSERT OR REPLACE INTO parcalar (parca_no, stok_adet, fiyat) VALUES (?, ?, ?)",
        (row["parca_no"], row["stok_adet"], row["fiyat"])
    )

conn.commit()
conn.close()

print("Excel verisi başarıyla veritabanına aktarıldı.")
