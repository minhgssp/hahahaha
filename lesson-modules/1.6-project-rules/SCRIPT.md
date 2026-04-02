# Module 1.6: Thiết lập Phong cách làm việc (Project Rules)

Chào mừng đến với Module 1.6! Đây là bài học quan trọng nhất để biến Antigravity từ một công cụ "biết tuốt" thành "trợ lý riêng" hiểu ý bạn.

Bạn có bao giờ thấy mệt khi phải nhắc đi nhắc lại với ChatGPT: *"Dùng tiếng Việt nhé"*, *"Tôi là Operations Lead"*, *"Sếp tôi tên Alex"*...?
Hôm nay chúng ta sẽ giải quyết triệt để vấn đề đó.

**STOP: Bạn đã sẵn sàng chưa? (Gõ: Sẵn sàng)**

**USER: Sẵn sàng**

---

Chúng ta sẽ làm một thí nghiệm: Yêu cầu AI làm cùng một việc 2 lần. Lần đầu không có quy tắc, lần sau có quy tắc.

Tình huống: Công ty TaskFlow vừa ra mắt chính sách "Làm việc từ xa (Remote Work) mới". Bạn cần viết thông báo gửi toàn công ty.

**STOP: Hãy gõ lệnh này: "Viết một email thông báo về chính sách Remote Work mới của công ty"**

**USER: Gõ lệnh**

**ACTION: Generate email_thong_bao_generic.md**
(Nội dung chung chung, có thể chêm tiếng Anh, không nhắc tên ai, giọng văn robot)

---

Xong! Hãy xem file vừa tạo.
Bạn thấy sao?
- Nó có biết công ty tên TaskFlow không? Không.
- Nó có biết Sếp bạn tên Alex không? Không.
- Giọng văn có vẻ hơi "máy móc"?
- Có thể nó còn chêm tiếng Anh "Remote Work Policy" lung tung?

Đó là vì tôi (AI) chưa biết gì về bạn cả. Tôi chỉ đoán mò.

**STOP: Bạn thấy nó chung chung quá đúng không?**

**USER: Đúng**

---

Bây giờ tôi sẽ chỉ cho bạn "Vũ khí bí mật".
Hãy nhìn vào thư mục `.agent/rules` ở cột bên trái.
(Nếu chưa có, chúng ta sẽ tạo nó).

Đây là nơi chứa các "Luật lệ" mà Antigravity **bắt buộc phải đọc** trước khi trả lời bạn. Nó giống như bộ nhớ dài hạn vậy.

**STOP: Hãy gõ lệnh này để thiết lập luật chơi: "Tạo file `.agent/rules/chuan_muc_lam_viec.md` chứa các quy tắc sau: 1. Luôn dùng Tiếng Việt chuyên nghiệp. 2. Tư duy thành tiếng (Think-out-loud) trước khi làm. 3. Sếp tổng là Alex, HR là Sarah."**

**USER: Gõ lệnh**

**ACTION: Create .agent/rules/chuan_muc_lam_viec.md**

---

Tuyệt vời! Bạn vừa tạo ra một "Hiến pháp" cho thư mục này.
Hãy mở file `chuan_muc_lam_viec.md` ra kiểm tra. Bạn sẽ thấy các quy tắc đã được ghi rõ.
Từ giờ trở đi, tôi sẽ luôn phải tuân thủ:
1.  **Tiếng Việt chuẩn:** Không teencode, không chêm tiếng Anh bừa bãi.
2.  **Think-out-loud:** Tôi phải giải thích kế hoạch (Tư duy) cho bạn nghe trước khi tôi viết file.
3.  **Nhân sự:** Tôi đã biết Alex và Sarah là ai.

**STOP: Bạn đã thấy file quy tắc chưa?**

**USER: Thấy rồi**

---

Bây giờ đến phần ma thuật.
Hãy gõ lại **Y HỆT** câu lệnh lúc nãy. Không thay đổi một chữ nào.

**STOP: Gõ lại: "Viết một email thông báo về chính sách Remote Work mới của công ty"**

**USER: Gõ lệnh**

**ACTION: Generate email_thong_bao_chuan.md**
(Lần này AI sẽ hiện ra dòng "Tư duy: Tôi cần viết email gửi Sarah và Alex...". Nội dung email sẽ dùng tiếng Việt chuẩn, nhắc đến TaskFlow, Alex, Sarah, giọng văn chuyên nghiệp).

---

Hãy xem kết quả mới (`email_thong_bao_chuan.md`).
Bạn thấy sự khác biệt chưa?
- Tôi đã tự động biết đây là TaskFlow.
- Tôi nhắc tên Sarah (HR) và Alex (CEO).
- Tôi giải thích (Think-out-loud) trước khi viết.
- Văn phong chuyên nghiệp hơn hẳn.

Đó chính là sức mạnh của **Project Rules**. Bạn chỉ cần dạy tôi một lần, tôi sẽ nhớ mãi mãi (trong dự án này).

**STOP: Bạn có thấy sự khác biệt rõ rệt không?**

**USER: Có / Rất rõ**

---

**Tổng kết Module 1.6:**
Bạn đã nắm được sức mạnh của Project Rules - "Hiến pháp" cho workspace.
Từ giờ, mỗi khi bắt đầu dự án mới, việc đầu tiên là thiết lập quy tắc.

Bài tiếp theo sẽ giúp bạn hiểu sâu hơn về 4 trụ cột của Antigravity: Knowledge, Workflow, Skill và Rule.

Để ăn mừng, hãy tạo một bức ảnh kỷ niệm nhé!

**STOP: Gõ lệnh: "Vẽ một bức ảnh vui nhộn về một nhân viên văn phòng đang thảnh thơi uống cà phê vì AI đã làm hết việc, phong cách hoạt hình 3D tươi sáng"**

**USER: Gõ lệnh**

**ACTION: Generate Image**

---

Tuyệt vời! Hãy lưu bức ảnh đó lại.
Khi nào bạn sẵn sàng cho thử thách tiếp theo, hãy bắt đầu Module 2.

**STOP: Gõ `/start-1-7` để đi tiếp.**
