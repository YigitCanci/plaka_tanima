import cv2
import pytesseract
import os

def plaka_okuma(gorsel_yolu):
    if (gorsel := cv2.imread(gorsel_yolu)) is None:
        print("Görsel bulunamadı!")
        return

    gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)
    bulaniklik = cv2.GaussianBlur(gri, (5, 5), 0)
    kenarlar = cv2.Canny(bulaniklik, 50, 150)
    
    # Kenar görüntüsünde dış konturları (şekil sınırlarını) bul
    konturlar, _ = cv2.findContours(kenarlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    konturlar = sorted(konturlar, key=cv2.contourArea, reverse=True)[:10]

    for kontur in konturlar:
        yaklasim = cv2.approxPolyDP(kontur, 0.018 * cv2.arcLength(kontur, True), True)
        
        if len(yaklasim) == 4:
            x, y, w, h = cv2.boundingRect(kontur)
            
            # Plaka en-boy oranı (2.0-5.5) ve genişlik (50-500px) kontrolü
            if 2.0 < (w / h) < 5.5 and 50 < w < 500:
                # Plaka bölgesini 2 kat büyüt, Otsu eşikleme yöntemi ile siyah-beyaz ikili binary görüntüye dönüştür
                _, thresh = cv2.threshold(cv2.resize(gri[y:y+h, x:x+w], None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                # OCR ile metni oku, karakterlerdeki gürültüleri kapat, temizle
                plaka_metni = ''.join(pytesseract.image_to_string(cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))), 
                config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPRSTUVYZ'))
                if len(plaka_metni) >=7:
                    print(f"Tanımlanan plaka: {plaka_metni}")
                else:
                    print("Plaka tanımlanamadı!")
                return

    print("Plaka bulunamadı!")

plaka_okuma(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plakalar", input("Görsel adı girin: ")))
