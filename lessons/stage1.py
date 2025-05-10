# Giai đoạn 1: Làm quen Python
stage1_lessons = {
    "g1_b1": {
        "title": "Bài 1: Giới thiệu Python",
        "content": (
            "*👋 Python là gì?*\n\n"
            "- Python là ngôn ngữ lập trình bậc cao, cú pháp đơn giản, dễ đọc.\n"
            "- Dùng trong nhiều lĩnh vực: kiểm thử tự động, phân tích dữ liệu, AI, web...\n"
            "- Phù hợp cả với người mới học lập trình hoặc tester muốn chuyển sang automation.\n\n"
            "*🤔 Tại sao chọn Python mà không phải ngôn ngữ khác?*\n"
            "- ✔️ Cú pháp ngắn gọn, dễ hiểu hơn Java, C++, C#\n"
            "- ✔️ Cộng đồng lớn, dễ tìm tài liệu và hỗ trợ\n"
            "- ✔️ Có nhiều thư viện mạnh: Selenium (test), Pandas (xử lý dữ liệu), FastAPI, v.v.\n"
            "- ✔️ Được dùng bởi các công ty lớn: Google, Facebook, Netflix, NASA...\n"
            "- ✔️ Không cần học cấu trúc phức tạp như class, static... từ đầu\n\n"
            "*🔧 Python giúp gì cho tester?*\n"
            "- Viết script kiểm thử tự động nhanh chóng\n"
            "- Test API dễ dàng với Requests\n"
            "- Tự động hóa kiểm tra Excel, email, báo cáo...\n\n"
            "*📦 Ví dụ đầu tiên:*\n"
            "```python\nprint(\"Hello, Python!\")\n```\n\n"
            "*🎯 Sau bài này bạn sẽ:*\n"
            "- Hiểu Python dùng để làm gì\n"
            "- Lý do nên chọn Python cho automation\n"
            "- Chuẩn bị cài đặt Python ở bài tiếp theo"
        ),
        "exercise": (
            "*📚 Bài tập Bài 1:*\n"
            "1. Viết lệnh in ra dòng chữ: `Hello Tester`\n"
            "2. Viết 3 dòng lệnh in ra tên, tuổi và nghề nghiệp của bạn.\n\n"
            "*Gợi ý: dùng lệnh `print()`*"
        )
    },
    "g1_b2": {
        "title": "Bài 2: Cài đặt Python & VSCode",
        "content": (
            "🧩 *Cài Python*\n"
            "1. Truy cập: https://www.python.org/downloads/\n"
            "2. Chọn phiên bản ổn định mới nhất (gợi ý: Python 3.12.x)\n"
            "3. Khi cài đặt:\n"
            "   - ✅ Tick vào *\"Add Python to PATH\"*\n"
            "   - ✅ Chọn *\"Install Now\"*\n"
            "\n"
            "🔍 Kiểm tra sau khi cài:\n"
            "`python --version`\n"
            "\n"
            "---\n"
            "💻 *Cài Visual Studio Code (VSCode)*\n"
            "1. Truy cập: https://code.visualstudio.com/\n"
            "2. Chọn bản phù hợp hệ điều hành của bạn (Windows/Mac/Linux)\n"
            "3. Sau khi cài:\n"
            "   - Mở VSCode\n"
            "   - Vào Extensions (Ctrl+Shift+X) → Cài *Python* (tác giả: Microsoft)\n"
            "\n"
            "---\n"
            "🚀 *Chạy thử Python đầu tiên:*\n"
            "1. Tạo file `test.py`\n"
            "2. Nhập:\n"
            "```python\nprint(\"Xin chào Python!\")\n```\n"
            "3. Click chuột phải → *Run Python File in Terminal*\n"
            "\n"
            "✅ Sau bài này:\n"
            "- Bạn đã cài xong Python & VSCode\n"
            "- Biết cách chạy 1 file Python đơn giản"
        )

    },
    "g1_b3": {
        "title": "Bài 3: Biến và kiểu dữ liệu",
        "content": (
            "*📦 Biến là gì?*\n"
            "- Biến là nơi lưu trữ dữ liệu trong chương trình.\n"
            "- Bạn có thể tưởng tượng nó như hộp chứa giá trị.\n\n"
            
            "*🧠 Khai báo biến trong Python:*\n"
            "```python\nname = 'Nhung'        # chuỗi (str)\nage = 30              # số nguyên (int)\nheight = 1.6          # số thực (float)\nis_tester = True      # đúng/sai (bool)\n```\n\n"

            "*📘 Kiểu dữ liệu cơ bản:*\n"
            "- `str`: chuỗi ký tự (vd: 'Hello')\n"
            "- `int`: số nguyên (vd: 10, -5)\n"
            "- `float`: số thực (vd: 3.14)\n"
            "- `bool`: logic đúng/sai (True/False)\n\n"

            "*🔍 Kiểm tra kiểu dữ liệu:*\n"
            "```python\nprint(type(name))    # <class 'str'>\nprint(type(age))     # <class 'int'>\n```\n\n"

            "*📝 Ghi nhớ:*\n"
            "- Python tự hiểu kiểu dựa vào giá trị gán.\n"
            "- Không cần khai báo kiểu rõ ràng như Java/C++.\n"
            "- Tên biến nên dùng chữ thường, có thể có gạch dưới `_`.\n\n"

            "🎯 *Sau bài này bạn sẽ:*\n"
            "- Biết khai báo biến trong Python\n"
            "- Phân biệt các kiểu dữ liệu cơ bản\n"
            "- Dùng `type()` để kiểm tra kiểu dữ liệu"
        )
    },
    "g1_b4": {
        "title": "Bài 4: Toán tử + logic",
        "content": (
            "*🔢 Toán tử trong Python:*\n\n"
            "*1. Toán tử số học:*\n"
            "- `+` cộng: `a + b`\n"
            "- `-` trừ: `a - b`\n"
            "- `*` nhân: `a * b`\n"
            "- `/` chia: `a / b`\n"
            "- `//` chia lấy nguyên: `a // b`\n"
            "- `%` chia lấy dư: `a % b`\n"
            "- `**` lũy thừa: `a ** b`\n\n"
            "```python\na = 5\nb = 2\nprint(a + b)   # 7\nprint(a % b)   # 1\n```\n\n"

            "*2. Toán tử so sánh:*\n"
            "- `==`: so sánh bằng\n"
            "- `!=`: khác nhau\n"
            "- `>`: lớn hơn\n"
            "- `<`: nhỏ hơn\n"
            "- `>=`: lớn hơn hoặc bằng\n"
            "- `<=`: nhỏ hơn hoặc bằng\n"
            "```python\nprint(5 > 2)    # True\nprint(3 == 4)   # False\n```\n\n"

            "*3. Toán tử logic:*\n"
            "- `and`: đúng khi cả 2 đều đúng\n"
            "- `or`: đúng khi ít nhất 1 cái đúng\n"
            "- `not`: phủ định giá trị\n"
            "```python\nage = 25\nis_tester = True\nprint(age > 18 and is_tester)  # True\n```\n\n"

            "*🎯 Ứng dụng logic:* Ví dụ kiểm tra đủ điều kiện học nâng cao:\n"
            "```python\nif age > 18 and is_tester:\n    print('Bạn đủ điều kiện học nâng cao')\nelse:\n    print('Chưa đủ điều kiện')\n```\n\n"

            "📌 *Ghi nhớ:*\n"
            "- Dùng toán tử để xử lý dữ liệu số và logic.\n"
            "- Các điều kiện logic thường dùng trong kiểm thử tự động và xử lý dữ liệu.\n"
            "- Kết hợp `if`, `and`, `or`, `not` rất quan trọng khi viết kiểm thử.\n"
        )
    },

    "g1_b5": {
        "title": "Bài 5: Câu lệnh điều kiện",
        "content": (
            "*📌 Câu lệnh điều kiện `if - else - elif` là gì?*\n\n"
            "👉 Dùng để kiểm tra điều kiện đúng hay sai và xử lý theo từng trường hợp.\n\n"

            "*1. Câu lệnh `if - else`:*\n"
            "```python\nage = 16\nif age >= 18:\n    print('Đủ tuổi học nâng cao')\nelse:\n    print('Chưa đủ tuổi')\n```\n"
            "➡️ Nếu điều kiện đúng thì thực hiện phần `if`, nếu sai thì thực hiện phần `else`.\n\n"

            "*2. Câu lệnh `elif` (else if):*\n"
            "```python\nscore = 85\nif score >= 90:\n    print('Xuất sắc')\nelif score >= 70:\n    print('Khá')\nelse:\n    print('Cần cố gắng')\n```\n"
            "➡️ Kiểm tra nhiều điều kiện. Điều kiện nào đúng đầu tiên sẽ được thực hiện.\n\n"

            "*3. So sánh kết hợp nhiều điều kiện:*\n"
            "```python\nage = 22\nis_tester = True\nif age >= 18 and is_tester:\n    print('Học được automation rồi!')\n```\n\n"

            "*💡 Ghi nhớ:*\n"
            "- `if` luôn đứng đầu khối điều kiện.\n"
            "- `elif` có thể có nhiều dòng.\n"
            "- `else` chỉ có 1 và luôn nằm cuối cùng.\n\n"

            "✅ Đây là cấu trúc rất quan trọng trong kiểm thử logic, tự động hóa và xử lý luồng dữ liệu."
        )
    },
    "g1_b6": {
        "title": "Bài 6: Vòng lặp for, while",
        "content": (
            "*🔁 Vòng lặp dùng để làm gì?*\n"
            "➡️ Vòng lặp giúp lặp đi lặp lại một khối lệnh nhiều lần thay vì phải viết lại thủ công.\n\n"

            "*1. Vòng lặp `for`: Duyệt qua danh sách*\n"
            "```python\ndanh_sach = ['Python', 'Selenium', 'API']\nfor ten in danh_sach:\n    print('Tôi đang học:', ten)\n```\n"
            "➡️ Lặp qua từng phần tử trong danh sách và xử lý.\n\n"

            "*2. Vòng lặp với `range()` – Đếm số lần*\n"
            "```python\nfor i in range(5):\n    print('Lần', i)\n```\n"
            "➡️ `range(5)` tạo ra các số từ 0 đến 4 (5 số).\n\n"

            "*3. Vòng lặp `while`: Lặp khi điều kiện còn đúng*\n"
            "```python\nn = 1\nwhile n <= 3:\n    print('Lần lặp:', n)\n    n += 1\n```\n"
            "➡️ Dùng `while` khi chưa biết rõ số lần lặp.\n\n"

            "*📌 Ghi nhớ:*\n"
            "- `for` phù hợp khi duyệt danh sách hoặc số lần cụ thể.\n"
            "- `while` dùng khi muốn lặp đến khi điều kiện thay đổi.\n"
            "- Đừng quên `n += 1` nếu không sẽ lặp vô tận 😱\n\n"

            "🎯 *Ứng dụng trong thực tế:*\n"
            "- Lặp qua danh sách dữ liệu kiểm thử\n"
            "- Chạy kiểm tra nhiều trường hợp một cách tự động\n"
            "- Tự động kiểm tra từng bước trong hệ thống"
        )
    },

    "g1_b7": {
        "title": "Bài 7: Hàm & gọi lại hàm",
        "content": (
            "*📣 Hàm là gì?*\n"
            "➡️ Hàm là tập hợp các lệnh được đặt tên, dùng để thực hiện một nhiệm vụ cụ thể.\n"
            "➡️ Giúp chia nhỏ chương trình, tái sử dụng và dễ quản lý hơn.\n\n"

            "*📌 Cách định nghĩa hàm:*\n"
            "```python\ndef chao(name):\n    print(f'Chào {name}, chúc bạn học tốt!')\n```\n"
            "👉 `def` là từ khóa để định nghĩa hàm.\n"
            "👉 `chao` là tên hàm, `name` là tham số truyền vào.\n\n"

            "*▶️ Gọi lại hàm:*\n"
            "```python\nchao('Nhung')\n```\n"
            "➡️ Kết quả: `Chào Nhung, chúc bạn học tốt!`\n\n"

            "*🎯 Lợi ích khi dùng hàm:*\n"
            "- Giúp code ngắn gọn, dễ đọc.\n"
            "- Có thể gọi lại nhiều lần thay vì lặp code.\n"
            "- Dễ sửa lỗi hoặc mở rộng logic kiểm thử.\n\n"

            "*🚀 Ứng dụng thực tế:*\n"
            "- Viết các bước kiểm thử như: `login()`, `logout()`\n"
            "- Tái sử dụng kiểm thử nhiều trang khác nhau\n"
            "- Tổ chức code rõ ràng theo chức năng\n\n"

            "*✅ Ghi nhớ:*\n"
            "- Hàm phải định nghĩa trước khi gọi.\n"
            "- Có thể có hoặc không có tham số.\n"
            "- Có thể trả kết quả về bằng `return`."
        )
    },
}