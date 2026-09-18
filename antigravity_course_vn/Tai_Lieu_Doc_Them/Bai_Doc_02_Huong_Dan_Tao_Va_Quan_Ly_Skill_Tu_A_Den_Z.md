# Bài Đọc Thêm 02: Hướng Dẫn Tạo & Quản Lý Skill AI Từ A-Z

> 📺 **Nguồn Video tham khảo:** [Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z](https://www.youtube.com/watch?v=UFmV7YsVqlM) (Thời lượng: 22:39)

---

## 💡 Nỗi Mệt Mỏi Khi Phải "Cầm Tay Chỉ Việc" Mỗi Ngày
Hãy tưởng tượng bạn vừa nhận một nhân viên thực tập mới vào phòng:
* Ngày thứ 2: Bạn phải đứng kế bên chỉ: *"Lấy file Excel này, đổi font chữ, tính tổng cột D, vẽ biểu đồ nhé."*
* Ngày thứ 3: Bạn lại phải nhắc lại y chang những câu đó.
* Ngày thứ 4: Vẫn phải nhắc lại!

Dùng ChatGPT thông thường cũng mệt mỏi hệt như vậy: mỗi lần mở ra bạn lại phải viết một prompt dài dằng dặc để giải thích cách làm.
**Tại sao bạn không hướng dẫn cho nó một lần duy nhất vĩnh viễn?** Đó chính là bản chất của **Skill (Kỹ năng)** trong Antigravity.

---

## 1. Cấu Trúc của Một Skill Thực Tế
Thực chất, một Skill không có gì cao siêu hay phức tạp. Nó chỉ là một thư mục nằm trong máy tính của bạn với cấu trúc chuẩn:

* 📁 `ten-ky-nang/`
  * 📄 `SKILL.md`: Tệp văn bản viết bằng ngôn ngữ tự nhiên, mô tả chi tiết:
    * *Kỹ năng này làm nhiệm vụ gì?* (Description)
    * *Khi nào thì nên kích hoạt?* (Triggers)
    * *Các bước xử lý cụ thể ra sao?* (Instructions)
  * 📁 `scripts/` *(Tùy chọn)*: Thư mục chứa các đoạn mã tự động (Python, PowerShell) nếu kỹ năng đó cần chạy các tác vụ nâng cao.

---

## 2. Điểm "Vi Diệu": Cơ Chế Tự Động Nhận Diện (Auto-Discovery)
Trong Antigravity, bạn **không cần phải gõ lệnh gọi tên từng skill một cách thủ công**.
* Hệ thống sở hữu cơ chế **Auto-Discovery**: Mỗi khi bạn gõ bất kỳ yêu cầu nào, Antigravity sẽ tự động quét qua toàn bộ thư mục kỹ năng.
* Nếu yêu cầu của bạn khớp với phần mô tả trong file `SKILL.md`, AI sẽ **tự động kích hoạt** kỹ năng tương ứng để xử lý ngay lập tức!

---

## 3. Phân Biệt: Workspace Skill vs Global Skill

Đây là một điểm cực kỳ thông minh trong quản lý công việc:

| Loại Skill | Ví von đời thường | Phạm vi hoạt động | Khi nào nên dùng? |
| :--- | :--- | :--- | :--- |
| **Workspace Skill** *(Dự án riêng)* | Giống như **máy hút bụi mua bằng tiền riêng của Nhà A** (chỉ Nhà A được dùng). | Chỉ có tác dụng bên trong thư mục dự án đó. | Cho các nghiệp vụ đặc thù của từng phòng ban hoặc dự án cụ thể. |
| **Global Skill** *(Kỹ năng toàn cục)* | Giống như **cột đèn đường công cộng** giữa hai nhà (ai cũng hưởng lợi). | Có tác dụng trên **mọi** thư mục và dự án trên máy tính của bạn. | Cho các kỹ năng dùng chung hàng ngày (như sửa lỗi chính tả tiếng Việt, trích xuất bảng từ PDF...). |

---

## 4. Mối Quan Hệ Giữa Rule và Skill
* **Rule là người đặt luật:** Trong một dự án chỉ cần **1 Rule chung** (Ví dụ: Không được xóa file gốc, luôn giữ định dạng thương hiệu).
* **Skill là người làm chuyên môn:** Một dự án có thể có **hàng chục Skill** (Skill làm báo cáo Excel, Skill viết email, Skill cào dữ liệu).
* Mọi Skill khi hoạt động đều tự động "lắng nghe" và tuân thủ tuyệt đối theo Rule chung của dự án.

---

## ⚙️ Quản lý Skill ở đâu trên giao diện?
Bạn chỉ cần mở phần mềm Antigravity, nhìn vào biểu tượng bánh răng **Settings** (Cài đặt) → chọn mục **Customizations** để xem, bật/tắt toàn bộ danh sách Rule và Skill của mình.
