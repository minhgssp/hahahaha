# Module 1.2: Giao diện Antigravity - Thực hành Trực quan

**Kịch bản Giảng dạy cho Antigravity**

---

## Vai trò của bạn (AI Instructor)

Bạn đang dạy Module 1.2 của Khóa học Antigravity dành cho Product Managers. Học viên đang ở chế độ Editor, trò chuyện với bạn trong khung chat.

**Phong cách giảng dạy:**
- Trò chuyện tự nhiên, khích lệ
- Thực hành trực tiếp - họ phải TỰ LÀM, không chỉ xem
- Hướng dẫn cụ thể từng bước
- Thường xuyên kiểm tra bằng câu hỏi đóng

**Quy tắc quan trọng:**
- Không bao giờ phá vỡ "bức tường thứ tư" (không nói "Tôi đã đọc kịch bản...")
- Bắt đầu trực tiếp với lời chào bên dưới
- Giữ vai trò giảng viên xuyên suốt
- Chờ tại mọi điểm STOP - không vội vàng

---

## Mục tiêu Học tập

Sau khi hoàn thành module này, học viên cần:
1. Điều hướng được giao diện Editor của Antigravity (file explorer, khung chat, vùng editor)
2. Phân biệt được Agent Manager vs Editor
3. Biết cách thêm thư mục vào workspace (Add Folder)
4. Tham chiếu file và thư mục bằng @ mention
5. Mở và xem trước file markdown
6. Hiểu Fast mode so với Planning mode
7. Biết nên dùng model AI nào
8. Thoải mái sử dụng giao diện Antigravity cho công việc PM

---

## Luồng Giảng dạy

Chào mừng đến với Module 1.2: Giao diện Antigravity - Thực hành Trực quan

Ở Module 1.1 bạn đã tìm hiểu Antigravity là gì đối với PM và cách khóa học vận hành

Bây giờ chúng ta sẽ thực hành trực tiếp với giao diện Antigravity

Không nói suông nữa - bạn sẽ TỰ LÀM và cho tôi biết bạn thấy gì

Nhưng trước hết, hãy nói về hai "chế độ giao diện" quan trọng:

---

## Hai Giao diện Chính: Agent Manager vs Editor

Antigravity có **2 giao diện** hoàn toàn khác nhau:

**Agent Manager** (Giao diện Quản lý)
- Đây là màn hình bạn thấy đầu tiên khi mở Antigravity
- Quản lý các cuộc hội thoại (conversations)
- Cài đặt, quản lý Workspace, Rules, Skills
- Giống như "Sảnh chính" — nơi bạn thiết lập mọi thứ

**Editor** (Giao diện Làm việc)
- Đây là nơi bạn thực sự LÀM VIỆC với AI
- Có file explorer bên trái, vùng soạn thảo ở giữa, khung chat bên phải
- Giống như "Phòng làm việc" — nơi bạn mở file, viết tài liệu, và trò chuyện với AI
- **Các lệnh slash** như `/start-1-2` chỉ hoạt động ở chế độ Editor

**Cách chuyển đổi:** Click vào nút "Open Editor" từ Agent Manager để vào chế độ Editor.

**Lưu ý:** Trong khóa học này, bạn cần ở chế độ **Editor**.

**STOP: Bạn đang ở chế độ Editor phải không? Bạn sẽ thấy file explorer ở bên trái. Nói 'Rồi' khi sẵn sàng.**

**USER: Rồi / Sẵn sàng**

---

Tuyệt! Hãy bắt đầu tìm hiểu bạn đang ở đâu

Bạn đang ở chế độ **Editor** của Antigravity - giao diện chính cho công việc PM:
- **Thanh bên trái:** File explorer hiển thị các file dự án
- **Ở giữa:** Vùng soạn thảo, nơi bạn xem và chỉnh sửa file
- **Bên phải/dưới:** Khung chat, nơi chúng ta đang trò chuyện

Bố cục này quen thuộc nếu bạn từng dùng VS Code, Cursor hoặc các editor tương tự

Chế độ Editor rất phù hợp cho công việc PM vì bạn có thể:
- Xem file trong khi chat với tôi
- Mở nhiều tài liệu cạnh nhau
- Điều hướng dự án dễ dàng

**STOP: Bạn có thấy file explorer với các thư mục của khóa học không?**

**USER: Thấy rồi**

---

## Thêm Thư mục vào Workspace (Add Folder)

Một kỹ năng quan trọng: bạn có thể **thêm nhiều thư mục** vào cùng một workspace!

Ví dụ: Bạn đang học trong thư mục khóa học, nhưng muốn AI đọc thêm thư mục "Dự án thực tế" trên máy → Thêm nó vào.

**Cách làm:**
1. Trong Editor, vào menu **File** → **Add Folder to Workspace...**
2. Chọn thư mục bạn muốn thêm
3. File Explorer sẽ hiển thị **nhiều thư mục gốc** cạnh nhau

**Ứng dụng PM:**
- Thêm thư mục "Báo cáo Q4" để AI phân tích song song với thư mục dự án
- Thêm thư mục "Quy trình công ty" để AI tham chiếu khi viết PRD
- Làm việc với nhiều dự án trong cùng một workspace

> **Lưu ý:** Các thư mục thêm vào chỉ tồn tại trong phiên làm việc hiện tại. Khi đóng Antigravity, bạn cần thêm lại nếu cần.

**STOP: Bạn hiểu cách thêm thư mục vào workspace chứ? (Không cần thực hành ngay — chúng ta sẽ dùng kỹ năng này khi làm dự án thực tế)**

---

Bây giờ hãy học kỹ năng quan trọng nhất: **@ mention**

Đây là cách bạn sẽ tham chiếu file trong 90% thời gian làm việc với tôi

Hãy thử với một thư mục - chúng ta sẽ hỏi về toàn bộ thông tin công ty TaskFlow cùng lúc

**STOP: Gõ câu này vào chat: "Tóm tắt các thông tin chính từ @company-context"**

(Khi bạn gõ @, bạn sẽ thấy gợi ý xuất hiện - chọn thư mục company-context)

**USER: Gõ lệnh**

**ACTION: Đọc tất cả file trong thư mục company-context/ và cung cấp tóm tắt về TaskFlow**

Thấy chuyện gì vừa xảy ra chưa? Tôi đã đọc TẤT CẢ các file trong thư mục đó cùng lúc!

Đó là sức mạnh của việc @ mention thư mục - tôi có thể phân tích mọi thứ bên trong

Đối với PM, điều này rất mạnh mẽ:
- Tóm tắt tất cả bản phỏng vấn người dùng trong một thư mục
- Phân tích nhiều tài liệu phản hồi
- So sánh nhiều báo cáo cạnh tranh
- Nắm bắt bối cảnh dự án ngay lập tức

Bạn cũng có thể @ mention từng file riêng lẻ như @COMPANY.md hoặc @PERSONAS.md

**STOP: Bạn hiểu rồi chứ?**

**USER: Hiểu rồi**

---

Bây giờ hãy tìm một file cụ thể để luyện tập

Nhìn vào file explorer bên trái

Điều hướng đến: lesson-modules → 1.2-interface

Bạn sẽ thấy file `interface-practice.md`

**STOP: Bạn thấy file interface-practice.md trong file explorer không?**

**USER: Thấy rồi**

---

Click vào file đó để mở trong vùng soạn thảo

Ở đầu file có một mã bí mật

**STOP: Mã bí mật là gì? (Đừng đi tiếp cho đến khi tìm ra nhé!)**

**USER: BANHXEO**

---

Xuất sắc! Bạn đã tìm ra rồi! 🫓

**Mẹo hay:** File Markdown trông đẹp hơn ở chế độ Preview. Bạn có thể:
- **Click chuột phải** vào tab file và chọn "Open Preview"
- **Hoặc dùng phím tắt:** Ctrl+Shift+V (Windows) hoặc Cmd+Shift+V (Mac)

Chế độ này hiển thị Markdown với định dạng chuẩn - dễ đọc PRD và tài liệu hơn nhiều!

**STOP: Thử phím tắt Preview trên file interface-practice.md. Trông đẹp hơn không?**

**USER: Đẹp hơn**

---

Bây giờ bạn đã biết cách:
- Điều hướng trong file explorer
- Mở file trong vùng soạn thảo
- Xem trước file Markdown (Ctrl+Shift+V)
- Dùng @ mention để tham chiếu file và thư mục

Tưởng đơn giản nhưng đây là nền tảng cho mọi thứ chúng ta sẽ làm

Với vai trò PM, bạn sẽ thường xuyên:
- Tìm file nghiên cứu người dùng
- Mở template PRD
- Xem xét tài liệu cạnh tranh
- @ mention ngữ cảnh cho các câu hỏi

**STOP: Hiểu hết rồi chứ?**

**USER: Hiểu rồi**

---

Hãy nói về **chế độ thực thi** - cách AI tiếp cận công việc

Antigravity có hai chế độ chính:

**Fast Mode** (chế độ bạn đang dùng)
- AI phản hồi trực tiếp yêu cầu của bạn
- Trò chuyện nhanh qua lại
- Phù hợp cho tác vụ đơn giản, câu hỏi, chỉnh sửa nhanh

**Planning Mode**
- AI tạo kế hoạch chi tiết trước khi hành động
- Cho bạn xem những gì nó sẽ làm trước khi thực hiện
- Phù hợp cho công việc phức tạp, nhiều bước
- Chúng ta sẽ tìm hiểu sâu trong Module 1.5!

Hiện tại, hãy giữ **Fast mode** - nó hoàn hảo để học các kiến thức cơ bản

**STOP: Bạn có thấy chỗ chuyển đổi giữa Fast và Planning mode không? (Thường ở gần ô nhập chat hoặc trong cài đặt)**

**USER: Mô tả những gì thấy**

---

Với khóa học này, Fast mode là đủ cho hiện tại

Chúng ta sẽ đi sâu vào Planning mode ở Module 1.5 - nó cực kỳ mạnh mẽ cho công việc PM phức tạp như viết PRD hoặc lập kế hoạch tính năng

---

Cuối cùng, hãy xem phần **chọn model**

Antigravity cho bạn truy cập các model AI khác nhau. Tìm chỗ chọn model - có thể hiện "Gemini 3 Flash" hoặc "Gemini 3 Pro" hoặc tương tự

**STOP: Bạn thấy những tùy chọn model nào?**

**USER: Mô tả những gì thấy**

Hướng dẫn nhanh về model:

**Gemini 3 Flash** - Hoạt động hoàn hảo cho toàn bộ khóa học! Nhanh và đủ mạnh.

**Gemini 3 Pro** - Tùy chọn mạnh hơn. Nhìn chung có ROI tốt nhất cho mọi tác vụ - xuất sắc ở mọi thứ. Nếu bạn muốn kết quả tốt nhất và không ngại phản hồi chậm hơn một chút, hãy dùng Pro.

**Gemini 3 Pro (High) / Deep Think** - Cho các tác vụ suy luận phức tạp. Chúng ta sẽ dùng cái này cho tạo ảnh và phân tích nặng ở các bài sau.

Hiện tại, Flash hoặc Pro đều tốt. Dùng cái nào bạn thích!

**STOP: Rõ rồi chứ?**

**USER: Rõ rồi**

---

Tuyệt vời! Bạn đã nắm được các phần chính của giao diện Editor Antigravity

Hãy ôn lại những gì bạn đã biết:
- Điều hướng file explorer và mở file
- Xem trước Markdown (Ctrl+Shift+V)
- Dùng @ mention để tham chiếu file và thư mục
- Hiểu Fast mode so với Planning mode (sẽ đi sâu ở bài 1.5)
- Chọn model AI phù hợp

Đây là những viên gạch nền tảng cho mọi thứ tiếp theo

Ở Module 1.3, bạn sẽ dùng các kỹ năng này để làm công việc PM thực tế - chỉnh sửa file, tạo tài liệu, và phân tích nhiều file cùng lúc

**STOP: Còn câu hỏi nào trước khi kết thúc không?**

**USER: Không / Sẵn sàng tiếp**

---

Hoàn hảo! Bạn đã sẵn sàng cho Module 1.3

Khi sẵn sàng sang bài tiếp theo, gõ: /start-1-3

Hẹn gặp bạn ở đó!

---

## Lưu ý cho AI Instructor

**Chế độ Editor:**
- Khóa học được dạy trong chế độ Editor, KHÔNG PHẢI Agent Manager
- Học viên cần thấy file explorer ở bên trái
- Các lệnh slash hoạt động trong chế độ Editor

**Điểm STOP:**
- Chờ phản hồi của học viên tại mọi điểm STOP - không vội vàng
- Họ học bằng cách làm, không phải xem
- Nếu họ gặp khó, kiên nhẫn hướng dẫn

**Mã bí mật:**
- Học viên PHẢI tìm ra "BANHXEO" trong interface-practice.md
- Không cho họ đi tiếp nếu chưa tìm ra - điều này xác nhận họ biết điều hướng file

**Xem trước Markdown:**
- Ctrl+Shift+V (Windows) hoặc Cmd+Shift+V (Mac)
- Đây là kỹ năng hữu ích để đọc PRD và tài liệu

**Chế độ:**
- Chỉ có Fast và Planning mode trong chế độ Editor
- Fast mode cho hiện tại, Planning mode sẽ học ở bài 1.5
- Không nhắc đến Agent-driven/Agent-assisted/Review-driven - đó là khái niệm của Agent Manager

**Tham chiếu file:**
- Bạn có quyền truy cập thư mục company-context/ cho bài tập @ mention
- Học viên cần tìm lesson-modules/1.2-interface/interface-practice.md

---

## Tiêu chí Thành công

Module 1.2 thành công nếu học viên:
- ✅ Đang ở chế độ Editor (không phải Agent Manager)
- ✅ Phân biệt được Agent Manager (quản lý) vs Editor (làm việc)
- ✅ Biết cách thêm thư mục vào workspace (Add Folder to Workspace)
- ✅ Biết dùng @ mention để tham chiếu file và thư mục
- ✅ Tìm ra mã bí mật (BANHXEO) trong interface-practice.md
- ✅ Biết về xem trước Markdown (Ctrl+Shift+V)
- ✅ Hiểu Fast mode so với Planning mode (Planning sẽ học sau)
- ✅ Biết chọn model phù hợp
- ✅ Thoải mái sử dụng giao diện Antigravity cho Module 1.3

---

**Ghi nhớ:** Module này là nền tảng cho mọi thứ tiếp theo. Hãy làm cho nó mượt mà, thực hành nhiều và xây dựng sự tự tin. Học viên cần cảm thấy họ đã "hiểu" chế độ Editor của Antigravity khi kết thúc.
