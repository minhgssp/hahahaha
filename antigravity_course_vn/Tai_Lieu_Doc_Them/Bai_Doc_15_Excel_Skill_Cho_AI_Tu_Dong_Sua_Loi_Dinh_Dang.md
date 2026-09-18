# Bài Đọc Thêm 15: Excel Skill Cho AI — Tự Động Sửa Lỗi Công Thức & Chuẩn Hóa Bảng Tính

> 📺 **Nguồn Video tham khảo:** [AI Văn Phòng #3: Excel Skill Cho AI | Tự Động Sửa Lỗi & Định Dạng](https://www.youtube.com/watch?v=BPhJifuAFps) (Thời lượng: 06:13 — Kênh PieLikeClaw)

![Excel Skill Cho AI](../assets/screenshots/video_frames/BPhJifuAFps_thumb.webp)

---

## ⚠️ 7 "Cái Bẫy" Chết Người Khi Để AI Thao Tác Với Excel

Khi xử lý các file bảng tính Excel chứa hàng nghìn dòng dữ liệu, nếu không có bộ kỹ năng ràng buộc, AI rất dễ mắc các sai lầm nghiêm trọng:

![Ảnh thực tế: 7 Quy tắc cốt lõi của Excel Skill từ video](../assets/screenshots/video_frames/BPhJifuAFps_frame_01-15.jpg)
> 📸 *Ảnh cắt từ video gốc (01:15): 7 quy tắc vàng giúp AI sửa Excel chuẩn xác: không hardcode công thức, định dạng Text cho số dài >15 số, bảo toàn vùng in và cấu trúc workbook.*

1. **Chuyển công thức sống thành số chết (Hardcode):** Thay vì giữ hàm tính toán (`=SUM(C2:C50)`), AI lại tự gõ số kết quả cứng vào ô, làm mất tính năng tự động nhảy số của bảng tính.
2. **Cắt cụt số dài trên 15 chữ số:** Các số tài khoản ngân hàng, mã số thuế, mã định danh nếu không được định dạng kiểu `Text` sẽ bị Excel tự động làm tròn hoặc chuyển thành dạng khoa học (`1.23E+11`).
3. **Phá vỡ vùng in (Print Area) & Bộ lọc (Filter):** Làm mất các thiết lập xem và in ấn mà kế toán/nhân sự đã dày công tạo trước đó.

---

## 🚀 Đóng Gói Bộ Kỹ Năng Excel Vào Antigravity

![Ảnh thực tế: AI phân tích và sửa lỗi logic công thức](../assets/screenshots/video_frames/BPhJifuAFps_frame_04-55.jpg)
> 📸 *Ảnh cắt từ video gốc (04:55): Antigravity đọc SkillExcel.md, phân biệt rạch ròi giữa ô Input (màu xanh) và ô Công thức (in đậm), đồng thời tự động sửa lỗi logic công thức thay vì gõ số cứng.*

![Ảnh thực tế: Bảng tính Excel hoàn thiện mở trên Microsoft Excel](../assets/screenshots/video_frames/BPhJifuAFps_frame_05-35.jpg)
> 📸 *Ảnh cắt từ video gốc (05:35): Bảng tính sau khi AI xử lý được định dạng tiền tệ chuyên nghiệp, sạch đẹp và không còn lỗi số mũ khoa học.*

* **Cách thức:** Nạp tệp quy tắc `excel_skill.md` vào thư mục dự án của Antigravity.
* **Quy trình hoạt động:** Mỗi khi bạn yêu cầu AI tính toán hoặc chỉnh sửa file Excel, Antigravity sẽ tự động đọc bộ quy tắc này trước để:
  * Viết đúng cú pháp hàm Excel.
  * Giữ nguyên cấu trúc các Sheet liên kết.
  * Tự động căn chỉnh độ rộng cột và tô màu xen kẽ giúp bảng tính dễ nhìn.
