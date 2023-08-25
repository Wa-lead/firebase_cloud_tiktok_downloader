from firebase_functions import https_fn
from firebase_admin import initialize_app
from downloader import TikTokDownloader
from flask import Flask, request, send_file
from io import BytesIO
from enum import Enum

initialize_app()

app = Flask(__name__)
downloader = TikTokDownloader() 

class DownloadStatus(Enum):
    PRIVATE_REMOVED = 'private/removed'
    URL_INVALID = 'url-invalid'
    DOWNLOAD_LINK_NOT_FOUND = 'download-link-not-found'

@app.route('/download', methods=['POST'])
def download():
    """
    Endpoint to download a video given a URL. Returns the video file or an error string.
    """
    url = request.form.get('url')  
    if not url:
        return 'No URL provided', 400
    
    download_link = downloader.down_musical(url)
    
    if download_link in [DownloadStatus.PRIVATE_REMOVED.value, 
                         DownloadStatus.URL_INVALID.value,
                         DownloadStatus.DOWNLOAD_LINK_NOT_FOUND.value]:
        return download_link, 400 

    try:
        video = BytesIO(downloader._get_video_content(download_link))
        video.seek(0)
        return send_file(video, mimetype='video/mp4', as_attachment=True, download_name='video.mp4')
    except Exception as e:
        return "Error processing the download", 500


#---- Firebase Functions ----#
@https_fn.on_request()
def tiktok_download_no_watermark(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
            