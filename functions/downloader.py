import requests
from bs4 import BeautifulSoup

class TikTokDownloader:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"
        }

    def _get_download_link(self, page_content, url):
        parse = BeautifulSoup(page_content, 'html.parser')
        link_url_input = parse.find('input', id='link_url')
        data = {link_url_input.get("name"): url}
        for i in parse.find_all('input', id=lambda x: x != 'link_url'):
            data[i.get("name")] = i.get("value")
        return data

    def _get_video_content(self, download_link):
        return requests.get(download_link).content

    def down_musical(self, url):
        try:
            with requests.Session() as ses:
                ses.headers.update(self.headers)
                server_url = 'https://musicaldown.com/'
                req = ses.get(server_url)
                data = self._get_download_link(req.text, url)
                post_url = server_url + "id/download"
                req_post = ses.post(post_url, data=data, allow_redirects=True)
                
                if any(msg in req_post.text for msg in ['This video is currently not available', 'Video is private or removed!']):
                    return 'private/removed'
                elif 'Submitted Url is Invalid, Try Again' in req_post.text:
                    return 'url-invalid'
                
                get_all_blank = BeautifulSoup(req_post.text, 'html.parser').find_all('a', target='_blank')
                if get_all_blank:
                    download_link = get_all_blank[0].get('href')
                    return download_link
                else:
                    return 'download-link-not-found'
            
        except IndexError:
            return 'error'
