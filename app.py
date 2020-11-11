from time import sleep
from fs import get_config
from youtube import youtube
from datetime import datetime
from telegram import telegram_send_message


SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CONFIG = get_config('config/config.json')
CREDENTIAL_FILE_NAME = f"config/{CONFIG['youtube_api_service_account_credentials_file_name']}"
TELEGRAM_API_KEY = CONFIG['telegram_api_key']
TELEGRAM_CHANNEL_ID = CONFIG['channel_id']
VIDEO_CATEGORY_ID = CONFIG['videoCategoryId']
REGION_CODE = CONFIG['regionCode']
MAX_RESULTS = CONFIG['maxResults']
SLEEP_TIMEOUT = CONFIG['sleep_timeout']


def get_new_videos():
    videos_dict = youtube(SCOPES, CREDENTIAL_FILE_NAME,
                          VIDEO_CATEGORY_ID, REGION_CODE, MAX_RESULTS)
    return videos_dict['items']


def format_message(videos_list):
    videos = []
    for video in videos_list:
        title = video['snippet']['title']
        views = format(int(video['statistics']['viewCount']), ",")
        likes = format(int(video['statistics']['likeCount']), ",")
        dislikes = format(int(video['statistics']['dislikeCount']), ",")
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
