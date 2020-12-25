import sqlite3
from tkinter import *
import time
import datetime


class MesajListesi:
    def __init__(self):
        self.baglanti = sqlite3.connect("MesajListesi.db")
        if not self.baglanti:
            print("HATA: Veritabanına Bağlanılamadı!")
            exit()
        else:
            self.komut = self.baglanti.cursor()

        self.db_kurulum()

        self.tk = Tk()
        self.tk.title("proje_05")
        self.fontStilim = ("arial", 16)
        self.tk.geometry("800x930+600+300")
        self.frame1 = Frame(self.tk)
        self.frame1.pack()
        self.frame2 = Frame(self.tk)
        self.frame2.pack()
        self.frame3 = Frame(self.tk)
        self.frame3.pack()
        self.frame4 = Frame(self.tk)
        self.frame4.pack()
        self.frame5 = Frame(self.tk)
        self.frame5.pack()
        self.frame6 = Frame(self.tk)
        self.frame6.pack()
        self.frame7 = Frame(self.tk)
        self.frame7.pack()
        self.frame8 = Frame(self.tk)
        self.frame8.pack()
        self.frame9 = Frame(self.tk)
        self.frame9.pack()
        self.frame10 = Frame(self.tk)
        self.frame10.pack()
        self.frame11 = Frame(self.tk)
        self.frame11.pack()
        self.frame12 = Frame(self.tk)
        self.frame12.pack()
        self.etiket1 = Label(self.frame1, text="Ad Soyad:", font=self.fontStilim)
        self.etiket1.pack(pady="20", side=LEFT)
        self.satir1 = Entry(self.frame1, font=self.fontStilim)
        self.satir1.pack(side=RIGHT)
        self.etiket2 = Label(self.frame2, text="      Mesaj:", font=self.fontStilim)
        self.etiket2.pack(pady="10", side=LEFT)
        self.satir2 = Entry(self.frame2, font=self.fontStilim)
        self.satir2.pack(side=RIGHT)
        self.dugme1 = Button(self.frame3, text="Kaydet", font=self.fontStilim, command=self.db_ekle)
        self.dugme1.pack(pady="5", ipadx="58")
        self.satir3 = Listbox(self.frame4, font=self.fontStilim, width=60, height=9)
        self.satir3.pack(pady="10", side=RIGHT)
        self.dugme2 = Button(self.frame5, text="Listele", font=self.fontStilim, command=self.db_listele)
        self.dugme2.pack(pady="5", ipadx="64")
        self.dugme2nokta2 = Button(self.frame5, text="Temizle", font=self.fontStilim, command=self.temizle)
        self.dugme2nokta2.pack(pady="5", ipadx="60")
        self.etiket5 = Label(self.frame5, text="        Silinecek Satır No:", font=self.fontStilim)
        self.etiket5.pack(pady="10", side=LEFT)
        self.satir5 = Entry(self.frame5, font=self.fontStilim)
        self.satir5.pack(side=RIGHT)
        self.dugme3 = Button(self.frame6, text="Sil", font=self.fontStilim, command=self.db_sil)
        self.dugme3.pack(pady="5", ipadx="82")
        self.etiket6 = Label(self.frame7, text="Güncellenecek Satır No:", font=self.fontStilim)
        self.etiket6.pack(pady="10", side=LEFT)
        self.satir6 = Entry(self.frame7, font=self.fontStilim)
        self.satir6.pack(side=RIGHT)
        self.etiket7 = Label(self.frame8, text="               Yeni AdSoyad:", font=self.fontStilim)
        self.etiket7.pack(pady="10", side=LEFT)
        self.satir7 = Entry(self.frame8, font=self.fontStilim)
        self.satir7.pack(side=RIGHT)
        self.etiket8 = Label(self.frame9, text="                    Yeni Mesaj:", font=self.fontStilim)
        self.etiket8.pack(pady="10", side=LEFT)
        self.satir8 = Entry(self.frame9, font=self.fontStilim)
        self.satir8.pack(side=RIGHT)
        self.dugme4 = Button(self.frame10, text="Güncelle", font=self.fontStilim, command=self.db_guncelle)
        self.dugme4.pack(pady="5", ipadx="55")
        self.etiket9 = Label(self.frame11, text="              Aranan Satır No:", font=self.fontStilim)
        self.etiket9.pack(pady="10", side=LEFT)
        self.satir9 = Entry(self.frame11, font=self.fontStilim)
        self.satir9.pack(side=RIGHT)
        self.dugme5 = Button(self.frame12, text="Ara", font=self.fontStilim, command=self.db_ara)
        self.dugme5.pack(pady="5", ipadx="80")
        self.tk.mainloop()

    def db_ekle(self):
        _adsoyad = self.satir1.get()
        _mesaj = self.satir2.get()
        tarih=time.time()
        saat=str(datetime.datetime.fromtimestamp(tarih).strftime("%d/%m/%Y %H.%M tarihinde eklendi."))

        if _adsoyad != "" and _mesaj != "":
            self.komut.execute("INSERT INTO kisiler (kisi_adsoyad,kisi_mesaj,saat) values (?,?,?)", (_adsoyad, _mesaj,saat))
            self.baglanti.commit()
            self.satir1.delete(0, END)
            self.satir2.delete(0, END)
            self.satir1.focus()


    def db_kurulum(self):
        self.komut.execute("""
            CREATE TABLE IF NOT EXISTS kisiler 
            (satirNo INTEGER PRIMARY KEY AUTOINCREMENT,
            kisi_adsoyad TEXT, 
            kisi_mesaj TEXT,
            saat TEXT)
        """)
        self.baglanti.commit()

    def db_listele(self):
        self.satir3.delete(0, END)
        for kayitlar in self.komut.execute('SELECT * FROM kisiler'):
            self.satir3.insert(END, kayitlar)

    def db_sil(self):
        satirNumarasi=self.satir5.get()
        self.komut.execute("DELETE FROM kisiler WHERE satirNo=?", (satirNumarasi,))
        self.satir5.delete(0, END)
        self.baglanti.commit()

    def db_guncelle(self):
        satirNumarasi=self.satir6.get()
        yeniAdSoyad=self.satir7.get()
        yeniMesaj=self.satir8.get()
        self.komut.execute("UPDATE kisiler SET  kisi_adsoyad=?, kisi_mesaj=? WHERE satirNo=?", (yeniAdSoyad,yeniMesaj,satirNumarasi))
        self.satir6.delete(0, END)
        self.satir7.delete(0, END)
        self.satir8.delete(0, END)
        self.baglanti.commit()

    def db_ara(self):
        satirAra = self.satir9.get()
        self.satir3.delete(0, END)
        #Satır numarası ile arama yapma #self.komut.execute("SELECT * FROM kisiler WHERE kisi_adsoyad=? OR kisi_mesaj=?", (satirAra,satirAra))
        self.komut.execute("SELECT * FROM kisiler WHERE kisi_adsoyad LIKE ? OR kisi_mesaj LIKE ?", ('%'+satirAra+'%','%'+satirAra+'%'))
        for kayitlar in self.komut.fetchall():
            self.satir3.insert(END, kayitlar)
            self.satir9.delete(0, END)

        self.baglanti.commit()

    def temizle(self):
        self.satir3.delete(0, END)

MesajListesi()
