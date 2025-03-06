# tiny-app

## Thông tin cá nhân
- Trương Long Tý - 22656001
- Nguyễn Thái Uy - 22651711

## Mô tả project
Đây là một ứng dụng blog đơn giản được phát triển bằng Django. Ứng dụng cho phép người dùng đăng ký, đăng nhập, tạo bài viết, quản lý bài viết của mình và xem bài viết của người khác. Ngoài ra, admin có thể quản lý người dùng, block/unblock người dùng và reset mật khẩu.

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.9 trở lên
- pip (Python package installer)
- Virtual environment (venv)
- Docker

### Cài đặt
1. Clone repository về máy của bạn:
    ```sh
    git clone https://github.com/truonglongty/tiny-app.git
    cd tiny-app
    ```

2. Tạo và kích hoạt môi trường ảo:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Trên Linux/macOS
    # venv\Scripts\activate   # Trên Windows
    ```

3. Cài đặt các thư viện cần thiết:
    ```sh
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Chạy migrations để tạo cơ sở dữ liệu:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Tạo tài khoản admin:
    ```sh
    python manage.py createsuperuser
    ```

6. Thu thập static files:
    ```sh
    python manage.py collectstatic --noinput
    ```

### Chạy server
1. Chạy server:
    ```sh
    python manage.py runserver
    ```

2. Truy cập ứng dụng tại địa chỉ:
    ```
    http://127.0.0.1:8000/
    ```

### Sử dụng Docker

#### Cách 1: Cài đặt và chạy bằng Docker Hub (không cần clone repo)
1. Kéo image từ Docker Hub:
    ```sh
    docker pull longty/tiny-app:latest
    ```

2. Chạy Docker container:
    ```sh
    docker run -d -p 8000:8000 longty/tiny-app:latest
    ```

3. Truy cập ứng dụng tại địa chỉ:
    ```
    http://127.0.0.1:8000/
    ```

#### Cách 2: Xây dựng và chạy bằng Docker Compose
1. Xây dựng Docker image:
    ```sh
    docker build -t tiny-app .
    ```

2. Chạy Docker container:
    ```sh
    docker-compose up
    ```

3. Truy cập ứng dụng tại địa chỉ:
    ```
    http://127.0.0.1:8000/
    ```
