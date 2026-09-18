# Bài đọc thêm 05: Xây dựng website giáo dục với NotebookLM và Antigravity

> 📺 **Nguồn video tham khảo:** [Cách xây dựng Website giáo dục từ A-Z với Antigravity và NotebookLM](https://www.youtube.com/watch?v=_mX7MidD2Jc) (Thời lượng: 2:45:05 — Chia sẻ bởi Hoàng Đức Minh & cộng đồng)

![Xây dựng Website Giáo dục cùng NotebookLM và Antigravity](../assets/screenshots/video_frames/_mX7MidD2Jc_thumb.webp)

---

## 💡 Triết lý cốt lõi: Kiểm soát và hạn chế ảo giác tri thức (Grounding)

Khi xây dựng một sản phẩm giáo dục hoặc đào tạo, rủi ro lớn nhất của AI là **"bịa chuyện" (ảo giác - hallucination)**. 

Trong buổi chia sẻ, giải pháp được diễn giả Hoàng Đức Minh và cộng đồng áp dụng là quy trình kết hợp hai công cụ bổ trợ của Google:

$$\text{NotebookLM (Kiểm định và đối chiếu tài liệu nguồn)} \longrightarrow \text{Antigravity (Tổ chức dữ liệu & Triển khai giao diện)}$$

---

## 1. NotebookLM: "Bộ lọc đối chiếu nguồn chuẩn xác" (Source Grounding)

![Website học liệu giáo dục được xây dựng từ tài liệu chuẩn](../assets/screenshots/video_frames/vd5_notebooklm_pipeline.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ buổi chia sẻ: Cổng học liệu giáo dục 'Khám phá đại dương' (haitrinh.org) được xây dựng từ nguồn tư liệu chuẩn mực của UNESCO.*

* **Tại sao cần NotebookLM?** Khác với các chatbot tìm kiếm mở trên mạng (dễ dẫn nguồn sai lệch), NotebookLM trả lời dựa trên **chính xác các tài liệu bạn nạp vào** (sách chuyên khảo, giáo trình, bài báo nghiên cứu, tài liệu khoa học).
* **Quy tắc chọn nguồn uy tín:** Trong video, diễn giả chia sẻ kinh nghiệm: ưu tiên sử dụng các nguồn tài liệu uy tín (như báo cáo khoa học, tổ chức nghiên cứu quốc tế, tài liệu chuyên ngành...) để làm nguồn "gốc rễ" cho bài giảng.
* **Đầu ra:** Bản tóm tắt kiến thức có đối chiếu và số trang trích dẫn cụ thể.

---

## 2. Antigravity: "Công cụ kiến tạo sản phẩm và quản lý tài liệu"

Sau khi đã có nội dung được đối chiếu từ NotebookLM, bạn nạp cấu trúc bài học sang Antigravity để biến thành sản phẩm thực tế:

![Cấu trúc bộ nhớ dự án trong Antigravity IDE](../assets/screenshots/video_frames/vd5_edu_website_demo1.jpg)
> 📸 *Ảnh chụp màn hình thực tế từ buổi chia sẻ: Quản lý kiến trúc tài liệu và bộ nhớ dự án (MEMORY.md) trực tiếp trong Antigravity IDE.*

* **Tự động hóa xây dựng trang học liệu:** Antigravity có thể hỗ trợ tạo nhanh các mẫu layout giới thiệu khóa học, nội dung bài giảng và bài tập tương tác.
* **Phối hợp hình ảnh tư liệu và đồ họa:**
  * *Thông tin & bằng chứng thực tế:* Dùng dữ liệu và hình ảnh tư liệu thực tế để tạo sự tin cậy.
  * *Hình ảnh minh họa khái niệm:* Sử dụng các mô hình tạo ảnh AI tích hợp sẵn để vẽ biểu tượng chủ đề theo đúng tông màu bài học.
* **Quản trị dễ dàng:** Toàn bộ nội dung khóa học được tổ chức thành các file văn bản Markdown hoặc HTML tĩnh. Bạn có thể mở sửa trực tiếp ngay trong Antigravity IDE.

---

## 🎯 Bài học ứng dụng cho bạn

1. **Chuẩn bị nguồn dữ liệu tin cậy:** Luôn chuẩn bị tài liệu gốc rõ ràng để đối chiếu (Grounding), giúp AI bám sát dữ liệu thật.
2. **Dùng Antigravity để hiện thực hóa:** Biến tài liệu văn bản thành trang học liệu trực quan, bài thuyết trình tương tác và hệ thống bài tập thực hành cho người học.
