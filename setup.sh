#!/bin/bash

echo "🚀 Bắt đầu cài đặt project Django trong tiny-app..."

# Bước 1: Di chuyển vào thư mục chứa Django project (myblog)
cd myblog || { echo "❌ Thư mục 'myblog' không tồn tại! Kiểm tra lại."; exit 1; }

# Bước 2: Tạo và kích hoạt virtual environment
echo "📦 Tạo môi trường ảo (venv)..."
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows (dùng lệnh này nếu chạy trên Windows)

# Bước 3: Cài đặt thư viện cần thiết
echo "📌 Cài đặt dependencies từ requirements.txt..."
pip install --upgrade pip
pip install -r ../requirements.txt  # Đọc từ file requirements.txt ở thư mục tiny-app/

# Bước 4: Chạy migrations
echo "🛠️ Chạy migrations..."
python manage.py makemigrations
python manage.py migrate

# Bước 5: Tạo superuser nếu chưa có
echo "🔑 Kiểm tra và tạo tài khoản admin..."
echo "Bạn có muốn tạo tài khoản admin không? (y/n)"
read create_admin
if [[ "$create_admin" == "y" ]]; then
    python manage.py createsuperuser
fi

# Bước 6: Thu thập static files
echo "🎨 Thu thập static files..."
python manage.py collectstatic --noinput

# Bước 7: Chạy server
echo "🚀 Chạy server..."
python manage.py runserver

echo "✅ Cài đặt hoàn tất! Truy cập http://127.0.0.1:8000/"
