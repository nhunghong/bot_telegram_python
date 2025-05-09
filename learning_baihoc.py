from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

#BOT_TOKEN = "7442682123:AAEC5a-kK2dls3UKlC8Ya3ASO6b-pb820tc"

stages = {
    "gd1": "Giai đoạn 1: Làm quen Python",
    "gd2": "Giai đoạn 2: Thực hành thực tế",
    "gd3": "Giai đoạn 3: Automation Test",
    "gd4": "Giai đoạn 4: Nâng cao"
}

lessons = {
    # GIAI ĐOẠN 1
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
            "*📘 Cách khai báo biến trong Python:*\n"
            "```python\nname = 'Nhung'       # chuỗi (string)\nage = 30             # số nguyên (int)\nis_tester = True     # giá trị đúng/sai (bool)\nheight = 1.62         # số thực (float)\n```\n\n"
            "*💡 Một số kiểu dữ liệu cơ bản:*\n"
            "- `str`: chuỗi ký tự, ví dụ: `'Hello'`, `'Python'`\n"
            "- `int`: số nguyên, ví dụ: `1`, `10`, `-5`\n"
            "- `float`: số thực, ví dụ: `1.5`, `3.14`\n"
            "- `bool`: giá trị logic, `True` hoặc `False`\n\n"
            "*🔍 Cách kiểm tra kiểu dữ liệu:*\n"
            "```python\nprint(type(name))     # <class 'str'>\nprint(type(age))      # <class 'int'>\n```\n\n"
            "*🧠 Ghi nhớ:*\n"
            "- Python tự động hiểu kiểu dữ liệu dựa trên giá trị bạn gán.\n"
            "- Không cần khai báo kiểu rõ ràng như các ngôn ngữ khác.\n"
            "- Tên biến nên viết bằng chữ thường, có thể dùng dấu _ (gạch dưới).\n\n"
            "🎯 *Sau bài này bạn sẽ:*\n"
            "- Biết cách khai báo biến\n"
            "- Phân biệt được các kiểu dữ liệu cơ bản\n"
            "- Kiểm tra được kiểu dữ liệu trong Python"
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

    # GIAI ĐOẠN 3: AUTOMATION
    "g3_b1": {
        "title": "Bài 1: Cài Selenium và mở trình duyệt Chrome",
        "content": (
            "*📦 Cài đặt thư viện Selenium:*\n"
            "- Mở terminal và chạy lệnh: `pip install selenium`\n\n"
            "*🌐 Tải ChromeDriver:*\n"
            "- Vào trang: https://sites.google.com/chromium.org/driver/\n"
            "- Tải đúng phiên bản tương ứng với trình duyệt Chrome đang dùng.\n"
            "- Giải nén và đặt vào cùng thư mục với file Python hoặc thêm vào PATH.\n\n"
            "*💻 Mở trình duyệt tự động bằng Python:*\n"
            "```python\nfrom selenium import webdriver\n\n"
            "driver = webdriver.Chrome()\ndriver.get('https://google.com')\n```"
        )
    },

    "g3_b2": {
        "title": "Bài 2: Tìm và nhập dữ liệu vào ô tìm kiếm",
        "content": (
            "*🔍 Tìm phần tử theo name/class/id...*\n"
            "- Cách tìm ô tìm kiếm trên Google là theo `name='q'`\n\n"
            "*📥 Nhập liệu tự động:*\n"
            "```python\nfrom selenium import webdriver\nfrom selenium.webdriver.common.by import By\n\n"
            "driver = webdriver.Chrome()\ndriver.get('https://google.com')\n\n"
            "search_box = driver.find_element(By.NAME, 'q')\n"
            "search_box.send_keys('Python học automation')\n```"
        )
    },

    "g3_b3": {
        "title": "Bài 3: Kiểm tra tiêu đề trang và đóng trình duyệt",
        "content": (
            "*✅ Kiểm tra tiêu đề trang web:* \n"
            "```python\nassert 'Google' in driver.title\n```\n\n"
            "*❌ Đóng trình duyệt sau khi kiểm tra xong:* \n"
            "```python\ndriver.quit()\n```"
        )
    },


    # GIAI ĐOẠN 4: NÂNG CAO
    "g4_b1": {
        "title": "Bài 1: Viết hàm kiểm thử tự động",
        "content": (
            "📌 *Viết hàm kiểm thử tự động là gì?*\n\n"
            "- Là cách bạn kiểm tra 1 chức năng trong hệ thống bằng đoạn mã tự động.\n"
            "- Mỗi hàm kiểm thử nên chỉ kiểm 1 hành vi cụ thể.\n\n"
            "🧪 *Ví dụ kiểm tra tiêu đề trang:*\n"
            "```python\ndef test_title():\n    assert 'Google' in driver.title\n```\n\n"
            "👉 Dòng `assert` sẽ kiểm tra điều kiện đúng/sai.\n"
            "- Nếu đúng → tiếp tục chạy.\n"
            "- Nếu sai → báo lỗi ngay lập tức.\n\n"
            "🎯 *Khi nào dùng?*\n"
            "- Kiểm tra trang web có tải đúng không.\n"
            "- Kiểm tra có hiện đúng dữ liệu không."
        )
    },
    "g4_b2": {
        "title": "Bài 2: Tạo class quản lý testcase",
        "content": (
            "📌 *Vì sao dùng class để tổ chức test?*\n\n"
            "- Nhóm các hàm kiểm thử lại theo module/chức năng.\n"
            "- Dễ mở rộng, quản lý logic test theo từng phần.\n\n"
            "👩‍💻 *Ví dụ class kiểm thử đăng nhập:*\n"
            "```python\nclass TestLogin:\n    def test_login_thanh_cong(self):\n        assert True\n\n"
            "    def test_login_that_bai(self):\n        assert False\n```\n\n"
            "👉 Trong thực tế, các hàm test sẽ thao tác trình duyệt, nhập dữ liệu, bấm nút...\n\n"
            "🎯 *Lưu ý:*\n"
            "- Tên hàm nên bắt đầu bằng `test_`\n"
            "- Có thể dùng framework như `unittest`, `pytest` để chạy toàn bộ class test."
        )
    },
    "g4_b3": {
        "title": "Bài 3: Ghi log và xử lý lỗi",
        "content": (
            "📌 *Lỗi là điều không tránh khỏi trong test tự động.*\n\n"
            "🎯 *Mục tiêu:*\n"
            "- Nếu lỗi → log ra thông tin rõ ràng.\n"
            "- Giúp bạn dễ debug, không bị 'đơ' khi gặp lỗi.\n\n"
            "🛠️ *Ví dụ xử lý lỗi với try/except:*\n"
            "```python\ntry:\n    driver.find_element(\"id\", \"submit\").click()\n"
            "except Exception as e:\n    print(\"❌ Có lỗi xảy ra:\", e)\n```\n\n"
            "🔍 *Tips:*\n"
            "- Ghi log ra file để dễ tra cứu sau.\n"
            "- Có thể dùng thư viện `logging` để quản lý log chuyên nghiệp hơn."
        )
    }

}

async def hoc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐍 Giai đoạn 1: Làm quen Python", callback_data="gd1")],
        [InlineKeyboardButton("⚙️ Giai đoạn 2: Thực hành thực tế", callback_data="gd2")],
        [InlineKeyboardButton("🤖 Giai đoạn 3: Automation Test", callback_data="gd3")],
        [InlineKeyboardButton("🚀 Giai đoạn 4: Nâng cao", callback_data="gd4")],
    ]
    
    text = "*Chọn giai đoạn học:*"
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")


async def show_stage_lessons(query, stage):
    lessons_keyboard = []
    stage_key = f"g{stage[2]}"  # gd1 -> g1, gd2 -> g2 ...
    for i in range(1, 10):
        code = f"{stage_key}_b{i}"
        if code in lessons:
            title = lessons[code]["title"]
            btn = InlineKeyboardButton(title, callback_data=code)
            if len(lessons_keyboard) == 0 or len(lessons_keyboard[-1]) == 2:
                lessons_keyboard.append([btn])
            else:
                lessons_keyboard[-1].append(btn)
    lessons_keyboard.append([InlineKeyboardButton("💖 Quay lại menu giai đoạn", callback_data="menu")])
    await query.edit_message_text(
        f"*{stages[stage]}*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(lessons_keyboard)
    )


async def show_lesson_detail(query, code):
    lesson = lessons.get(code)
    if not lesson:
        return
    stage_number = code.split("_")[0][1]  # "g1" -> "1"
    stage = f"gd{stage_number}"           # "gd1"

    current_number = int(code.split("_b")[1])
    prev_code = f"g{stage_number}_b{current_number - 1}" if f"g{stage_number}_b{current_number - 1}" in lessons else None
    next_code = f"g{stage_number}_b{current_number + 1}" if f"g{stage_number}_b{current_number + 1}" in lessons else None

    buttons = []
    if prev_code:
        buttons.append(InlineKeyboardButton("⬅️ Bài trước", callback_data=prev_code))
    if next_code:
        buttons.append(InlineKeyboardButton("➡️ Bài tiếp", callback_data=next_code))
    buttons.append(InlineKeyboardButton("🔙 Quay lại", callback_data=stage))

    await query.edit_message_text(
        f"*{lesson['title']}*\n\n{lesson['content']}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([buttons])
    )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu":
        # Gọi lại menu nhưng dùng edit_message_text vì đang ở callback
        await hoc_callback(query)
    elif data in stages:
        return await show_stage_lessons(query, data)
    elif data in lessons:
        return await show_lesson_detail(query, data)

async def hoc_callback(query):
    keyboard = [
        [InlineKeyboardButton("🐍 Giai đoạn 1: Làm quen Python", callback_data="gd1")],
        [InlineKeyboardButton("⚙️ Giai đoạn 2: Thực hành thực tế", callback_data="gd2")],
        [InlineKeyboardButton("🤖 Giai đoạn 3: Automation Test", callback_data="gd3")],
        [InlineKeyboardButton("🚀 Giai đoạn 4: Nâng cao", callback_data="gd4")],
    ]
    await query.edit_message_text(
        "*Chọn giai đoạn học:*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    await app.bot.set_my_commands([BotCommand("hoc", "Xem danh sách bài học")])
    app.add_handler(CommandHandler("hoc", hoc))
    app.add_handler(CallbackQueryHandler(handle_callback))
    print("✅ Bot bài học Python đã khởi động.")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
