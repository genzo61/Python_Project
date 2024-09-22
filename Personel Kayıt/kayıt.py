import sqlite3

def listele():
    veriler=baglanti.cursor().execute("SELECT * FROM perkayıt")
    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()
def ekle(persicilno,per_ad_soyad,permaas, peryıl,perdepatman):
    con=baglanti.cursor()
    con.execute("insert into perkayıt values(?,?,?,?,?)",(persicilno,per_ad_soyad,permaas,peryıl,perdepatman))
    baglanti.commit()
    baglanti.close()
    print("kayıt işlemi başarılı bir şekilde gerçekleştirildi.")
def sil(sn):
    con = baglanti.cursor()
    con.execute("delete from perkayıt where persıcılno = ?",(sn,))
    baglanti.commit()
    baglanti.close()
    print("kayıt başarılı bir şekilde silindi.")







menü="""
************************
1. kayıt ekle

2.kayıtları listele

3.kayıt sil

************************
"""

baglanti = sqlite3.connect("py personel kayıt.db")

while True:
 if(baglanti):
    print("Bağlantı Başarılı...")
 else:
    print("Bağlantı yok...")
 print(menü)
 print("lütfen işlem seçiniz.")
 işlem=int(input("işlem seçiniz : "))

 if(işlem==1):
    persicilno=int(input("personel sicil no yu giriniz : "))
    per_ad_soyad=input("personel ad ve soyad giriniz : ")
    permaas=int(input("personel maaş giriniz : "))
    peryıl=int(input("personel yıl giriniz : "))
    perdepatman=input("personel departmanı giriniz : ")
    ekle(persicilno,per_ad_soyad,permaas, peryıl,perdepatman)
 elif(işlem==2):
    listele()
 elif(işlem==3):
    sn=int(input("silinecek personelin sicil nosunu giriniz : "))
    sil(sn)
 else:
    print("geçersiz işlem...")