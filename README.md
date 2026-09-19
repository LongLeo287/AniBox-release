# AniBox — Bản phát hành chính thức

Ứng dụng Android TV xem anime, phim bộ, phim lẻ, kênh truyền hình trực tiếp và kho giải trí 18+ được bảo vệ bằng mã PIN. Repo này là cổng phát hành công khai, chỉ chứa **bản cài đặt** (APK), mã kiểm tra tính toàn vẹn SHA256SUMS.txt và ersion.json để app tự động kiểm tra và cập nhật trực tiếp trên TV.

---

## ⚡ CÀI ĐẶT NHANH TRÊN ANDROID TV / FIRE TV (QUA DOWNLOADER)

Không cần gõ link dài ngoằng trên remote TV! Chỉ cần nhập đúng **mã số ngắn vĩnh viễn** vào app Downloader:

| Phương thức | Mã nhập trên Downloader | Thao tác |
|---|---|---|
| **Mã số vĩnh viễn (Khuyên dùng)** | **3170287** | Mở **Downloader**, gõ đúng số **3170287** vào ô URL rồi bấm **Go** (tự động đếm ngược 5s và luôn tải bản mới nhất) |
| **Link rút gọn (Dự phòng 1)** | ftv.news/3170287 | Gõ ftv.news/3170287 vào ô URL rồi bấm **Go** |
| **Link rút gọn (Dự phòng 2)** | 	inyurl.com/anibox-latest | Gõ 	inyurl.com/anibox-latest vào ô URL rồi bấm **Go** |

> 🌟 **Lưu ý**: Mã số **3170287** là **mã vĩnh cửu** (trỏ tới bản phát hành mới nhất trên GitHub). Bất kể sau này AniBox có cập nhật lên phiên bản nào, bạn hay người dùng mới chỉ cần nhập đúng mã này là luôn luôn tải được bản cập nhật mới nhất!

### Các bước cài đặt chi tiết:
1. **Cài Downloader**: Vào kho ứng dụng trên TV (**Google Play Store** hoặc **Amazon Appstore**), tìm và cài đặt app **Downloader** (biểu tượng màu cam của AFTVnews).
2. **Cấp quyền cài ứng dụng**:
   - Vào *Cài đặt TV* → *Bảo mật & Hạn chế* (hoặc *Ứng dụng & Quyền riêng tư*) → *Cài đặt ứng dụng không rõ nguồn gốc* → Bật **Cho phép** (Allow) cho ứng dụng **Downloader**.
3. **Tải và cài AniBox**:
   - Mở app **Downloader** trên TV.
   - Tại ô nhập URL/Search ngay trang chủ Downloader, dùng remote gõ đúng mã số: **3170287**.
   - Bấm **Go**. App sẽ tự động tải file AniBox.apk (bản mới nhất) về máy.
   - Sau khi tải xong, chọn **Install** (Cài đặt) → Cài xong chọn **Open** (Mở).

---

## Tải trực tiếp APK (Dành cho máy tính / USB)

| Tên file APK | Phiên bản | Tương thích | Kích thước |
|---|---|---|---|
| **AniBox-v2.8.0.apk** | 2.8.0 (Build 11) | Android 6.0+ (TV, Box, Fire TV Stick) | ~258 MB |
| **AniBox.apk** | Bản mới nhất (Auto-update) | Android 6.0+ (TV, Box, Fire TV Stick) | ~258 MB |

- **Link tải trực tiếp bản mới nhất**: [Tải AniBox.apk](https://github.com/LongLeo287/AniBox-release/releases/latest/download/AniBox.apk)
- **Bản phát hành đầy đủ**: [Releases](../../releases/latest)
- **Bảo mật**: Đối chiếu mã băm SHA-256 trong file SHA256SUMS.txt.

---

## Tự động kiểm tra & Cập nhật phiên bản mới

- AniBox tự động kiểm tra ersion.json khi mở app và hiển thị thông báo khi có bản cập nhật mới. Người dùng đã cài app không cần vào Downloader gõ lại mã, mà cập nhật trực tiếp ngay trong app!
- Kiểm tra thủ công: **Cài đặt → Cập nhật & dữ liệu → Kiểm tra cập nhật ngay**.

---

## Lưu ý

- Yêu cầu hệ điều hành Android TV 6.0 trở lên (API 23+). Android < 7.1 đã được tích hợp sẵn chứng chỉ số gốc ISRG Root X1 để mở kết nối HTTPS an toàn.
- Nội dung video được tổng hợp tự động từ các nguồn công khai; AniBox không lưu trữ hay phát tán bất kỳ tệp video nào trên máy chủ riêng.