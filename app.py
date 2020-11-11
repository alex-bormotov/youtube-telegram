# In youtube func:
# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

import locale
from time import sleep
from fs import get_config
from youtube import youtube
from datetime import datetime
from telegram import telegram_send_message


SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CONFIG = get_config('config/config.json')
CREDENTIAL_FILE_NAME = CONFIG['config/youtube_api_service_account_credentials_file_name']
TELEGRAM_API_KEY = CONFIG['telegram_api_key']
TELEGRAM_CHANNEL_ID = CONFIG['channel_id']
VIDEO_CATEGORY_ID = CONFIG['videoCategoryId']
REGION_CODE = CONFIG['regionCode']
MAX_RESULTS = CONFIG['maxResults']
SLEEP_TIMEOUT = CONFIG['sleep_timeout']

locale.setlocale(locale.LC_ALL, 'en_US')


def get_new_videos():
    videos_dict = youtube(SCOPES, CREDENTIAL_FILE_NAME,
                          VIDEO_CATEGORY_ID, REGION_CODE, MAX_RESULTS)
    return videos_dict['items']


def format_message(videos_list):
    videos = []
    for video in videos_list:
        title = video['snippet']['title']
        views = locale.format_string(
            "%d", int(video['statistics']['viewCount']), grouping=True)
        likes = locale.format_string(
            "%d", int(video['statistics']['likeCount']), grouping=True)
        dislikes = locale.format_string(
            "%d", int(video['statistics']['dislikeCount']), grouping=True)
        url = f"https://youtube.com/watch?v={video['id']}"

        videos.append(
            f"\n\n*{title}*\n\n*Views: {views}*\n*Likes: {likes}*\n*Dislikes: {dislikes}*\n\n[Watch on YouTube.com]({url})")
    return videos


def send_videos():
    while True:
        try:
            videos = get_new_videos()
            if len(videos) > 1:
                video_formated = format_message(videos)
                for video in video_formated:
                    telegram_send_message(
                        TELEGRAM_API_KEY, TELEGRAM_CHANNEL_ID, video)
                    sleep(SLEEP_TIMEOUT)
                return
        except Exception:
            sleep(SLEEP_TIMEOUT)


def main():
    send_videos()
    while True:
        if int(datetime.strftime(datetime.utcnow(), '%H')) == 7:
            send_videos()


if __name__ == "__main__":
    main()