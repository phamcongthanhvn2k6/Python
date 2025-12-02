# utils.py
import os
import sys

def resource_path(relative_path):
    """
    Lấy đường dẫn tuyệt đối tới tài nguyên.
    Hỗ trợ cả môi trường dev và khi đóng gói bằng PyInstaller.
    """
    try:
        # PyInstaller tạo folder tạm _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)