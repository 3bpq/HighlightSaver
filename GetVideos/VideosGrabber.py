import json, requests, os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))


def VideosGrabber(url):
    Data = requests.get(url)

    imageCounter = 0

    with open(f"{dir_path}/templates/Videos.txt", 'w+') as file:
        file.write("""
    <html>
    <body>""")
        for item in Data.json()['data']['reels_media'][0]['items']:
            if item['is_video'] == True:
                img_data = requests.get(item['display_url']).content
                with open(f'{dir_path}/templates/images/{imageCounter}.jpg', 'wb') as handler:
                    handler.write(img_data)
                file.write(f"""<a href="{item['video_resources'][0]['src']}"><img src=f"./images/{imageCounter}.jpg" width="400" height="500"></a>\n""")
                imageCounter += 1
        file.write("""</body>
    </html>""")
        file.close()

    p = Path(f"{dir_path}/templates/Videos.txt")
    p.rename(p.with_suffix('.html'))