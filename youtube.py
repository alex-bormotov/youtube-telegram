import os
import googleapiclient.errors
import google_auth_oauthlib.flow
import googleapiclient.discovery
from google.oauth2 import service_account


def youtube(scopes, credentials_file_name, videoCategoryId, regionCode, maxResults):
    SCOPES = scopes
    SERVICE_ACCOUNT_FILE = credentials_file_name
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        maxResults=maxResults,
        regionCode=regionCode,
        videoCategoryId=videoCategoryId
    )
    response = request.execute()
    return response
