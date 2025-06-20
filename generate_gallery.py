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
  <title>My gallery</title>
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
    .copy-msg {
      display: none;
      color: green;
      font-size: 0.9em;
      margin-left: 10px;
    }
  </style>
</head>
<!--
  ну ти канєшна хакєр, на тобі анекдот і не балуйся
  чому програмісти не можуть відкрити двері?
  бо вони не бачать кнопки "Відкрити"
  (тому що вони завжди шукають кнопку "Закрити")
  а якщо серйозно, то ти крутий, що читаєш розмітку
  і можливо навіть щось змінюєш
  якщо ти хочеш щось додати або змінити, дай знати
  я можу допомогти
  якщо ти хочеш поділитися своїми ідеями, можеш написати мені в Discord
  або в Instagram
  або в Steam
  я завжди радий спілкуванню
  якщо ти хочеш просто подивитися на галерею, то вперед
  тут багато класних зображень
  і вони всі у форматі webp
  це дозволяє зекономити трафік і час завантаження
  ти красавчік
-->
<body>
  <button class="toggle-theme" onclick="toggleTheme()">🌗 Тема</button>
  <h1>My gallery</h1>
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

  <footer>
    <p>© 2025 Yarik</p>
    <p>
      <a href="https://steamcommunity.com/id/plavlyenyysynok/" target="_blank">🎮 Steam</a> |
      <a href="https://www.instagram.com/yarik_tarnavski9/" target="_blank">📸 Instagram</a> |
      <a href="#" onclick="copyDiscord(event)">💬 Discord</a>
    </p>
  </footer>

  <div id="toast">Ім'я користувача скопійовано</div>

  <style>
    #toast {
      visibility: hidden;
      min-width: 200px;
      background-color: #333;
      color: #fff;
      text-align: center;
      border-radius: 10px;
      padding: 12px 20px;
      position: fixed;
      z-index: 999;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 16px;
      opacity: 0;
      transition: opacity 0.5s ease, visibility 0.5s ease;
    }
    #toast.show {
      visibility: visible;
      opacity: 1;
    }
  </style>

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

    function copyDiscord(event) {
      event.preventDefault();
      const username = "yarik09";
      navigator.clipboard.writeText(username).then(() => {
        const toast = document.getElementById("toast");
        toast.className = "show";
        setTimeout(() => {
          toast.className = toast.className.replace("show", "");
        }, 2000);
      });
    }
  </script>
</body>
</html>
"""


# Запис у HTML-файл
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_start + img_tags + html_end)

print(f"\n✅ Згенеровано {OUTPUT_FILE} з {len(images)} зображеннями.")
