# 👽 Alien Invasion

**Alien Invasion** là một dự án game bắn súng không gian 2D (Vertical Scrolling Shooter) được phát triển bằng ngôn ngữ **Python** và thư viện **Pygame**.

Dự án này được xây dựng với mục tiêu thực hành **Lập trình hướng đối tượng (OOP)**, tư duy **Clean Code** và kiến trúc **Modular**, chia tách các thành phần logic rõ ràng để tối ưu hóa việc bảo trì và mở rộng.

## 📋 Mục lục
- [Giới thiệu](#-giới-thiệu)
- [Tính năng kỹ thuật](#-tính-năng-kỹ-thuật)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Cài đặt & Chạy](#-cài-đặt--chạy)
- [Cách chơi](#-cách-chơi)
- [Tác giả](#-tác-giả)

## 📖 Giới thiệu
Trong **Alien Invasion**, người chơi điều khiển một phi thuyền chiến đấu chống lại hạm đội người ngoài hành tinh. Dự án minh họa các khái niệm cốt lõi trong lập trình game:
* **Game Loop:** Quản lý vòng lặp xử lý logic và vẽ hình.
* **State Management:** Chuyển đổi trạng thái giữa Menu, Playing, Pause và Game Over.
* **Collision Detection:** Xử lý va chạm vật lý giữa đạn, tàu và kẻ địch.
* **Particle System:** Hệ thống hiệu ứng hạt nổ tung khi tiêu diệt mục tiêu.

## ✨ Tính năng kỹ thuật
* **Kiến trúc OOP:** Các thực thể (`Player`, `Enemy`, `Bullet`, `Explosion`) được kế thừa và quản lý chặt chẽ từ `pygame.sprite.Sprite`.
* **Module hóa (Modularity):** Code được tách biệt thành các file chức năng (`game`, `entities`, `visuals`, `menu`), tránh tình trạng "Spaghetti code".
* **Hiệu ứng đồ họa (Procedural Graphics):**
    * Hệ thống nền sao cuộn (Parallax Starfield) tạo chiều sâu không gian.
    * Hệ thống hạt (Particle System) tạo hiệu ứng nổ chân thực mà không cần dùng ảnh GIF.
* **Quản lý tài nguyên thông minh (Fallback Mechanism):** Tự động vẽ hình học vector (Tam giác, Tròn) nếu không tìm thấy file ảnh trong thư mục `assets/`, đảm bảo game không bao giờ bị crash do thiếu resource.
* **Data Persistence:** Lưu trữ điểm cao nhất (High Score) bền vững vào file `scores.txt`.
* **Config:** Mọi thông số cân bằng game (Game Balance) như tốc độ, màu sắc, FPS đều nằm tập trung trong `config.py`.

## 📂 Cấu trúc dự án
Cây thư mục được tổ chức khoa học:

```text
AlienInvasion/
├── assets/              # Chứa tài nguyên hình ảnh (nếu có)
├── config.py            # Cấu hình hằng số (Screen, Colors, Physics settings)
├── entities.py          # Định nghĩa Class: Player, Enemy, Bullet
├── game.py              # Logic chính (Core Loop, Spawning, Collision)
├── main.py              # Entry Point (Điểm khởi chạy chương trình)
├── menu.py              # Quản lý UI, Font chữ và Score I/O
├── visuals.py           # [NEW] Xử lý hiệu ứng hình ảnh (Starfield, Explosion)
├── utils.py             # Hàm tiện ích xử lý đường dẫn hệ thống
└── scores.txt           # File tự sinh lưu High Score

⚙️ Yêu cầu hệ thống
Python: 3.10 trở lên
Thư viện: Pygame

🛠 Cài đặt & Chạy
1. Clone dự án
  Bashgit clone [https://github.com/phamcongthanhvn2k6/AlienInvasion.git](https://github.com/phamcongthanhvn2k6/AlienInvasion.git)
  cd AlienInvasion
2. Thiết lập môi trường (Khuyên dùng)
Bash# Windows
python -m venv .venv
.venv\Scripts\activate
3. Cài đặt thư viện
Bashpip install pygame
4. Chạy game
Bashpython main.py
🎮 Cách chơi
Hành động
Phím điều khiển
Di chuyển: Phím mũi tên (⬅️ ➡️ ⬆️ ⬇️)
Bắn đạn: Phím SPACE
Tạm dừng: Phím ESC
Thoát game: Phím ESC (tại Menu hoặc Pause)
