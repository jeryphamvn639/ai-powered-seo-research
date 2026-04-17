import requests
import os

# ==========================================
# CẤU HÌNH THÔNG TIN (Thay đổi tại đây)
# ==========================================
# 1. Dán API Key bạn lấy từ điện thoại vào đây
API_KEY = "sd_de0d255a0c9e5aba2d1581c9a7db73b6"

# 2. Link video YouTube của Expert (Ví dụ: Julian Goldie)
VIDEO_URL = "https://www.youtube.com/watch?v=WzVgS-LtiW8"
# ==========================================

def get_youtube_transcript(url):
    endpoint = "https://api.supadata.ai/v1/youtube/transcript"
    headers = {"x-api-key": API_KEY}
    params = {"url": url, "text": True}
    
    response = requests.get(endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json().get('content', 'Không tìm thấy nội dung transcript.')
    else:
        return f"Lỗi API: {response.status_code} - {response.text}"

if __name__ == "__main__":
    print("🚀 Đang bắt đầu lấy dữ liệu từ YouTube... Vui lòng chờ giây lát.")
    content = get_youtube_transcript(VIDEO_URL)
    
    if "Lỗi API" not in content:
        # Tự động tạo folder nếu chưa có
        folder_path = "research/youtube-transcripts"
        os.makedirs(folder_path, exist_ok=True)
        
        # Lưu file với tên dựa trên video
        file_name = os.path.join(folder_path, "koray_gubur_semantic.txt")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(content))
        
        print(f"✅ Thành công! Transcript đã được lưu tại: {file_name}")
        print("💡 Bây giờ bạn có thể Commit file này lên GitHub.")
    else:
        print(f"❌ Có lỗi xảy ra: {content}")