# Báo Cáo Đánh Giá Sư Phạm: Kiến Thức Nào Cần Đưa Vào Bài Giảng Cho Newbie Non-Tech?

Sau khi phân tích toàn bộ phụ đề (transcript) của 4 video trên, dưới đây là bản phân loại sư phạm khắt khe dựa trên tiêu chí: **"Chỉ đưa vào giáo trình chính những gì là CĂN BẢN và MUST-KNOW cho người mới bắt đầu (non-tech); giữ lại các kiến thức nâng cao ở dạng bài đọc thêm để tránh gây ngợp."**

---

## 1. Các Kiến Thức MUST-KNOW (Đã Tích Hợp Vào Bài Giảng Chính)

### ✅ Điểm 1: Cơ chế Hạn mức Tài khoản & Chu kỳ phục hồi Quota (từ Video 4 của anh Minh)
* **Vấn đề của Newbie:** Người mới khi dùng AI rất sợ bị "hết lượt", "phải trả thêm tiền" hoặc không hiểu tại sao đang dùng thì AI báo chậm lại.
* **Kiến thức căn bản cần biết:**
  * Tài khoản miễn phí: Có hạn mức tuần.
  * Tài khoản Google One Pro / Ultra: Hạn mức làm việc sẽ **tự động phục hồi lại sau mỗi 5 tiếng**.
* **Vị trí tích hợp:** Bổ sung ngay vào [Module 0.2: Cài đặt & Thiết lập Antigravity](../Module_0_Getting_Started/0.2_Installation_Setup.md) để học viên an tâm sử dụng.

### ✅ Điểm 2: Ví dụ phân biệt Rule vs Skill trong Báo cáo Bảng tính (từ Video 2)
* **Vấn đề của Newbie:** Khái niệm "Rule" và "Skill" thường bị học viên non-tech hiểu nhầm là một.
* **Ví dụ thực tế đắt giá:**
  * **Rule (Luật):** *"Cấm tuyệt đối không được xóa hoặc sửa đè lên dữ liệu gốc của file Excel."* (Áp dụng cho mọi tác vụ).
  * **Skill (Kỹ năng):** *"Kỹ năng lọc dữ liệu, tính tổng và vẽ biểu đồ hình cột."* (Chuyên môn cụ thể).
* **Vị trí tích hợp:** Bổ sung vào bảng giải thích tại [Module 1.7: Phân biệt 4 Khái niệm Cốt lõi](../Module_1_Fundamentals/1.7_Core_Concepts.md).

### ✅ Điểm 3: Khảo sát thị trường bằng cách cào dữ liệu không cần đăng nhập (từ Video 4)
* **Vấn đề của Newbie:** Nghĩ rằng AI chỉ đọc được file có sẵn trong máy.
* **Kiến thức căn bản cần biết:** AI có thể tự ra web cào bài viết và bình luận công khai từ mạng xã hội/diễn đàn mà không bắt người dùng phải đăng nhập tài khoản.
* **Vị trí tích hợp:** Nhấn mạnh trong [Module 2.4: Tra cứu Thông tin Web (Web Browsing)](../Module_2_Advanced_PM_Work/2.4_Web_Browsing.md).

---

## 2. Các Kiến Thức ADVANCED / NÂNG CAO (Giữ ở Dạng Bài Đọc Thêm)

Các nội dung sau **KHÔNG NÊN** nhồi vào bài giảng 2 tiếng cho lớp Xóa mù vì sẽ làm học viên non-tech bị quá tải nhận thức:

1. **Cấu trúc kỹ thuật của file `SKILL.md` và mã Python trong `scripts/` (Video 2):**
   * *Lý do:* Học viên non-tech chỉ cần biết CÁCH DÙNG và cơ chế AI tự nhận diện (Auto-Discovery). Việc hướng dẫn họ tự cấu trúc thư mục code sẽ khiến họ nghĩ Antigravity là công cụ dành cho lập trình viên.
2. **Cấu hình Global Skill vs Workspace Skill qua thư mục ẩn `~/.gemini/antigravity/` (Video 2):**
   * *Lý do:* Đòi hỏi thao tác vào thư mục hệ sinh thái ẩn của hệ điều hành, dễ gây lỗi thao tác cho người mới.
3. **Kiến trúc Dynamic Sub-Agents & Parallel Multi-threading (Video 3):**
   * *Lý do:* Đây là kiến thức tầng sâu về cơ chế phân luồng tác tử. Học viên chỉ cần biết "hệ thống xử lý rất nhanh", không cần học cách cấu hình sub-agent.
4. **Hẹn giờ tác vụ tự động (Scheduled Tasks / Cron) (Video 3):**
   * *Lý do:* Phù hợp với khóa học nâng cao (Level 2: Kiến trúc sư AI Workforce) hơn là lớp Xóa mù cơ bản.
