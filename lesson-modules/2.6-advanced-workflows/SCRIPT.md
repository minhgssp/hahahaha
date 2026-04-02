# Module 2.6: Meta-Workflows & Reverse Engineering

Chào mừng **AI/Automation PM** đến với cấp độ cao nhất: **Meta-Programming**.
Hôm nay, bạn sẽ không viết code. Bạn sẽ dạy AI viết code cho bạn.

**STOP: Bạn có thấy việc viết file workflow thủ công hơi mệt không?**

**USER: Có**

---

**1. Tư duy Reverse Engineering (Dịch ngược)**

Thay vì "Nghĩ -> Làm", chúng ta sẽ "Làm -> Đóng gói".
Antigravity có khả năng nhớ lại những gì vừa xảy ra.

**Bài tập:** Tạo workflow `/quick-report`.
Giả sử bạn muốn tạo quy trình: Đọc file -> Tóm tắt 3 ý chính -> Gửi email.

**Bước 1: Làm nháp.**
Hãy ra lệnh cho tôi làm từng bước một:
1. "Đọc file `1.1_Welcome.md`."
2. "Tóm tắt 3 ý chính."
3. "Viết email nháp gửi Sếp dựa trên ý chính đó."

**STOP: Hãy thực hiện 3 lệnh trên ngay bây giờ.**

**USER: (Thực hiện)**

**ACTION: Execute steps.**

---

**2. Sử dụng `/buildflow`**

Bây giờ bạn đã có "Lịch sử thành công". Hãy đóng gói nó.

**STOP: Gõ lệnh: "Dùng `/buildflow` để tạo workflow tên là `/quick-email`. Hãy trích xuất các bước tôi vừa làm thành quy trình chuẩn."**

**USER: Gõ lệnh**

**ACTION: Create Workflow File**

(Tôi sẽ tự tạo file `.agent/workflows/quick-email.md` cho bạn).

---

**3. Thử thách nâng cao: Workflow `/learn`**

Bạn muốn hệ thống tự thông minh lên?
Hãy tạo workflow `/learn`:
1.  Đọc file mới.
2.  So sánh với quy trình cũ.
3.  Cập nhật quy trình cũ.

Đây là bài tập về nhà dành cho bạn. Hãy thử dùng `/buildflow` để tạo ra nó.

---

**4. Lời kết**

Khóa học đến đây là kết thúc.
Bạn đã có trong tay chiếc chìa khóa vạn năng.
- Bạn biết dùng AI.
- Bạn biết dạy AI.
- Bạn biết tạo ra công cụ để AI tự dạy chính mình.

Chúc bạn thành công trên con đường **AI/Automation PM**!

**STOP: Gõ `/finish` để tốt nghiệp.**
