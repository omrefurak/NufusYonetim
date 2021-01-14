import functions

DosyAd="Nufus Yonetim Sistemi.csv"
Dosya = open("Nufus Yonetim Sistemi.csv", "r", encoding="utf-8")
kisi_list = []
for kisi in Dosya:
    kisi_list.append(kisi.strip().split(","))
print("Veri tabanındaki kişi sayısı:",len(kisi_list))
Dosya.close()
while True:
    print("Lütfen yapmak istediğiniz işlemi seçiniz \n"
          "0. Çıkış \n"
          "1. Yeni Kayıt\n"
          "2. Veri Tabanı Listeleme\n"
          "3. Kişi Silme\n"
          "4. Kişi Güncelleme\n"
          "5. Kişi Arama\n")
    islev=input("Seçiminiz: ")
    if islev not in ["0","1","2","3","4","5"]:
        print("Hatalı giriş !!!")
    elif islev=="0":
        print("Çıkış seçildi")
        exit(0)
    elif islev=="1":
        functions.YeniKayitEkle(DosyAd)
    elif islev=="2":
        functions.VeriTabaniListele(DosyAd)
    elif islev=="3":
        functions.KisiyiSil(DosyAd)
    elif islev=="4":
        functions.KisiGuncelleme(DosyAd)
    elif islev=="5":
        functions.KisiArama(DosyAd)