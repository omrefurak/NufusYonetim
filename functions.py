from insan import insan
import csv

def VeriTabaniListele(DosyaAdi):
    Dosya=open(DosyaAdi,"r",encoding="utf-8")
    kisi_list=[]
    for kisi in Dosya:
        kisi_list.append(kisi.strip().split(","))
    for kisi in kisi_list:
        print(kisi)
    Dosya.close()

def YeniKayitEkle(DosyaAdi):
    list = []
    insan.KimlikNo = input("Kişinin kimlik nosunu giriniz:")
    if insan.KimlikNo.isnumeric():
        if int(insan.KimlikNo) > 10000000000 and int(insan.KimlikNo) < 99999999999 and (int(insan.KimlikNo) % 2 ==0):
            insan.Adi = input("Kişinin adını giriniz:")
            insan.Soyadi = input("Kişinin soyadını giriniz:")
            insan.BabaAdi = input("Kişinin baba adını giriniz:")
            insan.AnneAdi = input("Kişinin anne adını giriniz:")
            insan.DogumYeri = input("Kişinin doğum yerini giriniz:")
            insan.MedeniDurumu = input("Kişinin medeni durumunu giriniz:")
            insan.KanGrubu = input("Kişinin kan grubunu giriniz:")
            insan.KutukSehir = input("Kişinin kütük ilini giriniz:")
            insan.KutukIlce = input("Kişinin kütük ilçesini giriniz:")
            insan.ikametgahSehir = input("Kişinin ikamet ettiği ili giriniz:")
            insan.ikametgatIlce = input("Kişinin ikamet ettiği ilçeyi giriniz:")


            list.append(insan.KimlikNo)
            list.append(insan.Adi)
            list.append(insan.Soyadi)
            list.append(insan.BabaAdi)
            list.append(insan.AnneAdi)
            list.append(insan.DogumYeri)
            list.append(insan.MedeniDurumu)
            list.append(insan.KanGrubu)
            list.append(insan.KutukSehir)
            list.append(insan.KutukIlce)
            list.append(insan.ikametgahSehir)
            list.append(insan.ikametgatIlce)

        else:
            exit("Lütfen 11 haneli geçerli bir kimlik no giriniz")
    else:
        exit("Lütfen 11 haneli geçerli bir kimlik no giriniz")
    f = open(DosyaAdi, "a", encoding="utf-8")
    f.write(",".join(list))
    print("{} Kimlik nolu kişi sisteme kaydedildi.".format(insan.KimlikNo))
    f.write("\n")
    f.close()

def KisiyiSil(DosyaAdi):
    Dosya = open(DosyaAdi, "r", encoding="utf-8")
    kisi_list = []
    for kisi in Dosya:
        kisi_list.append(kisi.strip().split(","))

    for satir in kisi_list:
        print(satir)
    silinecek = input("Silinecek kişininin kimlik nosunu giriniz:")
    a = silinecek
    for satir in kisi_list:
        if silinecek in kisi_list[0]:
            kisi_list.remove(satir)
            print("Kişi silindi.")
            break
    if silinecek not in kisi_list[0]:
        print("{} Kimlik nolu kişi sistemde bulunmamaktadır.".format(a))

    Dosya.close()

    Dosya = open(DosyaAdi, "w", encoding="utf-8")
    kaydet = []
    for kisi in kisi_list:
        kaydet.append(",".join(kisi) + "\n")
    Dosya.writelines(kaydet)
    Dosya.close()

def KisiGuncelleme(DosyaAdi):
    kisi_list = []
    Dosya = open(DosyaAdi, "r", encoding="utf-8")
    for kisi in Dosya:
        kisi_list.append(kisi.strip().split(","))
    for satir in kisi_list:
        print(satir)
    degisecek =input("Güncellenecek kişininin kimlik nosunu giriniz:")
    b = degisecek
    for satir in kisi_list:
        if degisecek == satir[0]:
            print("Ad için 1, Soyad için 2, Baba Adı için 3, Anne Adı için 4, Doğum Yeri için 5, "
                  "Medeni Durum için 6, Kan grubu için 7, Kütük ili için 8, Kütük ilçe için 9,"
                  "İkamet ili 10, İkamet ilçesi için 11")
            guncellenecek = int(input("Güncellenecek özelliği giriniz:"))
            guncelleme = input("Güncellemeyi yazınız:")
            satir[guncellenecek] = guncelleme
            print("Kişi güncellendi.")

    if degisecek not in kisi_list[0]:
        print("{} Kimlik nolu kişi sistemde bulunmamaktadır.".format(b))

    Dosya = open(DosyaAdi, "w", encoding="utf-8")
    kaydet = []
    for kisi in kisi_list:
        kaydet.append(",".join(kisi) + "\n")
    Dosya.writelines(kaydet)
    Dosya.close()

def KisiArama(DosyaAdi):
    Dosya=open(DosyaAdi,"r",encoding="utf-8")
    kisi_list = []
    for kisi in Dosya:
        kisi_list.append(kisi.strip().split(","))
    for satir in kisi_list:
        print(satir[0])
    ara = input("Aramak istediğiniz kişinin kimlik nosunu giriniz:")
    c = ara
    search=False
    row=0
    for satir in range(0,len(kisi_list)):
        if(ara==kisi_list[satir][0]):
            search=True
            row=satir
    if(search):
        print(kisi_list[row])
    else:
        print("{} Kimlik nolu kişi bulunamadı".format(c))
    Dosya.close()



