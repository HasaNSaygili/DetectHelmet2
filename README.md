🦺 Akıllı Baret Takip Sistemi
📌 Proje Hakkında

Bu proje, iş güvenliği alanında baret kullanımını otomatik olarak takip etmek amacıyla geliştirilmiştir.
Görsel işleme ve yapay zekâ tabanlı yöntemlerle çalışan sistem, sahadaki çalışanların baretli veya baretsiz olup olmadığını anlık olarak tespit eder ve raporlar.

🚧 Neden Bu Proje?

Her yıl milyonlarca işçi iş kazalarında hayatını kaybediyor veya yaralanıyor.

OSHA verilerine göre inşaat sektöründeki ölümcül kazaların %20’si baş yaralanmaları kaynaklıdır.

Baret kullanımı, baş travması riskini %60–85 oranında azaltır.

Türkiye’de baret kullanım oranı %56 seviyelerinde kalmaktadır.

Bu proje, insan hatasını minimize etmek ve iş güvenliği kültürünü güçlendirmek amacıyla geliştirilmiştir.

🔧 Kullanılan Teknolojiler

Python 3.10+

YOLOv8 (Ultralytics) – Derin öğrenme modeli

OpenCV – Görsel işleme

Pandas / Excel Writer – Günlük raporlama

Numpy – Veri işleme

📂 Özellikler

Sahada baretli ve baretsiz çalışanları otomatik tespit eder.

Görüntüler üzerinde renk kodlamalı kutular çizer:

🟩 Yeşil → Baretli

🟥 Kırmızı → Baretsiz

Günlük raporları Excel dosyası halinde kaydeder.

Modüler yapısı sayesinde kolayca geliştirilebilir.

💻 Örnek Kod
from ultralytics import YOLO
import cv2

# Modeli yükle
model = YOLO("yolov8n.pt")

# Görüntüyü oku
img = cv2.imread("saha.jpg")

# Tahmin
results = model(img)

# Sonuçları kutularla görselleştir
annotated_frame = results[0].plot()
cv2.imshow("Baret Takip", annotated_frame)
cv2.waitKey(0)

🚀 Gelecek Geliştirmeler

Yelek, gözlük gibi farklı KKD’lerin de takip edilmesi

Bulut tabanlı izleme ve raporlama sistemi

Yapay zekâ destekli iş güvenliği asistanı

📎 Kaynakça

OSHA (2020) – Occupational Injury and Illness Statistics

NIOSH (2018) – Head Protection Guidelines

SGK (2022) – İş Kazası İstatistikleri

👤 Geliştirici
📧 hasansaygili425@gmail.com
🔗 [LinkedIn]:https://medium.com/@hasansaygili425
🔗 [Medium]:https://www.linkedin.com/in/hasan-sayg%C4%B1l%C4%B1-78755024a/
