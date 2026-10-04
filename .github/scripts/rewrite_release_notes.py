import json
import os
import urllib.request

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com"

NOTES = {
    "v2.8.0": """## AniBox 2.8.0

### 📦 Chuẩn hóa bản phát hành
- Chuẩn hóa APK dành cho Android TV và quy trình cập nhật về sau.
- Bổ sung file APK tên ổn định `AniBox.apk` để thuận tiện cho cài đặt và cập nhật.
- Bổ sung SHA-256 để người dùng có thể kiểm tra tính toàn vẹn của file tải về.
- Hoàn thiện luồng cài nhanh bằng Downloader trên TV.

### 📺 Cài nhanh bằng Downloader
- **Code:** `3170287`
- **Short link:** `aftv.news/3170287`
- **Backup:** `tinyurl.com/anibox-latest`

AniBox tập trung vào trải nghiệm Android TV, điều hướng bằng remote, playback UX và khả năng tương thích thiết bị.""",

    "v2.8.1": """## AniBox 2.8.1

### ✨ Cải tiến
- Tinh gọn gói cài đặt và tiếp tục chuẩn hóa quy trình phát hành AniBox.
- Cải thiện trải nghiệm cài đặt/cập nhật trên Android TV.
- Duy trì APK tên ổn định để người dùng luôn có một đường dẫn tải bản mới nhất.
- Bổ sung checksum để kiểm tra tính toàn vẹn của file cài đặt.

### 📺 Cài nhanh bằng Downloader
- **Code:** `3170287`
- **Short link:** `aftv.news/3170287`
- **Backup:** `tinyurl.com/anibox-latest`

AniBox tập trung vào UX/UI, D-pad navigation, playback experience và độ ổn định trên TV/box.""",

    "v2.9.0": """## AniBox 2.9.0

### ✨ Trải nghiệm & giao diện
- Mở rộng các khu vực duyệt nội dung với rail và màn hình `Xem tất cả` tối ưu cho TV.
- Cải thiện bố cục, focus và điều hướng bằng D-pad trên các màn hình danh mục.
- Tinh chỉnh cách hiển thị media để giao diện nhất quán hơn trên màn hình lớn.

### ▶️ Playback
- Nâng cấp engine phát media với MPV và FFmpeg để tăng khả năng tương thích codec/container.
- Cải thiện xử lý các stream HLS và nhiều định dạng audio/video phức tạp.
- Sửa lỗi tỉ lệ hiển thị khiến video có thể bị zoom/crop sai.

### ⚡ Hiệu năng & ổn định
- Tối ưu thời gian tải Home và giảm nguy cơ ANR khi tìm kiếm hoặc điều hướng nhanh.
- Sửa các lỗi crash trong một số luồng mở nội dung và chuyển sang player.

AniBox tập trung vào UX/UI, navigation, playback experience và khả năng tương thích Android TV.""",

    "v2.9.1": """## AniBox 2.9.1

### 🔄 Update flow
- Nâng cấp cơ chế OTA lên versionCode 14.
- Bổ sung cơ chế bypass cache khi kiểm tra phiên bản mới để giảm tình trạng nhận metadata cũ.
- Cải thiện độ tin cậy của luồng kiểm tra và hiển thị cập nhật.

### 🛠 Ổn định
- Sửa một số trường hợp crash khi chuyển giữa các màn hình/phát media.
- Cải thiện xử lý tỉ lệ khung hình để hạn chế hiện tượng zoom/crop không đúng.

Bản cập nhật tập trung vào độ ổn định, update experience và playback compatibility.""",

    "v2.9.2": """## AniBox 2.9.2

### ✨ TV UX
- Thiết kế lại menu trên cùng với trạng thái focus/selected rõ ràng hơn và tích hợp Hero mượt hơn.
- Chuẩn hóa margin, spacing và trạng thái rail để bố cục nhất quán trên Android TV.
- Cải thiện D-pad, BACK và khả năng giữ vị trí khi người dùng di chuyển giữa các màn hình.

### ▶️ Playback & episode UX
- Bổ sung preview khi tua, chọn nhanh khoảng tập và nhập số để nhảy tới tập mong muốn.
- Tối ưu danh sách tập dài để giảm treo/giật trên thiết bị cấu hình thấp.
- Cải thiện khả năng tương thích phát media trên các phiên bản Android cũ.

### 🏷️ Metadata & presentation
- Cải thiện cách hiển thị rating, trailer và Hero.
- Tối ưu trạng thái tiến độ xem và cách trình bày metadata trên card/rail.

### ⚡ Ổn định
- Giảm lỗi liên quan tới seek, progress, episode list và bộ nhớ trên box khoảng 1 GB RAM.""",

    "v2.9.3": """## AniBox 2.9.3

### ▶️ Player UX
- Làm mới giao diện điều khiển player theo hướng TV-first: thoát, phát lại, tập tiếp theo và thao tác OK để pause/resume.
- Tua trái/phải 10 giây kèm preview để dễ tìm vị trí.
- Màn hình pause hiển thị thông tin phim/tập rõ ràng hơn.
- Bổ sung luồng `Tiếp theo` và trải nghiệm chuyển tập liền mạch hơn.

### ✨ Home & detail
- Cải thiện Hero toàn màn hình, trailer, `Xem tiếp`, age badge và các rail trên Home.
- Làm lại trang chi tiết với action gọn hơn và dải tập tối ưu cho remote.
- Bổ sung lịch dạng lưới và cải thiện presentation cho các trải nghiệm media theo thời gian.

### 🎮 TV navigation
- Sửa các lỗi D-pad, focus, BACK, layout lệch và trạng thái controller không tự ẩn.
- Cải thiện tính nhất quán khi chuyển qua lại giữa Home, detail và player.""",

    "v2.9.4": """## AniBox 2.9.4

### ✨ UX/UI
- Dùng logo/title art tốt hơn ở Hero, trang chi tiết, box art và màn hình pause.
- Tinh chỉnh Hero gọn hơn và cải thiện hành vi trailer toàn màn hình khi người dùng dừng focus.
- Mở rộng hệ rail/collection và cách trình bày bảng xếp hạng, rating và metadata.
- Làm lại bộ lọc danh mục theo hướng trực quan, dễ thao tác bằng remote.

### ▶️ Unified playback experience
- Đồng bộ giao diện và hành vi player giữa các loại media input tương thích.
- Cải thiện skip intro, reload surface, next-episode flow và trạng thái pause.
- Làm mới splash/loading để quá trình chuyển sang playback mượt và rõ trạng thái hơn.

### 🏷️ Metadata & stability
- Cải thiện trailer, subtitle, episode title và metadata presentation.
- Tăng khả năng phục hồi khi mạng chập chờn.
- Sửa các trường hợp crash khi chuyển giữa các surface/player.""",

    "v2.9.5": """## AniBox 2.9.5

### ✨ UX/UI
- Tinh chỉnh Home, Hero, rail và focus để trải nghiệm D-pad trên Android TV rõ ràng và nhất quán hơn.
- Cải thiện cách trình bày logo/title, rating, episode title, trailer và status badge.
- Tinh chỉnh splash/loading, màn pause và luồng `Tập tiếp theo`.

### ▶️ Playback experience
- Đồng bộ playback UX cho các media input tương thích.
- Cải thiện subtitle/audio track và các surface phát media.
- Tối ưu chuyển đổi giữa các player/surface để giảm gián đoạn.

### 🔄 Update & stability
- Cải thiện update notification, kiểm tra phiên bản và trạng thái cập nhật trong Settings.
- Tối ưu hiệu năng tải và khả năng phục hồi khi mạng không ổn định.
- Tăng độ ổn định tổng thể trên Android TV/box.

AniBox tập trung vào UX/UI, navigation, playback experience, subtitle/audio và media presentation."""
}

def api(path, method="GET", payload=None):
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "AniBox-release-notes-maintenance",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

for tag, body in NOTES.items():
    release = api(f"/repos/{REPO}/releases/tags/{tag}")
    api(f"/repos/{REPO}/releases/{release['id']}", method="PATCH", payload={"body": body})
    check = api(f"/repos/{REPO}/releases/{release['id']}")
    if check.get("body") != body:
        raise RuntimeError(f"Verification failed for {tag}")
    print(f"updated {tag}")
