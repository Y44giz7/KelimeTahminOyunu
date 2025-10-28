import tkinter as tk
from tkinter import messagebox
import random

# Kelime listesi
kelimeler = ["python", "programlama", "bilgisayar", "yazılım", "internet", 
             "uygulama", "geliştirici", "teknoloji", "algoritma", "kodlama","elma","masa","gökyüzü","deniz","kalem","kitap","ışık","bilgisayar","fare","kulaklık","oyun","zaman","kedi","köpek","tahta","çanta","telefon","kablolu","gözlük","araba","sandalye","göl","rüzgar","bulut","ışın","dünya","gezegen","not","kağıt","renk","ışıldak","oyuncu","yazılım","kod","fikir","hayal","yol","şehir","orman","çiçek","bina","taş","dağ","nehir","kule","ev","kapı","pencere","duvar","kablo","radyo","film","dizi","kamera","fotoğraf","ses","mikrofon","hoparlör","televizyon","oyuncak","bebek","robot","yıldız","güneş","ay","gezinti","uçak","tren","gemi","balık","ağaç","yaprak","yağmur","kar","rüya","yastık","battaniye","yatak","mutfak","tabak","çatal","bıçak","kaşık","bardak","su","kahve","çay","şeker","ekmek","peynir","zeytin","yumurta","bal","reçel","kütüphane","kitaplık","defter","silgi","kalemtıraş","okul","sınıf","öğrenci","öğretmen","sınav","ders","ödev","not","kural","tahta","bilgi","internet","video","site","sayfa","program","uygulama","ekran","fare","klavye","buton","ayar","dosya","klasör","belge","yazı","satır","kod","komut","pencere","bağlantı","oyun","harita","görev","karakter","seviye","puan","silah","zırh","enerji","kalkan","bölüm","can","zamanlayıcı","yarış","skor","ekip","arkadaş","düşman","zafer","yenilgi","puan","ödül","kutlama","müzik","ses","melodi","ritim","not","enstrüman","gitar","piyano","davul","keman","bas","flüt","şarkı","söz","melodi","klip","konser","festival","bilet","seyirci","sahne","ışık","renk","efekt","duman","parıltı","kostüm","maske","karakter","hikaye","senaryo","oyuncu","yönetmen","kamera","çekim","film","kurgu"]

class KelimeTahminOyunu:
    def __init__(self, master):
        self.master = master
        self.master.title("Kelime Tahmin Oyunu")
        self.master.geometry("600x400")
        
        self.kelime = ""
        self.gizli_kelime = ""
        self.kalan_hak = 5
        
        # Arayüz elemanları
        self.label_kelime = tk.Label(master, text="", font=('Arial', 24))
        self.label_kelime.pack(pady=20)
        
        self.label_ipucu = tk.Label(master, text="Bir harf tahmin edin:")
        self.label_ipucu.pack()
        
        self.tahmin_entry = tk.Entry(master)
        self.tahmin_entry.pack(pady=10)
        
        self.tahmin_button = tk.Button(master, text="Tahmin Et", command=self.tahmin_yap)
        self.tahmin_button.pack(pady=10)
        
        self.kalan_hak_label = tk.Label(master, text=f"Kalan Hak: {self.kalan_hak}")
        self.kalan_hak_label.pack(pady=10)
        
        self.yeni_oyun_button = tk.Button(master, text="Yeni Oyun", command=self.yeni_oyun)
        self.yeni_oyun_button.pack(pady=10)
        
        # İlk oyunu başlat
        self.yeni_oyun()
        
    def yeni_oyun(self):
        self.kelime = random.choice(kelimeler)
        gizlenecek_index = random.randint(0, len(self.kelime)-1)
        self.gizli_kelime = self.kelime[:gizlenecek_index] + "_" + self.kelime[gizlenecek_index+1:]
        self.kalan_hak = 5
        self.label_kelime.config(text=self.gizli_kelime)
        self.kalan_hak_label.config(text=f"Kalan Hak: {self.kalan_hak}")
        self.tahmin_entry.delete(0, tk.END)
    
    def tahmin_yap(self):
        tahmin = self.tahmin_entry.get().lower()
        
        if len(tahmin) != 1:
            messagebox.showwarning("Uyarı", "Lütfen sadece bir harf girin!")
            return
        
        if tahmin in self.kelime:
            if tahmin == self.kelime[self.gizli_kelime.index("_")]:
                messagebox.showinfo("Tebrikler!", f"Doğru tahmin! Kelime: {self.kelime}")
                self.yeni_oyun()
            else:
                messagebox.showinfo("Yanlış", "Bu harf kelimede var ama gizli harf değil!")
                self.kalan_hak -= 1
        else:
            messagebox.showinfo("Yanlış", "Bu harf kelimede yok!")
            self.kalan_hak -= 1
        
        self.kalan_hak_label.config(text=f"Kalan Hak: {self.kalan_hak}")
        self.tahmin_entry.delete(0, tk.END)
        
        if self.kalan_hak <= 0:
            messagebox.showinfo("Oyun Bitti", f"Kaybettiniz! Doğru kelime: {self.kelime}")
            self.yeni_oyun()

# Oyunu başlat
root = tk.Tk()
oyun = KelimeTahminOyunu(root)
root.mainloop()