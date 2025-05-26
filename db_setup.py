import sqlite3

conn = sqlite3.connect('stok.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS parcalar")
c.execute("""
CREATE TABLE parcalar (
    parca_no TEXT PRIMARY KEY,
    stok_adet INTEGER,
    fiyat REAL
)
""")

# Örnek veri
c.execute("INSERT INTO parcalar (parca_no, stok_adet, fiyat) VALUES ('ABC123', 42, 12.50)")
c.execute("INSERT INTO parcalar (parca_no, stok_adet, fiyat) VALUES ('XYZ789', 15, 7.30)")
c.execute("INSERT INTO parcalar (parca_no, stok_adet, fiyat) VALUES ('DEF456', 30, 20.00)")

conn.commit()
conn.close()
