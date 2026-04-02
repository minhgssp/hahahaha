# Module 1.7: Phân biệt 4 Trụ cột của Antigravity

Chào mừng **AI/Automation PM** đến với bài học "Triết học" nhất của khóa học!
Để làm chủ Antigravity, bạn không cần nhớ lệnh, bạn cần hiểu **Cấu trúc**.

Có 4 khái niệm bạn sẽ gặp hàng ngày: **Knowledge, Workflow, Skill, Rule**.
Nghe có vẻ giống nhau? Hãy phân biệt chúng ngay bây giờ.

**STOP: Bạn đã bao giờ nhầm lẫn giữa "Quy trình" và "Quy tắc" chưa?**

**USER: Có/Chưa**

---

**1. Ví dụ Hình tượng: Người Đầu Bếp**

Hãy tưởng tượng tôi (AI) là một Đầu bếp trong nhà hàng của bạn.

- **Objective (Mục tiêu):** Nấu món Phở Bò.
- **Knowledge (Kiến thức):** Quyển sách công thức gia truyền (Nước dùng hầm 8 tiếng, Quế, Hồi...). Nếu không có sách này, tôi không biết nấu.
- **Workflow (Quy trình):** Các **bước** làm việc: sơ chế → ướp → nấu → trình bày. Đây là *trình tự*.
- **Skill (Kỹ năng):** Các **chi tiết chuyên sâu**: gia vị gì, tỷ lệ ra sao, nhiệt độ bao nhiêu. Đây là *tri thức chi tiết* mà tôi tự áp dụng.
- **Rule (Quy tắc):** "Luôn đeo khẩu trang". "Không được nếm bằng ngón tay". Đây là *luật bất di bất dịch*.

**STOP: Bạn đã hình dung ra sự khác biệt chưa?**

**USER: Rồi**

---

**2. Áp dụng vào Công việc Văn phòng**

Bây giờ hãy quay lại công việc của **AI/Automation PM**.
Bạn cần làm một "Báo cáo Tuần".

- **Knowledge:** Các file báo cáo của nhân viên (`@Sales_Report.csv`, `@HR_Report.md`). Đây là *nguyên liệu*.
- **Workflow:** Quy trình làm báo cáo: 1. Gom file → 2. Đọc lướt → 3. Tóm tắt → 4. Gửi sếp. Đây là *các bước*.
- **Skill:** Quy tắc trình bày số liệu, format trích dẫn, chuẩn ngôn ngữ. Đây là *chi tiết chuyên sâu* AI tự áp dụng.
- **Rule:** "Báo cáo không quá 1 trang A4". "Luôn dùng định dạng PDF". Đây là *luật*.

**STOP: Gõ lệnh: "Phân loại giúp tôi: 'File Danh sách nhân viên' - 'Quy trình Onboarding' - 'Khả năng tìm kiếm Google' - 'Quy định cấm hút thuốc'. Cái nào là K, W, S, R?"**

**USER: Gõ lệnh**

**ACTION: Classify Concepts**
(AI sẽ trả lời:
- Danh sách nhân viên -> Knowledge
- Quy trình Onboarding -> Workflow
- Khả năng tìm kiếm -> Skill
- Quy định cấm hút thuốc -> Rule)

---

**3. Deep Dive: Skill vs Workflow**

Đây là cặp dễ nhầm nhất. Hãy nhớ:

|                 | **Workflow**                          | **Skill**                            |
| --------------- | ------------------------------------- | ------------------------------------ |
| Trả lời câu hỏi | "Làm gì, theo thứ tự nào?"            | "Làm như thế nào, chi tiết ra sao?"  |
| Ai gọi          | User chủ động gọi                     | AI tự áp dụng khi phát hiện context  |
| Ẩn dụ nấu ăn    | Steps: sơ chế → ướp → nấu → trình bày | Chi tiết: gia vị gì, tỷ lệ, nhiệt độ |

**Quy tắc vàng:**
- 1 workflow có thể gọi nhiều skill.
- 1 skill có thể được nhiều workflow gọi chung.
- Skill KHÔNG chứa step-by-step process (đó là workflow territory).
- Workflow KHÔNG đi sâu vào rules/formulas chi tiết (đó là skill territory).

---

**4. Tại sao phải phân biệt?**

- Nếu bạn muốn AI *biết* thêm → Cập nhật **Knowledge** (Thêm file vào thư mục).
- Nếu bạn muốn AI *làm đúng trình tự* → Viết **Workflow** (Tạo file `.agents/workflows/`).
- Nếu bạn muốn AI *làm chi tiết, chuyên sâu hơn* → Tạo **Skill** (Đúc kết knowledge + rules).
- Nếu bạn muốn AI *không bao giờ sai phạm* → Thiết lập **Rule** (Trong `.agent/rules`).

Hiểu rõ 4 cái này — đặc biệt là Skill vs Workflow — bạn là Master.

Bài tiếp theo, chúng ta sẽ học cách quản lý không gian làm việc (Workspace), đảm bảo an toàn dữ liệu, và đồng bộ workspace giữa nhiều thiết bị hoặc với đồng nghiệp.

**STOP: Gõ `/start-1-8` để đi tiếp.**
