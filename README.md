# WEB CRAWLER TOOL

1. GIỚI THIỆU

---

Web Crawler Tool là một ứng dụng Python cho phép người dùng nhập URL của một trang web, sau đó hệ thống sẽ crawl dữ liệu HTML hoặc XML từ trang đó và xuất kết quả ra file TXT để tải về.

Ứng dụng gồm 2 phần:

* Frontend: Flask (hiển thị form nhập URL)
* Backend API: FastAPI (xử lý crawl dữ liệu)
* Server API: Uvicorn
* Output: File TXT sau khi xử lý dữ liệu

2. YÊU CẦU HỆ THỐNG

---

* Python 3.10 trở lên
* pip (Python package manager)

3. CÀI ĐẶT PROJECT

---

Clone repository:

```
git clone https://github.com/ThaiPhann/Web-Crawler-Tool.git
```

Di chuyển vào thư mục project:

```
cd crawler_application
```

## 4. TẠO MÔI TRƯỜNG ẢO (Virtual Environment)

Windows:

```
python -m venv .venv
```

Kích hoạt:

```
.venv\Scripts\activate
```

Linux / MacOS:

```
python3 -m venv .venv
source .venv/bin/activate
```

## 5. CÀI ĐẶT THƯ VIỆN

Cài đặt dependencies:

```
pip install -r requirements.txt
```

## 6. CẤU TRÚC THƯ MỤC

```bash
crawler_application
│
├── crawlerapp
│   ├── app
│   │   ├── crawler_api.py
│   │   └── output
│   │       └── txt
│   │
│   ├── static
│   │   └── css
│   │       └── style.css
│   │
│   ├── templates
│   │   └── index.html
│   │
│   ├── __init__.py
│   └── index.py
│
├── requirements.txt
└── README.md
```

7. CHẠY BACKEND CRAWLER API

---

Di chuyển vào thư mục chứa file API:

```
cd crawlerapp/app
```

Chạy server API bằng Uvicorn:

```
uvicorn crawler_api:app --reload
```

Server API sẽ chạy tại:

```
http://127.0.0.1:8000
```

## 8. CHẠY FRONTEND FLASK

Mở terminal khác và chạy:

```
python crawlerapp/index.py
```

Flask server sẽ chạy tại:

```
http://127.0.0.1:5000
```

## 9. TRUY CẬP ỨNG DỤNG

Mở trình duyệt và truy cập:

```
http://127.0.0.1:5000
```

Trang web sẽ hiển thị form để nhập URL và chọn định dạng dữ liệu cần crawl.

10. CÁCH SỬ DỤNG

---

1. Nhập URL của trang web cần crawl

2. Chọn định dạng dữ liệu:

   * HTML
   * XML

3. Nhấn nút Crawl

4. Backend API sẽ xử lý dữ liệu

5. File TXT sẽ được tạo và tải xuống

6. OUTPUT

---

Các file dữ liệu sau khi crawl sẽ được lưu tại:

```
crawlerapp/app/output/txt/
```

## 12. LƯU Ý

* Không commit thư mục .venv lên Git
* Các file crawler output nên được ignore trong .gitignore
* File requirements.txt chứa toàn bộ dependencies của project

13. TÁC GIẢ

---

Author: Thái Phan
GitHub: https://github.com/ThaiPhann
