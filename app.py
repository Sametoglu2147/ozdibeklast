from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def stok_sorgula(parca_no):
    conn = sqlite3.connect('stok.db')
    c = conn.cursor()
    c.execute("SELECT stok_adet, fiyat FROM parcalar WHERE parca_no=?", (parca_no,))
    result = c.fetchone()
    conn.close()
    return result  # (stok_adet, fiyat)

@app.route('/', methods=['GET', 'POST'])
def index():
    stok = None
    if request.method == 'POST':
        parca_no = request.form['parca_no']
        stok = stok_sorgula(parca_no)
    return render_template('index.html', stok=stok)

@app.route('/guncelle', methods=['GET', 'POST'])
def guncelle():
    mesaj = None
    if request.method == 'POST':
        parca_no = request.form['parca_no']
        yeni_adet = request.form['stok_adet']
        yeni_fiyat = request.form['fiyat']
        conn = sqlite3.connect('stok.db')
        c = conn.cursor()
        c.execute("UPDATE parcalar SET stok_adet=?, fiyat=? WHERE parca_no=?", (yeni_adet, yeni_fiyat, parca_no))
        conn.commit()
        conn.close()
        mesaj = f"{parca_no} için stok {yeni_adet}, fiyat {yeni_fiyat} olarak güncellendi."
    return render_template('guncelle.html', mesaj=mesaj)

if __name__ == '__main__':
    app.run(debug=True)
