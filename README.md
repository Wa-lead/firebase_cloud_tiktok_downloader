# TikTok Downloader (No Watermark)

A simple and efficient tool to download TikTok videos without any watermark. This project is hosted on the Firebase Cloud Function platform, offering fast response times and seamless integration with other Firebase services.

## Features

- **No Watermark**: Downloads TikTok videos without the distracting watermark.
- **Hosted on Firebase Cloud Function**

## How to Use

1. Send a `POST` request to the Firebase function endpoint with the desired TikTok video URL.
2. Receive the video media file in the response.

## Deployment

This project is deployed on Firebase Cloud Functions. Ensure you have Firebase CLI set up and authenticated.

1. Download firebase cli
2. Initialize firebase cloud function project
'''
firebase init functions
'''
3. Ensure all dependencies are in 'requirements.txt'
4. Deploy to firebase
'''
firebase deploy --only functions
'''

## Example request

```python
import requests

url = 'YOUR_CLOUD_FUNCTION_ENDPOINT'
data = {'url': 'TIKTOK_VIDEO_URL'}
response = requests.post(url, data=data)
with open('video.mp4', 'wb') as f:
    f.write(response.content)
```
