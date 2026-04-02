# Module 2.2: Phân tích Dữ liệu (Data Analysis)

Chào mừng trở lại!
Ở Module 2.1, bạn đã lập kế hoạch sự kiện.
Hôm nay, bạn có trước mặt **4 bộ dữ liệu thực** từ TaskFlow Q4. Sếp Alex muốn biết: "Tại sao người dùng mới không gắn bó? Có nên đầu tư cải thiện Onboarding không?"

Bạn sẽ dùng Antigravity để phân tích từ dữ liệu thô → insight → báo cáo chuyên nghiệp.

**STOP: Bạn đã sẵn sàng làm Data Analyst chưa? (Gõ: Sẵn sàng)**

**USER: Sẵn sàng**

---

## Phần 1: Làm quen với Dữ liệu Doanh số (Descriptive)

Trước tiên, hãy khởi động bằng file đơn giản nhất.

**Bước 1: Đọc hiểu cấu trúc**

**STOP: Gõ lệnh: "Đọc 5 dòng đầu của file @Sales_Data.csv để hiểu cấu trúc dữ liệu"**

**USER: Gõ lệnh**

**ACTION: Read first 5 lines**

---

Bạn thấy gì? Cột Date, Region, SalesPerson, Product, Revenue, Cost, SatisfactionScore.
Antigravity đã hiểu cấu trúc. Giờ hãy hỏi các câu tổng quan.

**Bước 2: Phân tích mô tả (Descriptive)**

**STOP: Gõ lệnh: "Tính tổng doanh thu (Revenue) trong quý 1, ai là người có doanh thu cao nhất, và vẽ biểu đồ cột so sánh doanh thu theo vùng (North, South, East, West)"**

**USER: Gõ lệnh**

**ACTION: Calculate revenue + chart**

---

**Bước 3: Phân tích chẩn đoán (Diagnostic)**

Sếp Mike thắc mắc: "Tại sao vùng West thấp thế?"

**STOP: Gõ lệnh: "Phân tích số liệu của Lisa ở vùng West. Tại sao doanh thu thấp? Có phải do bán ít hay do chỉ số SatisfactionScore thấp?"**

**USER: Gõ lệnh**

**ACTION: Analyze Lisa's data**
(AI phát hiện Lisa có SatisfactionScore < 4.0 → Khách hàng không hài lòng.)

---

Bạn vừa hoàn thành vòng phân tích cơ bản: Dữ liệu → Mô tả → Chẩn đoán.
Nhưng đây mới chỉ là 21 dòng dữ liệu. Thực tế, PM phải xử lý hàng nghìn bản ghi.

---

## Phần 2: Phân tích Dữ liệu Khảo sát (800 phản hồi)

Sếp Alex cho biết: "Đội Product vừa khảo sát 800 người dùng mới về trải nghiệm Onboarding. Hãy tìm ra vấn đề chính."

**STOP: Gõ lệnh: "Đọc file @user-survey-responses.csv. Cho tôi biết: 1) Có bao nhiêu phản hồi? 2) Các cột dữ liệu là gì? 3) Phân loại feedback theo nhóm feature_request và đếm số lượng từng nhóm."**

**USER: Gõ lệnh**

**ACTION: Analyze survey data**

---

Thú vị phải không? 800 phản hồi mà bạn không cần đọc từng dòng.
Giờ hãy kết hợp thêm dữ liệu NPS.

**STOP: Gõ lệnh: "Phân tích điểm NPS trung bình theo từng nhóm feature_request và theo company_size. Nhóm nào có NPS thấp nhất? Công ty lớn hay nhỏ bị ảnh hưởng nhiều hơn?"**

**USER: Gõ lệnh**

**ACTION: NPS breakdown**

---

Bạn vừa dùng AI để phân tích dữ liệu định tính (khảo sát) — điều mà Excel rất khó làm. Đây là sức mạnh thực sự của Antigravity.

---

## Phần 3: Phân tích Phễu Chuyển đổi (10.000 users)

Sếp Alex muốn biết: "Bao nhiêu phần trăm người đăng ký thực sự trở thành người dùng tích cực?"

**STOP: Gõ lệnh: "Đọc @activation-funnel-q4.csv. Tính tỷ lệ chuyển đổi qua từng bước của phễu: signup → created_first_task → completed_first_task → invited_teammate. Hiển thị dưới dạng bảng phần trăm."**

**USER: Gõ lệnh**

**ACTION: Funnel analysis**

---

Đây là phễu chuyển đổi (Conversion Funnel) — công cụ phân tích quan trọng nhất của Product Manager.
Hãy đào sâu: Bước nào mất người nhiều nhất?

**STOP: Gõ lệnh: "Vẽ biểu đồ phễu (funnel chart) cho 4 bước trên. Cho biết bước nào có tỷ lệ rơi (drop-off) lớn nhất — đó chính là nút thắt cần tối ưu."**

**USER: Gõ lệnh**

**ACTION: Funnel visualization**

---

## Phần 4: Ước lượng Tác động (Impact Estimation)

Bạn đã biết vấn đề (Onboarding yếu) và có số liệu. Giờ là lúc trả lời câu hỏi quan trọng nhất của CEO: **"Nếu sửa, đáng bao nhiêu tiền?"**

**STOP: Gõ lệnh: "Đọc @taskflow-usage-data-q4.csv và @impact-estimation-framework.md. Sử dụng khung Impact Estimation với phương pháp 3 kịch bản (Bi quan, Thực tế, Lạc quan) để ước lượng tác động kinh doanh nếu cải thiện tỷ lệ kích hoạt (activation rate). Trình bày dưới dạng bảng so sánh."**

**USER: Gõ lệnh**

**ACTION: Impact estimation**

---

Tuyệt vời! Bạn vừa kết hợp **4 nguồn dữ liệu** (Sales, Khảo sát, Phễu, Chỉ số kinh doanh) + 1 framework phân tích để tạo ra một bức tranh toàn cảnh.

---

## Phần 5: Đóng gói Báo cáo HTML

Giờ hãy biến tất cả thành sản phẩm chuyên nghiệp gửi CEO.

**STOP: Gõ lệnh: "Tổng hợp tất cả phân tích và biểu đồ nãy giờ thành một file báo cáo `baocao_onboarding_q4.html`. Gồm: 1) Executive Summary, 2) Phân tích phễu chuyển đổi, 3) Insight từ khảo sát, 4) Ước lượng tác động 3 kịch bản, 5) Đề xuất giải pháp. Thiết kế đẹp, hiện đại."**

**USER: Gõ lệnh**

**ACTION: Create HTML Report**

(Mở file HTML đó lên và chiêm ngưỡng. Đó là đẳng cấp **AI/Automation PM**.)

---

## Tổng kết

Bạn đã đi qua chuỗi phân tích hoàn chỉnh:

| Bước        | Dữ liệu                                                         | Kỹ năng Antigravity       |
| ----------- | --------------------------------------------------------------- | ------------------------- |
| 1. Mô tả    | `Sales_Data.csv` (21 dòng)                                      | @ mention, phân tích số   |
| 2. Khảo sát | `user-survey-responses.csv` (800 phản hồi)                      | Phân tích định tính, NPS  |
| 3. Phễu     | `activation-funnel-q4.csv` (10.000 users)                       | Xử lý dữ liệu lớn, funnel |
| 4. Tác động | `taskflow-usage-data-q4.csv` + `impact-estimation-framework.md` | Kết hợp đa nguồn, ROI     |
| 5. Báo cáo  | Tất cả                                                          | HTML report chuyên nghiệp |

Không cần Excel. Không cần PowerBI. Chỉ cần tư duy.

Bài tiếp theo, chúng ta sẽ học cách viết những bản báo cáo chiến lược nặng đô hơn.

**STOP: Gõ `/start-2-3` để đi tiếp.**
