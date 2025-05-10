stage3_lessons = {
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
}