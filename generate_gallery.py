import os
from PIL import Image

PHOTO_FOLDER = "photos"
OUTPUT_FILE = "index.html"

# Конвертація зображень у webp
for filename in os.listdir(PHOTO_FOLDER):
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        webp_file = f"{name}.webp"
        webp_path = os.path.join(PHOTO_FOLDER, webp_file)
        if not os.path.exists(webp_path):
            try:
                img_path = os.path.join(PHOTO_FOLDER, filename)
                img = Image.open(img_path).convert("RGB")
                img.save(webp_path, "webp")
                print(f"✅ Конвертовано: {filename} → {webp_file}")
            except Exception as e:
                print(f"❌ Помилка з {filename}: {e}")

# Отримати всі .webp зображення
images = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith('.webp')]

# HTML-частини
html_start = """<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Моя галерея</title>
  <style>
    :root {
      --bg-light: #f2f2f2;
      --bg-dark: #1e1e1e;
      --text-light: #000;
      --text-dark: #fff;
    }
    body {
      font-family: sans-serif;
      background: var(--bg-light);
      color: var(--text-light);
      padding: 20px;
      text-align: center;
      transition: background 0.3s, color 0.3s;
    }
    body.dark-mode {
      background: var(--bg-dark);
      color: var(--text-dark);
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
      transition: transform 0.3s ease;
      cursor: pointer;
    }
    .gallery img:hover {
      transform: scale(1.05);
    }
    .toggle-theme {
      position: fixed;
      top: 20px;
      right: 20px;
      background: #ccc;
      border: none;
      padding: 10px 15px;
      border-radius: 20px;
      cursor: pointer;
      font-weight: bold;
      transition: background 0.3s;
    }
    .toggle-theme:hover {
      background: #aaa;
    }
    .modal {
      display: none;
      position: fixed;
      z-index: 1000;
      padding-top: 50px;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgba(0,0,0,0.9);
    }
    .modal-content {
      margin: auto;
      display: block;
      max-width: 90%;
      max-height: 80vh;
      border-radius: 10px;
    }
    .close {
      position: absolute;
      top: 20px;
      right: 35px;
      color: #fff;
      font-size: 40px;
      font-weight: bold;
      cursor: pointer;
    }
    .close:hover {
      color: #aaa;
    }
  </style>
</head>
<body>
  <button class="toggle-theme" onclick="toggleTheme()">🌗 Тема</button>
  <h1>Моя галерея</h1>
  <div class="gallery">
"""

# Створення <img> з onclick
img_tags = "\n".join(
    [f'    <img src="{PHOTO_FOLDER}/{img}" alt="{img}" onclick="openModal(this)">' for img in sorted(images)]
)

html_end = """
  </div>

  <div id="modal" class="modal" onclick="closeModal()">
    <span class="close" onclick="closeModal()">&times;</span>
    <img class="modal-content" id="modal-img">
  </div>

  <script>
    function toggleTheme() {
      document.body.classList.toggle("dark-mode");
      localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
    }

    window.onload = () => {
      if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
      }
    };

    function openModal(img) {
      const modal = document.getElementById("modal");
      const modalImg = document.getElementById("modal-img");
      modal.style.display = "block";
      modalImg.src = img.src;
    }

    function closeModal() {
      document.getElementById("modal").style.display = "none";
    }
  </script>
</body>
</html>
"""

# Запис у HTML-файл
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_start + img_tags + html_end)

print(f"\n✅ Згенеровано {OUTPUT_FILE} з {len(images)} зображеннями.")
