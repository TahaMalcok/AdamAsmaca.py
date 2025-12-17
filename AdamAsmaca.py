import random
import json
import os
bonus = 0
puan = 0
hata = 0
kelime_liste = []
harfler = []
yaz_kelime = []
doğru_say = 0
kelime_liste_kopya = []
seç_kategori = ""

def kelimeseçici(kelime_liste): #Kategoriyi ve kelimeyi rastgele seçer.
    kategori = ["meyveler", "hayvanlar", "teknoloji"]
    meyveler = ["elma", "armut", "mandalina", "muz", "çilek", "portakal", "ayva", "dağ çileği"]
    hayvanlar = ["aslan", "fil", "balina", "kaplan", "yılan", "köstebek", "su samuru"]
    teknoloji = ["telefon", "bilgisayar", "televizyon", "buzdolabı", "araba", "kulaklık", "şarj aleti"]
    seç_kategori = random.choice(kategori)
    if seç_kategori == "meyveler":
        seç_kelime = random.choice(meyveler)
    elif seç_kategori == "hayvanlar":
        seç_kelime = random.choice(hayvanlar)
    elif seç_kategori == "teknoloji":
        seç_kelime = random.choice(teknoloji)
    seç_kelime1 = seç_kelime.split(" ")
    for i in seç_kelime1:
        for a in i :
            kelime_liste.append(a)
    return seç_kategori, seç_kelime

def adam_çizme(hata): #Kullanıcının oynarken göreceği adamı çizer. Hata sayısına göre adamın şeklini belirler.
    print("--- Yeni Tur ---")
    print()
    print("  +---+")
    print("  |   |")
    if hata >= 1:
        print("  O   |")
        if hata == 2:
            print("  |   |")
            print("      |")
            print("      |")
        elif hata == 3:
            print(" /|   |")
            print("      |")
            print("      |")
        elif hata == 4:
            print(r" /|\  |")
            print("      |")
            print("      |")
        elif hata == 5:
            print(r" /|\  |")
            print(" /    |")
            print("      |")
        elif hata == 6:
            print(r" /|\  |")
            print(r" / \  |")
            print("      |")
        else:
            print("      |")
            print("      |")
            print("      |")
    else:
        print("      |")
        print("      |")
        print("      |")
        print("      |")
    print("=========")

def harf_tahmin(kelime_liste, puan, hata, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya): #Harf tahmini yapmayı sağlar. Girdinin geçerliliğini kontrol eder. Doğruluğunu kontrol eder. Duruma göre puan verir veya hata sayısı arttırır.
    seç_harf = input("Tahmin etmek istediğiniz harfi giriniz:")
    seç_harf = seç_harf.lower()
    if seç_harf in harfler:
        print("Lütfen daha önce girmediğiniz bir harf giriniz.")
        harf_tahmin(kelime_liste, puan, hata, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif 0 == seç_harf.isalpha():
        print("Lütfen bir harf giriniz.")
        harf_tahmin(kelime_liste, puan, hata, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif seç_harf in kelime_liste:
        print("Tebrikler doğru tahmin yaptınız.")
        for i in range(len(kelime_liste)):
            if kelime_liste[i] == seç_harf and yaz_kelime[i] == "_":
                x = kelime_liste.index(seç_harf)
                yaz_kelime[i] = seç_harf
                kelime_liste_kopya.remove(kelime_liste[x])
                doğru_say += 1
                puan += 10
        harfler.append(seç_harf)
        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    else:
        print("Tahmininiz yanlış.")
        hata += 1
        puan -= 5
        harfler.append(seç_harf)
        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)

def işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say): #İşlem bilgilerini alır. İşlemin doğruluğunu kontrol eder. Sonuçlara göre puan verir, bonus puan verir, hata sayısı arttırır.
    işlem = input("Bir işlem seçiniz(Toplama, çıkarma, çarpma, bölme). İptal için iptal yazınız:")
    if işlem == "İptal" or işlem == "iptal":
        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif işlem == "toplama" or işlem == "Toplama":
            sayi1 = input("İşlem için birinci sayıyı giriniz. İptal için iptal yazınız:")
            if sayi1 == "İptal" or sayi1 == "iptal":
                arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
            else:
                sayi2 = input("İşlem için ikinci sayıyı giriniz. İptal için iptal yazınız:")
                if sayi2 == "İptal" or sayi2 == "iptal":
                    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                else:
                    try:
                        sayi1 = float(sayi1)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    try:
                        sayi2 = float(sayi2)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    print(f"Soru: {sayi1} + {sayi2} = ?")
                    tahmin = input("Cevabınız:")
                    sonuç = sayi1 + sayi2
                    try:
                        tahmin = float(tahmin)
                    except:
                        print("Lütfen geçerli değer giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    if tahmin == sonuç:
                        bonus += 1
                        puan += 15
                        aç_harf = random.choice(kelime_liste_kopya)
                        print("Cevap doğru!")
                        print(f"Bonus: {aç_harf} harfi açıldı!")
                        x = kelime_liste.index(aç_harf)
                        kelime_liste_kopya.remove(kelime_liste[x])
                        yaz_kelime[x] = aç_harf
                        doğru_say += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                    else:
                        print("Yanlış cevap girdiniz.")
                        puan -= 10
                        hata += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif işlem == "çıkarma" or işlem == "Çıkarma":
            sayi1 = input("İşlem için birinci sayıyı giriniz. İptal için iptal yazınız:")
            if sayi1 == "İptal" or sayi1 == "iptal":
                arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
            else:
                sayi2 = input("İşlem için ikinci sayıyı giriniz. İptal için iptal yazınız:")
                if sayi2 == "İptal" or sayi2 == "iptal":
                    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                else:
                    try:
                        sayi1 = float(sayi1)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    try:
                        sayi2 = float(sayi2)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    print(f"Soru: {sayi1} - {sayi2} = ?")
                    tahmin = input("Cevabınız:")
                    sonuç = sayi1 - sayi2
                    try:
                        tahmin = float(tahmin)
                    except:
                        print("Lütfen geçerli değer giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    if tahmin == sonuç:
                        bonus += 1
                        puan += 15
                        aç_harf = random.choice(kelime_liste_kopya)
                        print("Cevap doğru!")
                        print(f"Bonus: {aç_harf} harfi açıldı!")
                        x = kelime_liste.index(aç_harf)
                        kelime_liste_kopya.remove(kelime_liste[x])
                        yaz_kelime[x] = aç_harf
                        doğru_say += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                    else:
                        print("Yanlış cevap girdiniz.")
                        puan -= 10
                        hata += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif işlem == "çarpma" or işlem == "Çarpma":
            sayi1 = input("İşlem için birinci sayıyı giriniz. İptal için iptal yazınız:")
            if sayi1 == "İptal" or sayi1 == "iptal":
                arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
            else:
                sayi2 = input("İşlem için ikinci sayıyı giriniz. İptal için iptal yazınız:")
                if sayi2 == "İptal" or sayi2 == "iptal":
                    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                else:
                    try:
                        sayi1 = float(sayi1)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    try:
                        sayi2 = float(sayi2)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    print(f"Soru: {sayi1} x {sayi2} = ?")
                    tahmin = input("Cevabınız:")
                    sonuç = sayi1 * sayi2
                    try:
                        tahmin = float(tahmin)
                    except:
                        print("Lütfen geçerli değer giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    if tahmin == sonuç:
                        bonus += 1
                        puan += 15
                        aç_harf = random.choice(kelime_liste_kopya)
                        print("Cevap doğru!")
                        print(f"Bonus: {aç_harf} harfi açıldı!")
                        x = kelime_liste.index(aç_harf)
                        kelime_liste_kopya.remove(kelime_liste[x])
                        yaz_kelime[x] = aç_harf
                        doğru_say += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                    else:
                        print("Yanlış cevap girdiniz.")
                        puan -= 10
                        hata += 1
                        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif işlem == "bölme" or işlem == "Bölme":
            sayi1 = input("İşlem için birinci sayıyı giriniz. İptal için iptal yazınız:")
            if sayi1 == "İptal" or sayi1 == "iptal":
                arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
            else:
                sayi2 = input("İşlem için ikinci sayıyı giriniz. İptal için iptal yazınız:")
                if sayi2 == "İptal" or sayi2 == "iptal":
                    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                else:
                    try:
                        sayi1 = float(sayi1)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    try:
                        sayi2 = float(sayi2)
                    except:
                        print("Lütfen geçerli değerler giriniz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    if sayi2 == 0:
                        print("Bölen 0 olamaz.")
                        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                    else:
                        print(f"Soru: {sayi1} / {sayi2} = ?")
                        tahmin = input("Cevabınız:")
                        sonuç = sayi1 / sayi2
                        try:
                            tahmin = float(tahmin)
                        except:
                            print("Lütfen geçerli değer giriniz.")
                            işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
                        if tahmin == sonuç:
                            bonus += 1
                            puan += 15
                            aç_harf = random.choice(kelime_liste_kopya)
                            print("Cevap doğru!")
                            print(f"Bonus: {aç_harf} harfi açıldı!")
                            x = kelime_liste.index(aç_harf)
                            kelime_liste_kopya.remove(kelime_liste[x])
                            yaz_kelime[x] = aç_harf
                            doğru_say += 1
                            arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
                        else:
                            print("Yanlış cevap girdiniz.")
                            puan -= 10
                            hata += 1
                            arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    else:
        print("Geçersiz bir değer girdiniz.")
        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)

def ipucu(seç_kategori, bonus, yaz_kelime): #İpucu alma işlemini yapar.
    if bonus >= 1:
        print(f"Kelimenin kategorisi: {seç_kategori}")
        bonus -= 1
    else:
        print("Yeterli bonus puana sahip değilsiniz.")
    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)

def kazanma_kaybetme(hata, kelime_liste, puan, doğru_say): #Oyunun kazanılıp kazanılmadığını kontrol eder.
    if hata == 6:
        print("Oyun kaybedildi.")
        puan -= 20
        kaydetme(puan, bonus)
    elif doğru_say == len(kelime_liste):
        print("Oyun kazanıldı.")
        puan += 50
        kaydetme(puan, bonus)

def kelime_yazma(yaz_kelime): #Kelimenin açılan harflerini yazar. Açılmayan harflerin yerine de çizgi koyar kelimenin uzunluğuna göre.
    for i in yaz_kelime:
        print(i, end= " ")

def kaydetme(puan, bonus): #Oyun bittikten sonra kullanıcıdan isim alıp bilgileri bir json dosyasına kaydeder.
    isim = input("Skorunuzu kaydetmek için bir isim giriniz:")
    oyuncu = {"Isim": isim, "Puan": puan, "Bonus puan": bonus}
    if os.path.exists("scores.json") and os.path.getsize("scores.json") > 0:
        with open("scores.json", "r", encoding="utf-8") as f:
            skorlar = json.load(f)
    else:
        skorlar = []
    skorlar.append(oyuncu)
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(skorlar, f)
    print("Skorunuz scores.json dosyasına kaydedilmiştir.")
    quit()

def arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya): #Oyuncuya kelimeyi , puanını, bonus puanını, hata sayısını gösterir. Seçim yaparak oyuna devam etmesini sağlar. Oyunun toplanıp çalıştığı yerdir.
    print("=== Calc & Hang: İşlem Yap, Harfi Kurtar! ===")
    print()
    adam_çizme(hata)
    print("Kelime:", end = " ")
    kelime_yazma(yaz_kelime)
    print()
    print(f"Tahmin edilen harfler:", end=" ")
    for i in harfler:
        print(i, " ", end=" ", sep="")
    print()
    print(f"Hata sayınız: {hata}")
    print(f"Bonus puan: {bonus}")
    print("Seçenekler: [H]arf tahmini | [İ]şlem çöz | [I]pucu | [Ç]ıkış")
    kazanma_kaybetme(hata, kelime_liste, puan, doğru_say)
    seçim = input("Seçiminiz:")
    if seçim == "H" or seçim == "h":
        harf_tahmin(kelime_liste, puan, hata, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)
    elif seçim == "İ" or seçim == "i":
        işlem_yapma(kelime_liste, bonus, puan, hata, harfler, seç_kategori, kelime_liste_kopya, yaz_kelime, doğru_say)
    elif seçim == "I" or seçim == "ı":
        ipucu(seç_kategori, bonus, yaz_kelime)
    elif seçim == "Ç" or seçim == "ç":
        quit()
    else:
        print("Lütfen geçerli bir seçim yapınız.")
        arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)

def main(kelime_liste, bonus, puan, hata, harfler,  yaz_kelime, doğru_say, kelime_liste_kopya, seç_kategori): #Dosya çalışınca önce kelimeyi seçer sonrasında arayüzü çalıştırır.
    seç_kategori, seç_kelime = kelimeseçici(kelime_liste)
    kelime_liste_kopya = list(kelime_liste)
    if " " in seç_kelime: #Sonradan yaptığım için burda kaldı. Uygun bir yer bulamadım kendisine.
        x = seç_kelime.index(" ")
        yaz_kelime = ["_"] * len(kelime_liste)
        yaz_kelime.insert(x, " ")
    else:
        yaz_kelime = ["_"] * len(kelime_liste)
    arayüz(kelime_liste, bonus, puan, hata, harfler, seç_kategori, yaz_kelime, doğru_say, kelime_liste_kopya)

main(kelime_liste, bonus, puan, hata, harfler, yaz_kelime, doğru_say, kelime_liste_kopya, seç_kategori)