# AniBox · Android TV

<p align="center">
  <img src="https://raw.githubusercontent.com/LongLeo287/AniBox/main/img/logo/anibox-lockup-horizontal.png" alt="AniBox" width="360">
</p>

<p align="center">
  <strong>Anime, phim và truyền hình trực tiếp trên Android TV.</strong><br>
  Bản repository này chỉ quản lý APK phát hành, checksum và metadata cập nhật.
</p>

<p align="center">
  <a href="https://github.com/LongLeo287/AniBox-release/releases/latest"><img src="https://img.shields.io/github/v/release/LongLeo287/AniBox-release?label=latest%20APK&color=e7b45f" alt="Latest APK"></a>
  <a href="https://github.com/LongLeo287/AniBox/releases"><img src="https://img.shields.io/github/v/release/LongLeo287/AniBox?label=source&color=6f42c1" alt="Source release"></a>
  <a href="SHA256SUMS.txt"><img src="https://img.shields.io/badge/SHA--256-verified-2ea44f" alt="SHA-256 verified"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/LongLeo287/AniBox/main/img/banner/anibox-tv-banner-1280x720.png" alt="AniBox TV" width="720">
</p>

## Bản mới nhất

**AniBox 2.9.5 · versionCode 18**

- [Trang release 2.9.5](https://github.com/LongLeo287/AniBox-release/releases/tag/v2.9.5)
- [Tải AniBox.apk](https://github.com/LongLeo287/AniBox-release/releases/download/v2.9.5/AniBox.apk)
- [Tải AniBox-v2.9.5.apk](https://github.com/LongLeo287/AniBox-release/releases/download/v2.9.5/AniBox-v2.9.5.apk)
- [Checksum SHA-256](https://github.com/LongLeo287/AniBox-release/releases/download/v2.9.5/SHA256SUMS.txt)

> Hai tên APK trong release là cùng một bản build. `AniBox.apk` là tên ổn định cho cơ chế cập nhật; `AniBox-v2.9.5.apk` giúp nhận biết phiên bản khi tải thủ công.

## Cài đặt nhanh

### Android TV / Android Box

1. Mở trang [Releases](https://github.com/LongLeo287/AniBox-release/releases/latest) trên máy tính hoặc trình duyệt TV.
2. Tải `AniBox.apk`.
3. Cho phép cài ứng dụng từ nguồn bạn dùng trong phần **Bảo mật / Ứng dụng không rõ nguồn gốc**.
4. Mở file APK và chọn **Install**.
5. Sau khi cài, có thể tắt lại quyền cài từ nguồn không rõ.

### Cài qua ADB

```powershell
adb install -r -d AniBox.apk
```

Nếu đang nâng cấp từ bản cũ, `-r` giữ dữ liệu ứng dụng. Chỉ cài APK tải từ trang release chính thức của repository này.

## Xác minh file tải về

Windows PowerShell:

```powershell
Get-FileHash .\AniBox.apk -Algorithm SHA256
```

Đối chiếu chuỗi hash với [SHA256SUMS.txt](https://github.com/LongLeo287/AniBox-release/releases/download/v2.9.5/SHA256SUMS.txt).

Linux / macOS:

```bash
sha256sum AniBox.apk
```

## Cập nhật trong ứng dụng

AniBox đọc metadata cập nhật từ [version.json](version.json) và kiểm tra phiên bản định kỳ. Khi có bản mới, ứng dụng hiển thị thông báo và liên kết tải từ GitHub Releases. Người dùng cũng có thể mở **Cài đặt → Hệ thống & Dữ liệu → Cập nhật ứng dụng** để kiểm tra thủ công.

## Tương thích

- Android TV / Android Box API 23 trở lên
- Kiến trúc APK phụ thuộc bản build; kiểm tra trang release nếu thiết bị yêu cầu ABI cụ thể
- Media3/ExoPlayer là player direct chính; một số nguồn có thể phụ thuộc giới hạn mạng, khu vực hoặc chính sách provider

## Ghi chú phát hành

Bản phát hành gồm các cải tiến về:

- Home, hero, rail và điều hướng D-pad;
- metadata, danh mục, tìm kiếm và artwork;
- direct playback, subtitle/audio track và fallback nguồn;
- hiệu năng khởi động, tải dữ liệu và xử lý mạng;
- cập nhật ứng dụng và kiểm tra checksum.

Xem đầy đủ thay đổi trong [release notes](https://github.com/LongLeo287/AniBox-release/releases).

## Liên kết

- [Mã nguồn AniBox](https://github.com/LongLeo287/AniBox)
- [Danh sách release và APK](https://github.com/LongLeo287/AniBox-release/releases)
- [Báo lỗi](https://github.com/LongLeo287/AniBox/issues)
- [Tài liệu kỹ thuật](https://github.com/LongLeo287/AniBox/tree/main/docs)

## Trách nhiệm

AniBox là ứng dụng client lấy dữ liệu từ các provider bên ngoài. Provider có thể thay đổi, giới hạn địa lý hoặc ngừng hoạt động. Người dùng chịu trách nhiệm tuân thủ điều khoản, bản quyền và pháp luật áp dụng. Không tải APK từ mirror không thuộc hai repository chính thức này.


