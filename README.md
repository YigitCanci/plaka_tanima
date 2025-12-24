# Plaka Tanıma Sistemi

Bu projemde görüntü işleme teknikleri (OpenCV ve Tesseract-OCR) kullanarak araç plakalarını otomatik olarak tespit edip okuyan bir Python programıdır.

- **Python 3.9**
- **OpenCV**: Görüntü işleme ve kenar tespiti için
- **Pytesseract**: OCR (Optical Character Recognition) ile plaka metnini okumak için

## Kurulum ve çalıştırma

python3 -m venv venv
source venv/bin/activate  # Windows'ta: venv\Scripts\activate
pip install opencv-python pytesseract numpy## Kullanım

Programı çalıştırın ve plaka görseli ismini girin:

python plaka_tanima_sistemi.py Program sizden görsel adı isteyecektir (örn: `plaka1.jpg`). Görseller `plakalar/` klasöründe bulunmalıdır.

## Nasıl Çalışır?

1. **Ön İşleme**: Görsel gri tonlamaya dönüştürülüp Gaussian blur ile bulanıklaştırılır
2. **Kenar Tespiti**: Canny algoritması ile kenarlar belirlenir
3. **Kontur Analizi**: En büyük 10 kontur arasında dörtgen şekiller aranır
4. **Plaka Filtreleme**: En-boy oranı ve boyut kontrolü ile plaka tespiti yapılır
5. **OCR İşlemi**: Tespit edilen bölge büyütülüp, eşikleme ve morfolojik işlemlerden geçirilerek metin okunur

## Örnek Çıktı
    (venv) ╭─MacOS@MacBook-Pro ~/Downloads/odev/plaka_tanima  ‹main*› 
    ╰─➤  python plaka_tanima_sistemi.py                                       
        Görsel adı girin: plaka1.jpg
        Tanımlanan plaka: 20DD444