stage4_lessons = {
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