 # Giai đoạn 2: Thực hành
stage2_lessons = {
     # GIAI ĐOẠN 2: THỰC HÀNH
    "g2_b2": {
        "title": "Bài 2: Dictionary - Từ điển trong Python",
        "content": (
            "*📘 Dictionary là gì?*\n"
            "➡️ Là kiểu dữ liệu lưu trữ theo cặp `key: value`, giống như một cuốn từ điển.\n\n"
            "*📌 Ví dụ tạo dictionary:*\n"
            "```python\nthong_tin = {'ten': 'Nhung', 'tuoi': 30}\n```\n"
            "- `'ten'` và `'tuoi'` là key.\n"
            "- `'Nhung'` và `30` là value.\n\n"
            "*📌 Truy cập dữ liệu theo key:*\n"
            "```python\nprint(thong_tin['ten'])  # Kết quả: Nhung\n```\n\n"
            "*🎯 Ứng dụng:*\n"
            "- Lưu trữ thông tin người dùng, cấu hình hệ thống, dữ liệu JSON...\n"
            "- Truy xuất nhanh giá trị theo tên rõ ràng."
        )
    },

    "g2_b3": {
        "title": "Bài 3: Xử lý chuỗi và input",
        "content": (
            "*✍️ Nhận dữ liệu từ người dùng với `input()`*\n"
            "```python\nten = input('Nhập tên: ')\nprint(f'Xin chào {ten}')\n```\n"
            "- `input()` luôn trả về chuỗi.\n"
            "- Có thể dùng `int()`, `float()` để ép kiểu nếu cần.\n\n"
            "*🧵 Một số thao tác chuỗi cơ bản:*\n"
            "```python\ns = 'python'\nprint(s.upper())    # In hoa\nprint(s.capitalize())  # Viết hoa chữ đầu\nprint(s.replace('p', 'P'))\n```\n\n"
            "*🎯 Ứng dụng:*\n"
            "- Xử lý dữ liệu người dùng nhập vào (email, tên...)\n"
            "- Làm sạch, chuẩn hóa thông tin trước khi lưu hoặc kiểm thử."
        )
    },

    "g2_b4": {
        "title": "Bài 4: Đọc ghi file .txt",
        "content": (
            "*📄 Đọc/Ghi file văn bản bằng Python*\n\n"
            "*📌 Ghi dữ liệu vào file:*\n"
            "```python\nwith open('data.txt', 'w') as f:\n    f.write('Hello file')\n```\n"
            "- `'w'`: chế độ ghi (overwrite).\n"
            "- `with`: tự đóng file sau khi ghi.\n\n"
            "*📌 Đọc dữ liệu từ file:*\n"
            "```python\nwith open('data.txt', 'r') as f:\n    noi_dung = f.read()\n    print(noi_dung)\n```\n\n"
            "*🎯 Ứng dụng:*\n"
            "- Lưu log kiểm thử.\n"
            "- Đọc dữ liệu đầu vào từ file cấu hình/testdata."
        )
    },

    "g2_b5": {
        "title": "Bài 5: Làm việc với Excel (openpyxl/pandas)",
        "content": (
            "*📊 Đọc file Excel với thư viện `pandas`*\n\n"
            "*📌 Ví dụ đơn giản:*\n"
            "```python\nimport pandas as pd\n\ndf = pd.read_excel('du_lieu.xlsx')\nprint(df.head())\n```\n"
            "- `pd.read_excel()`: đọc file .xlsx.\n"
            "- `df.head()`: in 5 dòng đầu tiên.\n\n"
            "*📌 Ghi dữ liệu ra file Excel:*\n"
            "```python\ndf.to_excel('ket_qua.xlsx', index=False)\n```\n\n"
            "*🎯 Ứng dụng:*\n"
            "- Tự động đọc dữ liệu test từ file.\n"
            "- Xuất báo cáo kết quả test, log xử lý.\n"
            "- Xử lý dữ liệu sản phẩm, thông tin đơn hàng tự động."
        )
    },  
   
}