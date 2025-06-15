
import os

PHOTO_FOLDER = "photos"
OUTPUT_FILE = "index.html"

html_start = """<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Моя Автоматична Галерея</title>
  <style>
    body {
      font-family: sans-serif;
      background: #f2f2f2;
      padding: 20px;
      text-align: center;
    }
    h1 {
      margin-bottom: 30px;
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 15px;
    }
    .gallery img {
      width: 100%;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
      transition: 0.3s ease;
    }
    .gallery img:hover {
      transform: scale(1.05);
    }
  </style>
</head>
<body>
  <h1>Моя Фото-Галерея</h1>
  <div class="gallery">
"""

html_end = """
  </div>
</body>
</html>
"""

# Отримати список зображень
images = [f for f in os.listdir(PHOTO_FOLDER)
          if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]

# Створити HTML-код
img_tags = "\n".join([f'    <img src="{PHOTO_FOLDER}/{img}" alt="{img}">' for img in images])

# Записати у файл
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_start + img_tags + html_end)

print(f"Згенеровано {OUTPUT_FILE} з {len(images)} зображеннями.")
