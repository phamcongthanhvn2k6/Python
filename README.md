# 🚀 Space Shooter (Simple)

Dự án game bắn súng không gian 2D cổ điển (Vertical Scrolling Shooter) được phát triển bằng ngôn ngữ **Python** và thư viện **Pygame**. 

Dự án này tập trung vào việc áp dụng **Lập trình hướng đối tượng (OOP)** và tư duy **Clean Code**, chia tách module rõ ràng để dễ dàng bảo trì và mở rộng.

## 📋 Mục lục
- [Giới thiệu](#-giới-thiệu)
- [Tính năng chính](#-tính-năng-chính)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt & Chạy](#-cài-đặt--chạy)
- [Cách chơi](#-cách-chơi)
- [Screenshots](#-screenshots)

## 📖 Giới thiệu
Space Shooter là một game đơn giản nơi người chơi điều khiển phi thuyền tiêu diệt kẻ địch đang lao tới. Mục tiêu là đạt điểm số cao nhất có thể trước khi hết mạng. Dự án được thiết kế để minh họa cách quản lý trạng thái game (Game States), vòng lặp game (Game Loop) và xử lý va chạm (Collision Detection) trong Pygame.

## ✨ Tính năng chính
* **Hệ thống OOP:** Các thực thể (Player, Enemy, Bullet) được quản lý bằng các lớp riêng biệt kế thừa từ `pygame.sprite.Sprite`.
* **Quản lý tài nguyên thông minh:** Hệ thống tự động sử dụng hình khối màu (Placeholder) nếu không tìm thấy file ảnh trong thư mục `assets/`, giúp game không bao giờ bị crash do thiếu resources.
* **Hệ thống High Score:** Điểm cao nhất được lưu trữ bền vững vào file `scores.txt`.
* **Game States:** Chuyển đổi mượt mà giữa Menu chính, Gameplay, Pause và Game Over.
* **Cấu hình tập trung:** Mọi thông số (tốc độ, màu sắc, FPS) đều nằm trong `config.py`.

## 📂 Cấu trúc dự án
Cây thư mục được tổ chức theo mô hình Modular:

```text
SpaceShooter/
├── assets/              # Chứa tài nguyên hình ảnh (player.png, enemy.png, bullet.png)
├── config.py            # Chứa các hằng số cấu hình (Resolution, Colors, Speed...)
├── entities.py          # Định nghĩa các Class: Player, Enemy, Bullet
├── game.py              # Logic chính (Game Loop, Event Handling, Collision)
├── main.py              # Entry Point (Điểm khởi chạy ứng dụng)
├── menu.py              # Quản lý giao diện (UI), Text rendering, Score handling
├── utils.py             # Các hàm tiện ích (xử lý đường dẫn file resource_path)
└── scores.txt           # File tự sinh để lưu điểm cao nhất

🎮 Cách chơi
Hành động
Phím điều khiển
Di chuyển
Phím mũi tên (⬅️ ➡️ ⬆️ ⬇️)
Bắn đạn Phím SPACE
Tạm dừng Phím ESC
Thoát game Phím ESC (tại Menu hoặc Pause)
