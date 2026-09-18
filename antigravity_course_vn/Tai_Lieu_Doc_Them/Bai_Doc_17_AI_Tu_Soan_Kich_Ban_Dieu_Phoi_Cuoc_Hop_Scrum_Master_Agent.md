# Bài Đọc Thêm 17: AI Tự Soạn Kịch Bản Mọi Cuộc Họp — Xây Dựng Scrum Master & Meeting Agent

> 📺 **Nguồn Video tham khảo:** [AI Văn Phòng #5: AI Tự Viết Script Cho Mọi Cuộc Họp | Scrum Master Agent](https://www.youtube.com/watch?v=xLehvqex9gc) (Thời lượng: 09:04 — Kênh PieLikeClaw)

![Tài liệu Scrum Master Sprint Ceremonies Guide](../assets/screenshots/video_frames/xLehvqex9gc_01-45.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ video (mốc 01:45): Tài liệu chuẩn hóa nghi thức Scrum Master Sprint Ceremonies Guide (.docx) và khung kịch bản Facilitator Script.*

---

## 😫 Áp Lực "Họp Triền Miên" Của Người Quản Lý & Điều Phối

Trong môi trường doanh nghiệp hiện đại, những người làm quản lý, Scrum Master hay Project Manager (PM) thường phải chủ trì hàng chục cuộc họp mỗi tuần:
* **Daily Standup:** Họp nhanh đầu ngày 15 phút.
* **Sprint Planning:** Lập kế hoạch 2 tuần cho toàn đội ngũ.
* **Sprint Demo / Showcase:** Trình diễn sản phẩm cho Ban giám đốc & Stakeholders.
* **Retrospective (Họp rút kinh nghiệm):** Nhìn nhận việc làm tốt & chưa tốt.
* **PI Planning:** Lập kế hoạch chiến lược 3 tháng.

Chuẩn bị kịch bản dẫn dắt (Facilitation Script), đặc biệt là các cuộc họp bằng tiếng Anh với lãnh đạo nước ngoài, thường tiêu tốn hàng giờ đồng hồ và gây căng thẳng tâm lý.

![Tự động hóa xây dựng Prompt từ tài liệu nghiệp vụ](../assets/screenshots/video_frames/xLehvqex9gc_04-45.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ video (mốc 04:45): Ra lệnh cho AI tự phân tích tài liệu nghiệp vụ để sinh ra file prompt chuẩn hóa điều phối cuộc họp.*

---

## 🤖 Giải Pháp: Xây Dựng POM (Prompt Object Model) Cho Scrum Master

Thay vì mỗi lần họp lại gõ một prompt rời rạc, tác giả đóng gói thành một file prompt chuẩn mực `.prompt.md`:

![Cấu trúc file scrum-master-prep.prompt.md](../assets/screenshots/video_frames/xLehvqex9gc_06-05.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ video (mốc 06:05): Cấu trúc file prompt chuẩn POM gồm: Thông tin đầu vào & Yêu cầu đầu ra (Agenda timebox, Facilitator Script, Báo cáo tóm tắt, Checklist chuẩn bị).*

### Cấu trúc 5 phần của một Kịch bản Cuộc họp Chuẩn:
1. **Opening (Chào mừng & Giới thiệu bối cảnh):** Lời chào lịch sự, nêu rõ mục tiêu cuộc họp và cảm ơn các bên liên quan đã dành thời gian.
2. **Sprint Highlights (Tổng kết thành tựu):** Tóm tắt nhanh những hạng mục quan trọng đã hoàn thành trong kỳ (Velocity, Story points).
3. **Showcase Transitions (Dẫn dắt thuyết trình):** Lời chuyển giao mạch lạc giữa các thành viên lên trình bày từng tính năng/kết quả.
4. **Stakeholder Feedback (Thu thập phản hồi):** Đặt câu hỏi gợi mở để Lãnh đạo và các bên liên quan góp ý mang tính xây dựng.
5. **Action Items & Closing (Tổng kết & Giao việc):** Chốt lại các việc cần làm tiếp theo, rủi ro cần phòng ngừa và kết thúc cuộc họp đúng giờ.

---

## 🚀 Thực Thi Trực Tiếp Trong Antigravity IDE

Chỉ cần gọi file prompt đã tạo và nạp thông tin cuộc họp trong Antigravity:

![Gọi file prompt Scrum Master trong Antigravity](../assets/screenshots/video_frames/xLehvqex9gc_07-35.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ video (mốc 07:35): Thao tác gõ `@scrum-master-prep.prompt.md` trong Antigravity IDE.*

### Kết Quả Nhận Được Chỉ Sau 3 Phút:

![AI xuất Agenda 60 phút và Facilitator Script chi tiết](../assets/screenshots/video_frames/xLehvqex9gc_08-35.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ video (mốc 08:35): AI tạo hoàn chỉnh Agenda 60 phút phân bổ từng mốc thời gian và Facilitator Script từng lời thoại cho người điều phối.*

---

## 💡 Bài Học Thực Chiến Cho Dân Công Sở
* **Chỉ mất 3 phút trước giờ G:** Bạn chỉ cần gõ `@scrum-master-prep.prompt.md [Loại cuộc họp]`, AI sẽ xuất ngay một kịch bản song ngữ (Việt - Anh) sắc sảo để bạn tự tin làm chủ phòng họp.
* **AI là "chiếc phao cứu sinh" về ngôn ngữ:** Giúp người không giỏi tiếng Anh tự tin dẫn dắt các cuộc họp quốc tế chuyên nghiệp mà không còn nỗi sợ "nói vấp hay bí từ".
