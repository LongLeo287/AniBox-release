import json
import os
import urllib.request

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com"

SCOPE = """### 📺 Phạm vi AniBox
**AniBox không cung cấp, host, đóng gói hoặc phân phối phim, series, kênh truyền hình hay kho media có sẵn.**

APK trong release này chỉ chứa ứng dụng AniBox, tập trung vào UX/UI, navigation, playback experience, subtitle/audio, performance và media presentation.

**No bundled movies · No built-in media catalog · No AniBox-hosted streams**"""

NOTES = {
    "v2.8.0": """## AniBox 2.8.0

### ✨ Cải tiến
- Chuẩn hóa bản cài AniBox dành cho Android TV và quy trình phát hành về sau.
- Bổ sung file APK tên ổn định `AniBox.apk` để việc tải và cập nhật bản mới thuận tiện hơn.
- Bổ sung SHA-256 để kiểm tra tính toàn vẹn của file cài đặt.
- Hoàn thiện nền tảng update/release để các phiên bản sau có thể dùng chung một luồng phân phối.
- Cải thiện tính nhất quán khi cài đặt AniBox trên TV, box và Fire TV.

""" + SCOPE,

    "v2.8.1": """## AniBox 2.8.1

### ✨ Cải tiến
- Tinh gọn gói cài đặt và tiếp tục chuẩn hóa cấu trúc bản phát hành AniBox.
- Cải thiện trải nghiệm cài đặt và nâng cấp ứng dụng trên Android TV.
- Duy trì APK tên ổn định để người dùng luôn có một đường dẫn tải bản mới nhất.
- Bổ sung checksum đi kèm release để kiểm tra file tải về.
- Tăng tính nhất quán của quy trình phát hành trước khi chuyển sang nhánh tính năng 2.9.x.

""" + SCOPE,

    "v2.9.0": """## AniBox 2.9.0

### ✨ Cải tiến
- Nâng cấp playback engine với MPV và FFmpeg để tăng khả năng tương thích với nhiều định dạng audio/video.
- Cải thiện xử lý HLS, codec/container phức tạp và các trường hợp phát media trên thiết bị Android TV khác nhau.
- Mở rộng trải nghiệm duyệt nội dung với rail riêng, màn hình `Xem tất cả` và bố cục tối ưu cho remote.
- Cải thiện focus, D-pad navigation và độ mượt khi tìm kiếm hoặc di chuyển nhanh giữa các khu vực.
- Tối ưu thời gian tải Home và giảm nguy cơ ANR trên thiết bị cấu hình thấp.
- Sửa lỗi tỉ lệ hiển thị khiến video có thể bị zoom/crop sai và một số trường hợp crash khi chuyển sang player.

""" + SCOPE,

    "v2.9.1": """## AniBox 2.9.1

### ✨ Cải tiến
- Nâng cấp cơ chế cập nhật ứng dụng lên versionCode 14.
- Bổ sung bypass cache khi kiểm tra phiên bản mới để hạn chế tình trạng nhận metadata cũ.
- Cải thiện độ tin cậy của luồng kiểm tra và hiển thị cập nhật.
- Sửa một số trường hợp crash khi chuyển giữa các màn hình và playback surface.
- Cải thiện xử lý tỉ lệ khung hình để hạn chế hiện tượng zoom/crop không đúng.
- Tăng độ ổn định tổng thể cho quá trình mở và phát media trên Android TV.

""" + SCOPE,

    "v2.9.2": """## AniBox 2.9.2

### ✨ Cải tiến
- Thiết kế lại menu trên cùng với trạng thái focus/selected rõ ràng hơn và Hero hòa vào giao diện tự nhiên hơn.
- Chuẩn hóa margin, spacing, rail state và hành vi D-pad/BACK để trải nghiệm TV nhất quán hơn.
- Bổ sung preview khi tua, chọn nhanh khoảng tập và nhập số để nhảy tới tập mong muốn.
- Tối ưu danh sách tập dài để giảm treo/giật và sử dụng bộ nhớ hiệu quả hơn trên box cấu hình thấp.
- Cải thiện khả năng tương thích playback trên các phiên bản Android cũ.
- Cải thiện rating, trailer, Hero, tiến độ xem và cách trình bày metadata trên card/rail.
- Sửa nhiều lỗi liên quan tới seek, progress, episode list, focus và bộ nhớ trên thiết bị khoảng 1 GB RAM.

""" + SCOPE,

    "v2.9.3": """## AniBox 2.9.3

### ✨ Cải tiến
- Làm mới player theo hướng TV-first với các action rõ ràng cho Thoát, Phát lại, Tập tiếp theo và pause/resume bằng nút OK.
- Bổ sung tua trái/phải 10 giây kèm preview để tìm vị trí nhanh hơn.
- Cải thiện màn hình pause với logo/title và thông tin tập rõ ràng hơn.
- Bổ sung luồng `Tiếp theo`, chuyển tập và trải nghiệm xem liên tục mượt hơn.
- Nâng cấp Home và trang chi tiết với Hero toàn màn hình, trailer, `Xem tiếp`, age badge và dải tập tối ưu cho remote.
- Cải thiện lịch dạng lưới và cách trình bày nội dung theo thời gian trên màn hình TV.
- Sửa các lỗi D-pad, focus, BACK, layout lệch và trạng thái controller không tự ẩn.

""" + SCOPE,

    "v2.9.4": """## AniBox 2.9.4

### ✨ Cải tiến
- Cải thiện logo/title art ở Hero, trang chi tiết, box art và màn hình pause để presentation rõ ràng hơn.
- Tinh chỉnh Hero gọn hơn và cải thiện hành vi trailer toàn màn hình khi người dùng dừng focus.
- Mở rộng rail/collection, bảng xếp hạng, rating và metadata presentation theo phong cách TV hiện đại.
- Làm lại bộ lọc danh mục để dễ đọc và thao tác hơn bằng remote.
- Đồng bộ playback UX giữa các media surface, cải thiện skip intro, reload, pause và luồng `Tập tiếp theo`.
- Làm mới splash/loading để quá trình chuyển sang playback mượt và rõ trạng thái hơn.
- Cải thiện trailer, subtitle, episode title, khả năng phục hồi khi mạng chập chờn và độ ổn định khi chuyển giữa các player/surface.

""" + SCOPE,

    "v2.9.5": """## AniBox 2.9.5

### ✨ Cải tiến
- Tinh chỉnh Home, Hero, rail và focus để trải nghiệm D-pad trên Android TV rõ ràng và nhất quán hơn.
- Cải thiện cách trình bày metadata: logo/title, rating, episode title, trailer và badge trạng thái.
- Đồng bộ playback UX cho media input tương thích, subtitle/audio track và web surface khi integration cần.
- Cải thiện splash/loading, màn tạm dừng và luồng `Tập tiếp theo`.
- Cải thiện update notification, kiểm tra phiên bản và trạng thái cập nhật trong Settings.
- Tối ưu hiệu năng tải, phục hồi khi mạng chập chờn và độ ổn định khi chuyển giữa các surface/player.

""" + SCOPE,
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
