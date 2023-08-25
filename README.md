# TikTok Downloader (No Watermark)

A simple and efficient tool to download TikTok videos without any watermark. This project is hosted on the Firebase Cloud Function platform.
## Features

- **No Watermark**: Downloads TikTok videos without the distracting watermark.
- **Hosted on Firebase Cloud Function**

## How to Use

1. Send a `POST` request to the Firebase function endpoint with the desired TikTok video URL.
2. Receive the video media file in the response.

## Deployment

This project is deployed on Firebase Cloud Functions. Ensure you've done the following:

1. Create a project on firebase console
2. Install python firebase SDK
   ```shell
   pip install firebase-admin
   ```
4. Install [Firebase CLI](https://firebase.google.com/docs/cli#mac-linux-auto-script) 
   
6. Initialize firebase cloud function project ( This repo is missing some files )
   ```shell
   firebase init functions
   ```
7. Ensure all used dependencies are in 'requirements.txt' 
8. Deploy to firebase
   ```shell
   firebase deploy --only functions
   ```

## Example request

```python
import requests

url = 'YOUR_CLOUD_FUNCTION_ENDPOINT'
data = {'url': 'TIKTOK_VIDEO_URL'}
response = requests.post(url, data=data)
with open('video.mp4', 'wb') as f:
    f.write(response.content)
```


## Integration with iPhone Shortcuts
1. [Download Shortcut](https://www.icloud.com/shortcuts/84d1eab18abf40e6bbb24a653fb57407)
   ```
   NOTE: Replace the API endpoint with your own cloud function endpoint
   ```
3. Add Shortcut to Quick Actions

<img src="https://github.com/Wa-lead/firebase_cloud_tiktok_downloader/assets/81301826/47cb5d72-ca4b-4db0-85c4-244038250b32" alt="drawing" style="width:200px;"/>

