<h1 align="center">🎬 AniBox</h1>

<p align="center">
  <strong>Android TV app focused on UX/UI, navigation and playback experience.</strong><br>
  Official AniBox APK releases
</p>

<p align="center">
  <a href="https://github.com/LongLeo287/AniBox-release/releases/latest"><img src="https://img.shields.io/github/v/release/LongLeo287/AniBox-release?label=Latest&color=e7b45f" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Android%20TV-6.0%2B-3DDC84?logo=android&logoColor=white" alt="Android TV 6.0+">
  <img src="https://img.shields.io/badge/ABI-ARMv7%20%7C%20ARM64-59636e" alt="ARM ABI">
  <img src="https://img.shields.io/badge/SHA--256-verified-2ea44f" alt="SHA-256">
</p>

<p align="center">
  <a href="https://github.com/LongLeo287/AniBox-release/releases/latest"><strong>⬇ Download latest APK</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/LongLeo287/AniBox">💻 Source</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/LongLeo287/AniBox/issues">🐛 Issues</a>
</p>

---

> **AniBox không cung cấp, host, đóng gói hoặc phân phối phim, series, kênh truyền hình hay kho media có sẵn.**  
> APK trong repository này chỉ là ứng dụng AniBox. Nội dung/media được sử dụng với ứng dụng, nếu có, nằm ngoài phạm vi phân phối của AniBox.

---

## 🚀 Latest release

### AniBox 2.9.6.3

`versionCode 22` · `Android 6.0+` · `armeabi-v7a / arm64-v8a`

| File | Dùng cho |
|---|---|
| **AniBox.apk** | Tên ổn định cho updater và cài đặt thông thường |
| **AniBox-v2.9.6.3.apk** | File có version để lưu trữ / tải thủ công |
| **SHA256SUMS.txt** | Kiểm tra tính toàn vẹn file |

👉 **[Open AniBox 2.9.6.3 release](https://github.com/LongLeo287/AniBox-release/releases/tag/v2.9.6.3)**

**Có gì mới:** chọn giọng AI Thuyết minh trong Cài đặt › AniSub (Ngọc Lan, Quang Huy, giọng Google — AniSub 0.4.0); phụ đề ưu tiên đúng ngôn ngữ giọng đọc; logo tiếng Việt cho mọi phim khi có đủ bộ; Hero giữ phim sau BACK; trailer ẩn chú thích nhạc. Xem [CHANGELOG](https://github.com/LongLeo287/AniBox/blob/main/CHANGELOG.md).

---

## 📺 Install

### Downloader by AFTVnews — mã vĩnh viễn `3170287`

Trên **Android TV / Google TV / Fire TV**, có thể cài AniBox nhanh mà không cần nhập URL GitHub dài:

| Phương thức | Giá trị |
|---|---|
| **Downloader code** | **`3170287`** |
| **Short link** | [`aftv.news/3170287`](https://aftv.news/3170287) |
| **Backup** | [`tinyurl.com/anibox-latest`](https://tinyurl.com/anibox-latest) |
| **Direct APK** | [`AniBox.apk`](https://github.com/LongLeo287/AniBox-release/releases/latest/download/AniBox.apk) |

1. Mở **Downloader by AFTVnews**.
2. Nhập **`3170287`** vào ô URL/Search rồi chọn **Go**.
3. Nếu mã số không truy cập được, nhập **`aftv.news/3170287`**.
4. Nếu short link chính gặp sự cố, dùng backup **`tinyurl.com/anibox-latest`**.
5. Tải APK và chọn **Install**.

> Mã **`3170287`** được cấu hình để trỏ tới URL ổn định **`releases/latest/download/AniBox.apk`**, nên không cần thay mã khi AniBox phát hành phiên bản mới.

### Tải APK trực tiếp

1. Tải **AniBox.apk** từ [Latest Release](https://github.com/LongLeo287/AniBox-release/releases/latest).
2. Cho phép cài ứng dụng từ nguồn đang dùng.
3. Mở APK → **Install**.
4. Khi nâng cấp, cài đè bản cũ để giữ dữ liệu.

### ADB

```bash
adb install -r -d AniBox.apk
```

---

## 🔐 Verify download

### Windows PowerShell

```powershell
Get-FileHash .\AniBox.apk -Algorithm SHA256
```

### Linux / macOS

```bash
sha256sum AniBox.apk
```

Đối chiếu kết quả với **SHA256SUMS.txt** trong cùng release.

---

## 🔄 In-app update

AniBox dùng `version.json` để kiểm tra bản ứng dụng mới và trỏ tới APK chính thức trong repository này. Từ 2.9.6, ứng dụng chỉ cài bản cập nhật khi SHA-256 của APK và chứng chỉ ký khớp với `version.json`. Từ 2.9.6-hotfix, có bản mới thì **bắt buộc cập nhật khi mở app** (đang xem chỉ nhắc nhẹ); `"mandatory": false` trong `version.json` chuyển về cập nhật mềm.

<p>
  <img src="https://img.shields.io/badge/STABLE%20URL-AniBox.apk-111111?style=flat-square" alt="Stable APK">
  <img src="https://img.shields.io/badge/CHECKSUM-SHA--256-111111?style=flat-square" alt="SHA-256">
  <img src="https://img.shields.io/badge/APP%20RELEASE-GitHub%20Releases-111111?style=flat-square" alt="GitHub Releases">
</p>

---

## 🔗 Links

- 💻 [AniBox source](https://github.com/LongLeo287/AniBox)
- 📦 [All releases](https://github.com/LongLeo287/AniBox-release/releases)
- 📚 [Technical docs](https://github.com/LongLeo287/AniBox/tree/main/docs)
- 🐛 [Report an issue](https://github.com/LongLeo287/AniBox/issues)

---

<p align="center">
  <sub><strong>No bundled movies · No built-in media catalog · No AniBox-hosted streams</strong></sub>
</p>

<p align="center">
  <strong>ANIME FOR A BRIGHTER DAY</strong>
</p>
