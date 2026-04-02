# Khung Ước lượng Tác động (Impact Estimation Framework)

## Tổng quan

Khung này giúp PM ước lượng tác động kinh doanh của tính năng mới trước khi đầu tư thời gian kỹ thuật. Sử dụng nó để xây dựng mô hình ROI, hỗ trợ ra quyết định ưu tiên và thuyết phục ban lãnh đạo.

## Công thức

```
Tác động = Người dùng Ảnh hưởng × Tỷ lệ Hiện tại × Mức Tăng Dự kiến × Giá trị mỗi Hành động
```

### Phân tích công thức

**Người dùng Ảnh hưởng (Users Affected)**
- Bao nhiêu người dùng sẽ trải nghiệm tính năng này?
- Người dùng mới hàng tháng? Người dùng hiện tại sẽ áp dụng?
- Tính cả tỷ lệ áp dụng (adoption rate) — không phải ai cũng dùng mọi tính năng

**Tỷ lệ Hiện tại (Current Rate)**
- Chỉ số cơ sở (baseline) nào bạn đang muốn cải thiện?
- Tỷ lệ kích hoạt, tỷ lệ chuyển đổi, tỷ lệ giữ chân...
- Dùng dữ liệu lịch sử để xác định baseline

**Mức Tăng Dự kiến (Expected Lift)**
- Tính năng sẽ cải thiện chỉ số bao nhiêu?
- Biểu thị bằng điểm phần trăm (ví dụ: 45% → 55% = +10pp)
- Dựa trên: tính năng tương tự, đối thủ, dữ liệu ngành

**Giá trị mỗi Hành động (Value per Action)**
- Giá trị kinh doanh khi có thêm một người dùng chuyển đổi?
- LTV (Giá trị vòng đời), ACV (Giá trị hợp đồng hàng năm)
- Dùng mô hình của bộ phận tài chính hoặc dữ liệu lịch sử

## Phương pháp 3 Kịch bản

Không bao giờ trình bày một con số duy nhất cho lãnh đạo. Luôn mô hình hóa **3 kịch bản** để thể hiện phạm vi kết quả:

### Bi quan (Phân vị 20)
- Tỷ lệ áp dụng thận trọng
- Mức tăng khiêm tốn
- "Kịch bản xấu nhất, ROI vẫn dương"

### Thực tế (Phân vị 50)
- Dựa trên đánh giá tốt nhất
- Đây là kịch bản "cơ sở" (base case)
- "Đây là những gì chúng ta kỳ vọng"

### Lạc quan (Phân vị 80)
- Áp dụng mạnh, mức tăng cao
- "Nếu mọi thứ thuận lợi, đây là tiềm năng"

## Ví dụ Áp dụng

**Tính năng:** Onboarding Hướng dẫn với dự án mẫu

**Người dùng Ảnh hưởng:**
- 350 đăng ký mới/tháng
- Bi quan: 30% áp dụng (105 người dùng)
- Thực tế: 70% áp dụng (245 người dùng)
- Lạc quan: 90% áp dụng (315 người dùng)

**Tỷ lệ Hiện tại:**
- Baseline kích hoạt: 45%

**Mức Tăng Dự kiến:**
- Bi quan: +5pp (45% → 50%)
- Thực tế: +13pp (45% → 58%)
- Lạc quan: +17pp (45% → 62%)

**Giá trị mỗi Hành động:**
- LTV trung bình của người dùng đã kích hoạt: $850
- Người dùng kích hoạt ở lại lâu gấp 2.5 lần

**Tính ROI:**
```
Bi quan:  105 × 5pp × $850 = $4,460/tháng × 36 tháng = $161k trong 3 năm
Đầu tư:  $100k chi phí kỹ thuật → ROI: 1.6x

Thực tế:  245 × 13pp × $850 = $27k/tháng × 36 tháng = $972k trong 3 năm
Đầu tư:  $100k chi phí kỹ thuật → ROI: 9.7x

Lạc quan: 315 × 17pp × $850 = $45k/tháng × 36 tháng = $1.6M trong 3 năm
Đầu tư:  $100k chi phí kỹ thuật → ROI: 16x
```

## Nguyên tắc Chính

**Bảo thủ hơn là Lạc quan**
- Under-promise, over-deliver
- Kịch bản bi quan vẫn phải cho ROI dương nếu bạn khuyến nghị làm

**Minh bạch Giả định**
- Ghi rõ mọi giả định
- Dẫn nguồn dữ liệu
- Để mô hình có thể kiểm chứng được

**Cập nhật sau Triển khai**
- So sánh kết quả thực tế vs dự đoán
- Xây dựng uy tín theo thời gian

## Sai lầm Thường gặp

❌ **Ước lượng điểm đơn** — Luôn cho phạm vi
❌ **Thiên lệch lạc quan** — Trung thực về kết quả thực tế
❌ **Bỏ qua adoption** — Không phải ai cũng dùng mọi tính năng
❌ **Quên chi phí** — Tính cả thời gian kỹ thuật, bảo trì
❌ **Không xác minh** — Kiểm chứng giả định bằng dữ liệu khi có thể

---

**Nhớ:** Mục tiêu không phải dự đoán chính xác tuyệt đối. Mục tiêu là **tư duy nghiêm túc** về tác động và **truyền đạt phạm vi kết quả** để lãnh đạo ra quyết định sáng suốt.
