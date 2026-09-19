# AniBox — Bản phát hành chính thức

Ứng dụng Android TV xem anime, phim bộ, phim lẻ, kênh truyền hình trực tiếp và kho giải trí 18+ được bảo vệ bằng mã PIN. Repo này là cổng phát hành công khai, chỉ chứa **bản cài đặt** (APK), mã kiểm tra tính toàn vẹn `SHA256SUMS.txt` và `version.json` để app tự động kiểm tra và cập nhật trực tiếp trên TV.

---

## Tải về bản cài đặt chuẩn hóa

| Tên file APK | Phiên bản | Tương thích | Tính năng |
|---|---|---|---|
| **AniBox-v2.8.0.apk** | 2.8.0 (Build 11) | Android 6.0+ (TV, Box, Fire TV Stick) | **Bản đầy đủ chuẩn hóa duy nhất**: Đầy đủ bộ giải mã ExoPlayer + libVLC (AC3/DTS/EAC3/HEVC 10-bit) + dịch phụ đề AI offline, Top Pill Bar Netflix, Instant Play. |

- Bản phát hành mới nhất: **[Releases](../../releases/latest)**
- Kiểm tra mã băm bảo mật SHA-256 đối chiếu trong file `SHA256SUMS.txt`.

---

## Hướng dẫn cài đặt lên Android TV / Fire TV bằng Downloader (by AFTVnews)

Ứng dụng **Downloader** là cách nhanh nhất và tiện lợi nhất để cài đặt AniBox trực tiếp trên Android TV mà không cần cắm USB hay máy tính:

1. **Cài Downloader**: Vào kho ứng dụng trên TV (**Google Play Store** hoặc **Amazon Appstore**), tìm và cài đặt ứng dụng **Downloader**.
2. **Cấp quyền cài ứng dụng**:
   - Vào *Cài đặt TV* → *Bảo mật & Hạn chế* (hoặc *Quyền riêng tư*) → *Cài đặt ứng dụng không rõ nguồn gốc* → Bật **Cho phép** (Allow) cho ứng dụng **Downloader**.
3. **Tải và cài AniBox**:
   - Mở ứng dụng **Downloader** trên TV.
   - Tại ô nhập URL ở trang chủ Downloader, nhập trực tiếp đường dẫn sau:
     ```text
     https://github.com/LongLeo287/AniBox-release/releases/latest/download/AniBox-v2.8.0.apk
     ```
   - Bấm **Go** để ứng dụng bắt đầu tải file về.
4. **Cài đặt**:
   - Sau khi tải xong, màn hình sẽ tự động hiện thông báo cài đặt → chọn **Cài đặt** (Install).
   - Cài xong chọn **Mở** (Open) để thưởng thức AniBox!

---

## Tự động kiểm tra & Cập nhật phiên bản mới

- AniBox tự động kiểm tra `version.json` khi mở app và hiển thị thông báo khi có bản cập nhật mới.
- Người dùng cũng có thể kiểm tra thủ công trong app: **Cài đặt → Cập nhật & dữ liệu → Kiểm tra cập nhật ngay**.

---

## Lưu ý

- Yêu cầu hệ điều hành Android TV 6.0 trở lên (API 23+). Android < 7.1 đã được tích hợp sẵn chứng chỉ số gốc ISRG Root X1 để mở kết nối HTTPS an toàn.
- Nội dung video được tổng hợp tự động từ các nguồn công khai; AniBox không lưu trữ hay phát tán bất kỳ tệp video nào trên máy chủ riêng.
