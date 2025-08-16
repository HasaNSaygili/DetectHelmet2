import os
import cv2
from ultralytics import YOLO
import pandas as pd
from datetime import datetime

model = YOLO("best.pt")

input_folder = "test_images"
output_folder = "test_outputs"
os.makedirs(output_folder, exist_ok=True)

#Rapor için liste
report_data = []

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Şu anki tarih ve saat
        now = datetime.now()
        tarih = now.strftime("%d.%m.%Y")
        saat = now.strftime("%H:%M:%S")

        results = model.predict(source=image_path, conf=0.3, save=False)

        helmet_count = 0
        no_helmet_count = 0

        for result in results:
            boxes = result.boxes
            names = model.names

            for box in boxes:
                cls_id = int(box.cls[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                label_original = names[cls_id]

                if label_original == "head":
                    label = "no helmet"
                    color = (0, 0, 255)
                    no_helmet_count += 1
                elif label_original == "helmet":
                    label = "helmet"
                    color = (0, 128, 0)
                    helmet_count += 1
                else:
                    continue

                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                cv2.putText(image, label, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        total = helmet_count + no_helmet_count
        if total > 0:
            ratio = (helmet_count / total) * 100
            ratio_text = f"Baret Takilma Orani: %{ratio:.2f}"
        else:
            ratio = 0.0
            ratio_text = "Baret Takilma Orani: %0.00"

        # Sağ alt köşeye oran yaz
        text_size = cv2.getTextSize(ratio_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = image.shape[1] - text_size[0] - 10
        text_y = image.shape[0] - 10

        cv2.putText(image, ratio_text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        save_path = os.path.join(output_folder, filename)
        cv2.imwrite(save_path, image)

        # Rapor verisi ekle
        report_data.append({
            "Görsel Adı": filename,
            "Tarih": tarih,
            "Saat": saat,
            "Baretli Sayı": helmet_count,
            "Baretsiz Sayı": no_helmet_count,
            "Toplam Kişi": total,
            "Baret Takılma Oranı (%)": round(ratio, 2)
        })

        print(f"✓ {filename} işlendi")

# Excel'e yaz
df = pd.DataFrame(report_data)

# Bugünün tarihini al
bugun = datetime.now().strftime("%d-%m-%Y")
excel_adi = f"günlük_baret_raporu_{bugun}.xlsx"

# Excel olarak kaydet
df.to_excel(excel_adi, index=False)
print(f"📊 Rapor oluşturuldu: {excel_adi}")