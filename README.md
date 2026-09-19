# AniBox — bản phát hành

Ứng dụng Android TV xem anime, phim bộ/lẻ và kênh TV trực tiếp. Repo này chỉ chứa **bản cài đặt** (APK) và `version.json` để app tự kiểm tra cập nhật.

## Tải về

| File | Dung lượng | Dùng khi |
|---|---|---|
| **AniBox-TV.apk** (Full) | ~270 MB | Khuyến nghị — có libVLC, giải mã AC3/DTS/EAC3/HEVC 10-bit và dịch phụ đề trên máy |
| **AniBox-TV-Lite.apk** | ~8 MB | TV yếu hoặc mạng chậm — chỉ ExoPlayer |

Bản mới nhất: **[Releases](../../releases/latest)**. Kiểm tra SHA-256 trong `SHA256SUMS.txt`.

## Cài lên TV bằng Downloader (by AFTVnews)

1. Cài **Downloader** từ cửa hàng ứng dụng của TV (Google Play / Amazon Appstore).
2. Bật cài đặt từ nguồn không xác định cho Downloader (TV sẽ hỏi lần đầu).
3. Mở Downloader, nhập đúng link tải ở phần Releases, ví dụ:
   `https://github.com/LongLeo287/AniBox-release/releases/latest/download/AniBox-TV-Lite.apk`
   (hoặc `.../AniBox-TV.apk` cho bản Full).
4. Chờ tải xong → chọn **Install** → mở AniBox.

## Cập nhật

AniBox tự kiểm tra `version.json` ở repo này khi mở app và báo khi có bản mới; cũng có thể bấm **Cài đặt → Cập nhật & dữ liệu → Kiểm tra cập nhật ngay**.

## Lưu ý

- Yêu cầu Android 6.0+ (API 23). Android < 7.1 được bổ sung chứng chỉ gốc để mở HTTPS.
- Nội dung phát đến từ các nguồn bên thứ ba công khai; AniBox không lưu trữ video.
