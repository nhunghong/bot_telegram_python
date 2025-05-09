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
            "*Python là gì?*\n\n"
            "- Python là ngôn ngữ lập trình phổ biến, cú pháp đơn giản, dễ đọc.\n"
            "- Được dùng trong: kiểm thử tự động, phân tích dữ liệu, AI, web...\n"
            "- Dễ học, phù hợp cả với tester chuyển sang automation.\n\n"
            "*Vì sao tester nên học Python?*\n"
            "- Viết script kiểm thử nhanh chóng\n"
            "- Có thư viện mạnh như Selenium, Pandas, Requests...\n"
            "- Hỗ trợ automation test, kiểm API, xử lý file\n\n"
            "*Ví dụ đầu tiên:*\n"
            "```python\nprint(\"Hello, Python!\")\n```\n\n"
            "*Sau bài này bạn sẽ:*\n"
            "- Biết Python dùng để làm gì\n"
            "- Hiểu lợi ích với tester\n"
            "- Cài được Python ở bài sau"
        )
    },
    "g1_b2": {
        "title": "Bài 2: Cài đặt Python & VSCode",
        "content": (
            "- Tải Python từ https://python.org\n"
            "- Tải VSCode từ https://code.visualstudio.com\n"
            "- Mở terminal chạy: `python --version`\n"
            "- Tạo file .py và chạy lệnh `print('Hello')`"
        )
    },
    "g1_b3": {
        "title": "Bài 3: Biến và kiểu dữ liệu",
        "content": "```python\nname = 'Nhung'\nage = 30\nis_tester = True\nheight = 1.62\n```\nKiểu: `str`, `int`, `float`, `bool`"
    },
    "g1_b4": {
        "title": "Bài 4: Toán tử + logic",
        "content": "```python\nif age > 18 and is_tester:\n    print('Bạn đủ điều kiện học nâng cao')\n```"
    },
    "g1_b5": {
        "title": "Bài 5: Câu lệnh điều kiện",
        "content": "```python\nage = 16\nif age >= 18:\n    print('Đăng ký học')\nelse:\n    print('Chưa đủ tuổi')\n```"
    },
    "g1_b6": {
        "title": "Bài 6: Vòng lặp for, while",
        "content": "```python\nfor i in range(5):\n    print(i)\n```\nDùng for để lặp qua danh sách, while cho điều kiện linh hoạt hơn."
    },
    "g1_b7": {
        "title": "Bài 7: Hàm & gọi lại hàm",
        "content": "```python\ndef chao(name):\n    print(f'Chào {name}')\n\nchao('tester')\n```"
    },

    # GIAI ĐOẠN 2: THỰC HÀNH
    "g2_b1": {
        "title": "Bài 1: Danh sách (list) và vòng lặp",
        "content": "```python\ndanh_sach = ['A', 'B', 'C']\nfor ten in danh_sach:\n    print(ten)\n```"
    },
    "g2_b2": {
        "title": "Bài 2: Dictionary - Từ điển trong Python",
        "content": "```python\nthong_tin = {'ten': 'Nhung', 'tuoi': 30}\nprint(thong_tin['ten'])\n```"
    },
    "g2_b3": {
        "title": "Bài 3: Xử lý chuỗi và input",
        "content": "```python\nten = input('Nhập tên: ')\nprint(f'Xin chào {ten}')\n```"
    },
    "g2_b4": {
        "title": "Bài 4: Đọc ghi file .txt",
        "content": "```python\nwith open('data.txt', 'w') as f:\n    f.write('Hello file')\n```"
    },
    "g2_b5": {
        "title": "Bài 5: Làm việc với Excel (openpyxl/pandas)",
        "content": "```python\nimport pandas as pd\ndf = pd.read_excel('du_lieu.xlsx')\nprint(df.head())\n```"
    },

    # GIAI ĐOẠN 3: AUTOMATION
    "g3_b1": {
        "title": "Bài 1: Cài Selenium và mở Chrome",
        "content": "```python\nfrom selenium import webdriver\ndriver = webdriver.Chrome()\ndriver.get('https://google.com')\n```"
    },
    "g3_b2": {
        "title": "Bài 2: Tìm và nhập liệu trong ô textbox",
        "content": "```python\ndriver.find_element('name', 'q').send_keys('python')\n```"
    },
    "g3_b3": {
        "title": "Bài 3: Kiểm tra tiêu đề trang",
        "content": "```python\nassert 'Google' in driver.title\n```"
    },

    # GIAI ĐOẠN 4: NÂNG CAO
    "g4_b1": {
        "title": "Bài 1: Viết hàm kiểm thử tự động",
        "content": "```python\ndef test_title():\n    assert 'Google' in driver.title\n```"
    },
    "g4_b2": {
        "title": "Bài 2: Tạo class quản lý testcase",
        "content": "```python\nclass TestLogin:\n    def test_login(self):\n        pass\n```"
    },
    "g4_b3": {
        "title": "Bài 3: Ghi log và xử lý lỗi",
        "content": "```python\ntry:\n    # chạy test\nexcept Exception as e:\n    print('Lỗi:', e)\n```"
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
