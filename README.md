# AniBox — Bản phát hành chính thức

Ứng dụng Android TV xem anime, phim bộ, phim lẻ, kênh truyền hình trực tiếp và kho giải trí 18+ được bảo vệ bằng mã PIN. Repo này là cổng phát hành công khai, chỉ chứa **bản cài đặt** (APK), mã kiểm tra tính toàn vẹn SHA256SUMS.txt và ersion.json để app tự động kiểm tra và cập nhật trực tiếp trên TV.

---

## ⚡ CÀI ĐẶT NHANH TRÊN ANDROID TV / FIRE TV (QUA DOWNLOADER)

Không cần gõ link dài ngoằng trên remote TV! Bạn chỉ cần nhập đúng **mã số ngắn** (Downloader Short Code) vào app Downloader:

| Phương thức | Mã nhập trên Downloader | Thao tác |
|---|---|---|
| **Mã số nhanh (Khuyên dùng)** | **9151756** | Mở **Downloader**, gõ số **9151756** vào ô URL rồi bấm **Go** (tự động đếm ngược 5s và tải ngay) |
| **Link rút gọn (Dự phòng 1)** | ftv.news/9151756 | Gõ ftv.news/9151756 vào ô URL rồi bấm **Go** |
| **Link rút gọn (Dự phòng 2)** | 	inyurl.com/anibox-app | Gõ 	inyurl.com/anibox-app vào ô URL rồi bấm **Go** |

### Các bước cài đặt chi tiết:
1. **Cài Downloader**: Vào kho ứng dụng trên TV (**Google Play Store** hoặc **Amazon Appstore**), tìm và cài đặt app **Downloader** (biểu tượng màu cam của AFTVnews).
2. **Cấp quyền cài ứng dụng**:
   - Vào *Cài đặt TV* → *Bảo mật & Hạn chế* (hoặc *Ứng dụng & Quyền riêng tư*) → *Cài đặt ứng dụng không rõ nguồn gốc* → Bật **Cho phép** (Allow) cho ứng dụng **Downloader**.
3. **Tải và cài AniBox**:
   - Mở app **Downloader** trên TV.
   - Tại ô nhập URL/Search ngay trang chủ Downloader, dùng remote gõ đúng mã số: **9151756**.
   - Bấm **Go**. App sẽ tự động tải file AniBox-v2.8.0.apk về máy.
   - Sau khi tải xong, chọn **Install** (Cài đặt) → Cài xong chọn **Open** (Mở).

---

## Tải trực tiếp APK (Dành cho máy tính / USB)

| Tên file APK | Phiên bản | Tương thích | Kích thước |
|---|---|---|---|
| **AniBox-v2.8.0.apk** | 2.8.0 (Build 11) | Android 6.0+ (TV, Box, Fire TV Stick) | ~258 MB |

- **Link tải trực tiếp**: [Tải AniBox-v2.8.0.apk](https://github.com/LongLeo287/AniBox-release/releases/latest/download/AniBox-v2.8.0.apk)
- **Bản phát hành mới nhất**: [Releases](../../releases/latest)
- **Bảo mật**: Đối chiếu mã băm SHA-256 trong file SHA256SUMS.txt.

---

## Tự động kiểm tra & Cập nhật phiên bản mới

- AniBox tự động kiểm tra ersion.json khi mở app và hiển thị thông báo khi có bản cập nhật mới.
- Người dùng cũng có thể kiểm tra thủ công trong app: **Cài đặt → Cập nhật & dữ liệu → Kiểm tra cập nhật ngay**.

---

## Lưu ý

- Yêu cầu hệ điều hành Android TV 6.0 trở lên (API 23+). Android < 7.1 đã được tích hợp sẵn chứng chỉ số gốc ISRG Root X1 để mở kết nối HTTPS an toàn.
- Nội dung video được tổng hợp tự động từ các nguồn công khai; AniBox không lưu trữ hay phát tán bất kỳ tệp video nào trên máy chủ riêng.